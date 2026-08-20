class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


def main():
    my_animal = Animal("Dog")
    print(my_animal.speak())

    # Python supplies my_animal as self in this call.
    print(Animal.speak(my_animal))


if __name__ == "__main__":
    main()
