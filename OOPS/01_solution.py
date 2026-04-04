""" Basic class and object """
""" Class method and self """
""" inheritance """
""" Encapsulation Private attribute __brand """
""" """

class Car:

    total_car = 0

    def __init__(self , brand, model):      
        self.__brand = brand
        self.model = model
        # self.total_car += 1
        Car.total_car += 1

    def get_brand(self):    # not compalsorily get name of method
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fual_type(self):
        return "Pertrol charges "

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fual_type(self):
        return "Electric charges "

print("=====================")
# my_tesla = ElectricCar("Tesla","S","100wh")     
# print(my_tesla.brand) // brand is private attribute so direct acess are not allowed
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.fual_type())

print("=====================")
my_safari = Car("Safari", "sf")

print(my_safari.full_name())
print(my_safari.fual_type())

print("=====================")
# no of object created of the class
print(Car.total_car)

print("=====================")
# my_class = Car("Toyota", "Corolla")
# print(my_class.brand)
# print(my_class.model)
# print(my_class.full_name())
# print(my_class.fual_type())

print("=====================")
# my_class_new = Car("Tata", "Safari")
# print(my_class_new.brand)
# print(my_class_new.model)
# print(my_class_new.full_name())

