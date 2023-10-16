# ezserialize 1.0

### An easy to use python json serializer and deserializer for custom objects using similar syntax to dataclasses

## Install
On the terminal, type the following command:<br>
```pip install ezserialize```

## Usage

```py
# Import ezserialize
from ezserialize import serializable, serialize, deserialize, List, pretty_print
# Use your IDE to inspect the rest of the functions which are similar to the ones imported

# Tell ezserialize which objects you want to serialize. Each attribute must be serializable aswell

@serializable
class Pet:
    pet_type: str
    name: str
    age: int
    weight: float

@serializable
class Person:
    name: str
    age: int
    profession: str
    pets: List(Pet)
# When you use a default value, the type hint can be avoided, except for lists. Always use ezserialize.List and not 'list' for type hinting.

# Create your object. The __init__ method is automatically implemented, and use keyword arguments
person = Person(
    name = "John",
    age = 19,
    profession = "vet",
    pets = [
        Pet(
            pet_type = "cat",
            name = "luna",
            age = 6,
            weight = 2.5,
        ),
    ]
)

# Serialize your object to make it a JSON dict. You can then save it to a file using ezserialize.save() or manually dumping it using builtins.json
serialized_person = serialize(person)

# When you need your person back, use deserialize with the JSON object and the type you want back
deserialized_person = deserialize(serialized_person, Person)

# When you print the person (using pretty_print/(pretty_format for the string alone)) person and deserialized_person should look the same
print("Normal:")
pretty_print(person)
print("Deserialized:")
pretty_print(deserialized_person)
```