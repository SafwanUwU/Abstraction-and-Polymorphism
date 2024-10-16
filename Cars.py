class Ferrari:
    def __init__(self):
        self.name = "Ferrari"

    def fuel_type(self):
        print(f"{self.name} fuel type: Petrol")

    def max_speed(self):
        print(f"{self.name} max speed: 350")


class BMW:
    def __init__(self):
        self.name = "BMW"

    def fuel_type(self):
        print(f"{self.name} fuel type: Diesel")

    def max_speed(self):
        print(f"{self.name} max speed: 240")


class Peugeot:
    def __init__(self):
        self.name = "Peugeot"

    def fuel_type(self):
        print(f"{self.name} fuel type: Petrol")

    def max_speed(self):
        print(f"{self.name} max speed: 208")


class Pagani:
    def __init__(self):
        self.name = "Pagani"

    def fuel_type(self):
        print(f"{self.name} fuel type: Diesel")

    def max_speed(self):
        print(f"{self.name} max speed: 384")


class Mazda:
    def __init__(self):
        self.name = "Mazda"

    def fuel_type(self):
        print(f"{self.name} fuel type: Octane")

    def max_speed(self):
        print(f"{self.name} max speed: 260")


class McLaren:
    def __init__(self):
        self.name = "McLaren"

    def fuel_type(self):
        print(f"{self.name} fuel type: Petrol")

    def max_speed(self):
        print(f"{self.name} max speed: 402")


ferrari = Ferrari()
bmw = BMW()
peugeot = Peugeot()
pagani = Pagani()
mazda = Mazda()
mclaren = McLaren()

for car in (ferrari, bmw, peugeot, pagani, mazda, mclaren):
    car.fuel_type()
    car.max_speed()

