""" Basic class and object """

class Car:
    def __init__(self , brand, model):      
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"

my_class = Car("Toyota", "Corolla")
print(my_class.brand)
print(my_class.model)
print(my_class.full_name())

my_class_new = Car("Tata", "Safari")
print(my_class_new.brand)
print(my_class_new.model)
print(my_class_new.full_name())