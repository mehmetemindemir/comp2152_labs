from Person import Person
class Student(Person):
    def __init__(self, name, age, height, major):      
        super().__init__(name, age, height)
        self.major = major
        print("Student object created")
    def __del__(self):
        print("The garbage collector is deleting the object")
    
s1 = Student("John", 36, 6.1, "Computer Science")
print(s1.name)
