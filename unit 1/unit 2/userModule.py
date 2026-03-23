class FordCars:
    def _init_(self, color, speed, name, interior):
        self.color = color
        self.speed = speed
        self.name = name
        self.interior = interior

    def startEngine(self):
        print(self.name + "engine started.")

    def seating(self):
        if self.interior == "leather":
            print(self.name + "only has 2 seats")


def doSomthingCool():
    print("wow")