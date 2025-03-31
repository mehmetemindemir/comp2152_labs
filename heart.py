import random


class Heart:
    def __init__(self):
        self.bpm = 72 # Default heart rate

    def beat(self):
        print("Lub-dub")
        self.bpm = random.randint(70, 75) # Simulate heart rate change

    def __str__(self):
        return f"Heart rate: {self.bpm} bpm."
    
    def __eq__(self, other):
        return self.bpm == other.bpm