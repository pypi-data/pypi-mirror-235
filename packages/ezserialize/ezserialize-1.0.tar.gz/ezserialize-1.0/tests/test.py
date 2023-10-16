from src.ezserialize.ezserialize import serializable, serialize, List, deserialize, pretty_print

@serializable
class Wheel:
    radius = 0.5
    type = "winter"
    
@serializable
class Engine:
    speed = 500.0
    power = 650

@serializable
class Car:
    w = 4.5
    h = 1.5
    wheels: List(Wheel)
    num_doors = 5
    engine: Engine
            
def main():
    car = Car(wheels = [Wheel() for _ in range(4)], engine = Engine(speed=300))
    pretty_print(deserialize(serialize(car), Car))
    
main()