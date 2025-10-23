class Bottole:
    def __init__(self,color,shape,height,width):
        print("i am constructore")
        self.color=color
        self.shape=shape
        self.height=height
        self.width=width
    def iam_shape(self):
        
        return f"i am shape of bottole{self.shape}"
    def iam_color(self):
        return f"i am color of bottole {self.color}"
t1=Bottole("blue","cylinder","1 feet","3 inches dia")

print(t1.iam_color())
print(t1,"i am t1")



    
class Car:
    def __init__(self, brand, model, color, year):
        print("Car object created!")
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def car_details(self):
        return f"This is a {self.color} {self.brand} {self.model} made in {self.year}."

    def start_engine(self):
        return f"The {self.model}'s engine has started!"


c1 = Car("Tesla", "Model S", "Red", 2023)
print(c1,"i am c1")

print(c1.car_details())
print(c1.start_engine())



class Dog:
    def __init__(self, name, breed, age):
        print("Dog object created!")
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} is barking loudly!"

    def details(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."


d1 = Dog("Bruno", "Labrador", 3)

print(d1.details())
print(d1.bark())
print(d1,"i am d1")