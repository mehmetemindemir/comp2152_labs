from mammal import Mammal
class Puma(Mammal):
    def __init__(self, age, tick=None):
        super().__init__(age)
        if tick :
            self.tick = tick

    def speak(self):
        print("Grrrrr")

    def __str__(self):
        return f"Puma, Age: {self.age}, {self.heart}"
    
    def claw(self):
        print("Puma claws")