"""Static methods: utility behavior that needs no object state.

Without ``@staticmethod``, callers may create a meaningless ``House`` just
to run a utility. The solution keeps the function on the class namespace
while making its lack of ``self`` explicit.
"""


class House:
    def __init__(self, number_rooms:int, address:str):
        self.number_rooms = number_rooms
        self.address = address

    @staticmethod
    def display_name():
        name = "Siddhant"
        print(f"The name of the owner is {name}")

def client():
    print("WITHOUT A STATIC METHOD")
    print("A utility function would live outside House or need an object")

    print("\nWITH A STATIC METHOD")
    # my_house = House(5, "123 Main St")
    # my_house.display_name()
    # dhanushya_house = House(3, "456 Elm St")
    # dhanushya_house.display_name()
    House.display_name()  # Calling the static method directly from the class

if __name__ == "__main__":
    client()

    