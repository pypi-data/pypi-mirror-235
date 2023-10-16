"Easy to use python json serializer and deserializer for custom objects using syntax similar to dataclasses"
import json

_FIELDSSIG = "_ezserialize_fields_"
_TYPES = [int, float, bool, type(None), str]
_TYPESSTR = [t.__name__ for t in _TYPES]


class EZSerializeError(Exception):
    ...


class SerializeDefinitionError(EZSerializeError):
    ...


class SerializeError(EZSerializeError):
    ...


def _non_serializable_error(cls, a_name, a_type):
    raise SerializeDefinitionError(
        f"In serializable class {cls.__name__}, '{a_name}' attribute has a non-serializable type hint/default value '{a_type.__name__}'. Serializable types are @serializable classes and {_TYPESSTR}. Remember to use ezserialize.List<T> to type hint lists")


class _field:
    def __init__(self, name, type_, default):
        self.name = name
        self.type = type_
        self.default = default

    def __str__(self):
        return f"Field(name={self.name}, type={self.type}, default={self.default})"
    __repr__ = __str__


class _missing_meta(type):
    def __str__(self):
        return "MissingDefault"
    __repr__ = __str__


class _missing(metaclass=_missing_meta):
    ...


class List:
    """Allows to serialize lists. Use this type hint opposed to 'list' and specify the elements type in the constructor"""
    element_type = _missing
    __name__ = "List"

    def __init__(self, element_type: type):
        self.element_type = element_type

    def __str__(self):
        return f"List<{self.element_type.__name__ if not isinstance(self.element_type, List) else str(self.element_type)}>"
    __repr__ = __str__
    
    def _ezserialize_print_(self, tabs, elements):
        res = "[\n"
        str_tabs, inner_tabs = "\t"*tabs, "\t"*(tabs+1)
        for element in elements:
            if hasattr(self.element_type, _FIELDSSIG):
                res += f"{inner_tabs}{element._ezserialize_print_(tabs+1)},\n"
            elif isinstance(self.element_type, List):
                res += f"{inner_tabs}{element._ezserialize_print_(tabs+1, element)},\n"
            else:
                res += f"{inner_tabs}{element},\n"
        res += f"{str_tabs}]"
        return res


class SerializableType:
    _ezserialize_fields_: dict[str, _field]


def _type_serializable(type_):
    return type_ in _TYPES or isinstance(type_, List) or hasattr(type_, _FIELDSSIG)


def _value_serializable(value):
    return isinstance(value, tuple(_TYPES+[list])) or hasattr(value.__class__, _FIELDSSIG)


def _is_dunder(name: str):
    return name.startswith("__") and name.endswith("__")


def _is_method(method):
    return hasattr(method, "__call__") and not hasattr(method, _FIELDSSIG)


def _default_from_type(type_):
    if type_ is int:
        return 0
    elif type_ is float:
        return 0.0
    elif type_ is str:
        return ""
    elif type_ is bool:
        return False
    elif isinstance(type_, List):
        return []
    else:
        return None


def _get_default(cls, name, pydefault=_missing):
    return getattr(cls, name, pydefault)


def _get_field(name, type_, default):
    return _field(name, type_, default)


def _add_init(cls):
    def _init_(self, **kwargs):
        # from parameters
        for a_name, a_val in kwargs.items():
            setattr(self, a_name, a_val)
        # from defaults
        for field in getattr(cls, _FIELDSSIG).values():
            if field.name not in kwargs:
                if field.default is not _missing:
                    setattr(self, field.name, field.default)
                else:
                    setattr(self, field.name, _default_from_type(field.type))

    cls.__init__ = _init_


def _add_print(cls):
    def _ezserialize_print_(self, tabs):
        fields = getattr(self, _FIELDSSIG)
        str_tabs, inner_tabs = "\t"*tabs, "\t"*(tabs+1)
        res = f"{cls.__name__}(\n"
        for a_name, a_val in vars(self).items():
            if a_name in fields:
                type_ = fields[a_name].type
                if hasattr(type_, _FIELDSSIG):
                    res += f"{inner_tabs}{a_name}: {type_.__name__} = {a_val._ezserialize_print_(tabs+1)},\n"
                elif isinstance(type_, List):
                    res += f"{inner_tabs}{a_name}: {str(type_)} = {type_._ezserialize_print_(tabs+1, a_val)},\n"
                else:
                    res += f"{inner_tabs}{a_name}: {type_.__name__} = {str(a_val)},\n"
        return res+f"{str_tabs})"

    cls._ezserialize_print_ = _ezserialize_print_


def serializable(cls):
    """Decorator that inspect the class signature and fields to add the _ezserialize_fields_ attribute to it, used for serialization and deserialization. The class attributes must be serializable. The class __init__ method will be overridden"""
    cls_annotations = cls.__annotations__
    fields = {}

    # type hinted fields
    for a_name, a_type in cls_annotations.items():
        if not _type_serializable(a_type):
            _non_serializable_error(cls, a_name, a_type)
        field = _get_field(a_name, a_type, _get_default(cls, a_name, _missing))
        fields[a_name] = field

    # non-type hinted fields with serializable default
    for d_name in dir(cls):
        if not _is_dunder(d_name) and not d_name in fields and not _is_method(getattr(cls, d_name)):
            value = _get_default(cls, d_name, _missing)
            type_ = type(value)
            if not _value_serializable(value):
                _non_serializable_error(cls, d_name, type_)
            field = _get_field(d_name, type_, value)
            fields[d_name] = field

    _add_init(cls)
    _add_print(cls)
    setattr(cls, _FIELDSSIG, fields)

    return cls

def pretty_format(serializable_obj):
    """Return a string of the object with newlines and tabs"""
    if (not hasattr(serializable_obj, _FIELDSSIG)):
        raise SerializeError(f"Only an object marked with @serializable supports formatting, not '{type(serializable_obj).__name__}'")
    return serializable_obj._ezserialize_print_(0)

def pretty_print(serializable_obj):
    """Print a string of the object with newlines and tabs"""
    if (not hasattr(serializable_obj, _FIELDSSIG)):
        raise SerializeError(f"Only an object marked with @serializable supports formatting, not '{type(serializable_obj).__name__}'")
    print(serializable_obj._ezserialize_print_(0))

def is_serializable_obj(serializable_obj):
    """Check if the object has the '_ezserialize_fields_' attribute"""
    return hasattr(serializable_obj, _FIELDSSIG)

def _serialize_list(obj):
    return [serialize(o) for o in obj]


def _serialize_obj(obj):
    return {field.name: serialize(getattr(obj, field.name, None)) for field in getattr(obj, _FIELDSSIG, {}).values()}


def serialize(serializable_obj: int | float | bool | str | list | SerializableType | None) -> int | float | bool | str | list | dict | None:
    """Serialize a serializable object to its respective python object"""

    if not _value_serializable(serializable_obj):
        raise SerializeError(
            f"'{serializable_obj}' is not serializable. Serializable types are @serializable classes and {_TYPESSTR} + lists")
    if isinstance(serializable_obj, (int, float, bool, str, type(None))):
        return serializable_obj
    elif isinstance(serializable_obj, list):
        return _serialize_list(serializable_obj)
    elif hasattr(serializable_obj.__class__, _FIELDSSIG):
        return _serialize_obj(serializable_obj)
    raise SerializeError(
        f"Could not serialize '{serializable_obj}' (unknown error)")


def serialize_str(serializable_obj: int | float | bool | str | list | SerializableType | None) -> str:
    """Serialize a serializable object to its respective python object, and then converts it to a JSON string using builtins.json"""
    return json.dumps(serialize(serializable_obj))


def _deserialize_list(obj, type_):
    return [deserialize(o, type_.element_type) for o in obj]


def _deserialize_obj(obj, type_):
    return type_(**{key: deserialize(value, getattr(type_, _FIELDSSIG)[key].type) for key, value in obj.items()})


def deserialize(serialized_obj: int | float | bool | str | list | dict | None, type_: type | List) -> int | float | bool | str | list | SerializableType | None:
    """Deserialize a serialized object to the requested type as specified in the type_ parameter"""
    if not _type_serializable(type_):
        raise SerializeError(
            f"'{type_}' is not deserializable. Deserializable types are @serializable classes and {_TYPESSTR}")
    if type_ in [int, float, bool, type(None), str]:
        return serialized_obj
    elif isinstance(type_, List):
        return _deserialize_list(serialized_obj, type_)
    elif hasattr(type_, _FIELDSSIG):
        return _deserialize_obj(serialized_obj, type_)
    raise SerializeError(
        f"Could not deserialize '{serialized_obj}' (unknown error)")


def deserialize_str(serialized_str: str, type_: type | List) -> int | float | bool | str | list | SerializableType | None:
    """Deserialize a serialized object in the form of a string (loaded with builtins.json) to the requested type as specified in the type_ parameter"""
    return deserialize(json.loads(serialized_str), type_)


def save(serialized_obj: int | float | bool | str | list | dict | None, filepath: str):
    """Saves a serialized object to a file"""
    with open(filepath, "w") as file:
        json.dump(serialized_obj, file)


def save_str(serialized_str: str, filepath: str):
    """Saves a serialized object in the form of a string to a file"""
    with open(filepath, "w") as file:
        file.write(serialized_str)


def load(type_: type | List, filepath: str) -> int | float | bool | str | list | SerializableType | None:
    """Load a serialized object from a file and return the deserialized version of it with the requested type specified by the type_ parameter"""
    with open(filepath, "r") as file:
        return deserialize(json.load(file), type_)
