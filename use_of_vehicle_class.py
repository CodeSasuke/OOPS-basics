import method_example
def main():
    my_car = method_example.Vehicle("Honda", "Civic", 2022)
    print("This is my car:")
    print(my_car.make)
    print(my_car.display_info())

if __name__ == "__main__":
    main()