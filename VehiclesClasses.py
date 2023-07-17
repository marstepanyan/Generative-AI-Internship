from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

    def honk(self):
        print(f"{self.make} {self.model} says honk!")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def start(self):
        print("The key is turned, the starter motor  activated.")
        print(f"{self.make} {self.model} with {self.num_doors} doors is starting.")

    def honk(self):
        print(f"{self.make} {self.model} says beep!")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def start(self):
        print("The key is turned, the starter motor  activated.")
        print(f"{self.make} {self.model} with {self.num_wheels} wheels is starting.")

    def stop(self):
        print(f"{self.make} {self.model} with {self.num_wheels} wheels is stopping.")

    def wheelie(self):
        print(f"{self.make} {self.model} is popping a wheelie!")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def start(self):
        print("The rider initiates motion by pedaling.")
        print(f"{self.make} {self.model} with {self.num_gears} gears is starting.")

    def pedal(self):
        print(f"{self.make} {self.model} is pedaling smoothly.")


car = Car("Ferrari", "911 Carrera", 2023, 2)
motorcycle = Motorcycle("Harley Davidson", "Sportster", 2023, 2)
bicycle = Bicycle("Trek", "FX 3", 2023, 21)


vehicles = [car, motorcycle, bicycle]
for vehicle in vehicles:
    vehicle.start()
    vehicle.honk()
    vehicle.stop()
    print()
