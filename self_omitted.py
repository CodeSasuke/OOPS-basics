class Animal:
    def __init__(self, name: str):
        self.name = name

    
    def speak(self):
        print(f"{self.name} makes a sound.")

    my_animal = Animal("Dog")
    my_animal.speak() # inside empty bracket im actually passing my_animal.


if __name__ == "__main__":
    main()
