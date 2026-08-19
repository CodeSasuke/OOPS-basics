class House:
    def __init__(self, number_rooms:int, address:str):
        self.number_rooms = number_rooms
        self.address = address

    @staticmethod
    def display_name():
        name = "Siddhant"
        print(f"The name of the owner is {name}")

def client():
    # my_house = House(5, "123 Main St")
    # my_house.display_name()
    # dhanushya_house = House(3, "456 Elm St")
    # dhanushya_house.display_name()
    House.display_name()  # Calling the static method directly from the class

if __name__ == "__main__":
    client()

    