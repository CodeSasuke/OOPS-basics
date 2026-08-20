"""Using a class from another file.

Without a reusable ``Vehicle`` class, every client would duplicate vehicle
data and display logic. The solution is to import the finished class and use
its public interface here.
"""

import method_example


def main():
    print("WITHOUT REUSE")
    print("The client would need to duplicate Vehicle's data and methods")

    print("\nWITH REUSE")
    my_car = method_example.Vehicle("Honda", "Civic", 2022)
    print("This is my car:")
    print(my_car.make)
    print(my_car.display_info())

if __name__ == "__main__":
    main()