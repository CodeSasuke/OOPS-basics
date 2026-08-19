class Student:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"My name is {self.name}")

    def introduce_2(self):
        print(f"Object recieved: {self}")


student1 = Student("Dhanushya")
student2 = Student("Siddhant")
student1.introduce_2()  
student2.introduce_2()  

