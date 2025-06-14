import random

class Car:
    def __init__(self, id, fuel_capacity, fuel_consumption, injection_type, color, weight, wheels):
        self.id = id
        self.fuel_capacity = fuel_capacity
        self.fuel_level = random.uniform(0.2, 1.0) * fuel_capacity
        self.fuel_consumption = fuel_consumption
        self.injection_type = injection_type
        self.color = color
        self.weight = weight
        self.wheels = wheels
        self.damage = 0

    def drive(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
        else:
            self.damage += 10

    def refuel(self, amount):
        self.fuel_level = min(self.fuel_capacity, self.fuel_level + amount)

    def __str__(self):
        return f"Car {self.id}: Fuel = {self.fuel_level:.2f}, Damage = {self.damage}"


class FuelStation:
    def __init__(self, fuel_volume, num_pumps, fueling_time_per_car):
        self.fuel_volume = fuel_volume
        self.num_pumps = num_pumps
        self.fueling_time_per_car = fueling_time_per_car

    def refuel_car(self, car):
        if self.fuel_volume <= 0:
            return
        amount_to_fill = car.fuel_capacity - car.fuel_level
        fuel_given = min(amount_to_fill, self.fuel_volume)
        car.refuel(fuel_given)
        self.fuel_volume -= fuel_given

    def __str__(self):
        return f"FuelStation: Fuel Left = {self.fuel_volume:.2f}"


cars = [Car(id=i, fuel_capacity=random.randint(40, 60),
            fuel_consumption=random.uniform(0.05, 0.15),
            injection_type=random.choice(['carburetor', 'injection']),
            color=random.choice(['red', 'blue', 'black']),
            weight=random.randint(1000, 1500),
            wheels=4) for i in range(5)]

station = FuelStation(fuel_volume=300, num_pumps=2, fueling_time_per_car=5)

for car in cars:
    distance = random.randint(50, 150)
    car.drive(distance)
    if car.fuel_level < car.fuel_capacity * 0.2:
        station.refuel_car(car)
    print(car)
    print('-' * 40)
