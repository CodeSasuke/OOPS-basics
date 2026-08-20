"""Beginner notes: how Python binds methods to objects.

When a method is called through an object, Python automatically passes that
object as the first argument, usually named ``self``. This is called method
binding.

Without binding, calling a method through an object would fail because the
method would not know which object's data to read. The solved calls below
show both object syntax and explicit class syntax.
"""


class Student:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"My name is {self.name}")

    def introduce_2(self):
        print(f"Object received: {self}")


student1 = Student("Dhanushya")
student2 = Student("Siddhant")

print("Without binding, introduce() would not know which student to use")

# These are bound method calls. Python supplies student1/student2 as self.
student1.introduce()
student2.introduce()
student1.introduce_2()
student2.introduce_2()

# Accessing the method through the class does not bind an object.
# Therefore, self must be supplied explicitly in the call below.
Student.introduce(student1)

# In other words, these two calls do the same thing:
student1.introduce()
Student.introduce(student1)

