"""Classes and methods: organize data with behavior.

Without a class, vehicle data and display logic would be separate values and
functions that callers must keep matched manually. The solution groups the
data with the methods that use it, while ``@staticmethod`` handles behavior
that does not need an object.
"""


class Vehicle:
    def __init__(self, make: str, model: str, year: int): # whereas make is a parameter
        self.make = make # the make of the object is stored in the instance variable 'make'
        self.model = model # the model of the object is stored in the instance variable 'model'
        self.year = year

    # This is a function inside a class, Thus it is a method.
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    @staticmethod
    def get_info():
        return "This is a simple vehicle information display method."

def main():
    my_car = Vehicle("Toyota", "Innova", 2020) # toyota is argument and arguments are actual
    print("Without a class, vehicle data and display logic would be separate")
    print(my_car.display_info())
    print(Vehicle.get_info())
    # Vehicle.display_info()
    my_car.display_info()

if __name__ == "__main__":
    main()


# memory somewher i have stored my object
# to access it i need a pointer to that memory location
# the name of the object is used to access the object and its methods and attributes.

# question 
# What is the difference between self.attribute and a local variable inside a method?

class House:
    def __init__(self, number_rooms:int, address:str):
        self.number_rooms = number_rooms
        self.address = address
        name = "Siddhant"
        print(f"The name of the owner is {name} and the address is {self.address} and the number of room in the house are: {self.number_rooms}")

    @staticmethod
    def display_name():
        name = "Siddhant"
        print(f"The name of the owner is {name}")

def client():
    my_house = House(5, "123 Main St")
    my_house.display_name()

# What happens if self is omitted?