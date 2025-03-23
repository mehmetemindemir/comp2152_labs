class Person:
    def __init__(self, name, age,height):
        self.name = name
        self.age = age
        self.height = height
        self.public_prop="I am public"
    def __del__(self):
        print("The garbage collector is deleting the object")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height    