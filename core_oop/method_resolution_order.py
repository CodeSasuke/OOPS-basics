"""Notes and examples for Python's Method Resolution Order (MRO).

MRO is the order Python follows when looking for a method or attribute in
an inheritance hierarchy. It is especially important with multiple
inheritance because more than one parent may define the same method.

Without MRO, multiple inheritance could not decide which ``show`` method to
run. Python's lookup order and ``super()`` provide one predictable path.
"""


class Animal:
	def speak(self):
		print("Animal speaks")


class Dog(Animal):
	def speak(self):
		print("Dog barks")


dog = Dog()
print("Without MRO, Dog.speak() would be ambiguous between Dog and Animal")
dog.speak()  # Dog is checked before Animal.
print(Dog.mro())


class A:
	def show(self):
		print("A")


class B(A):
	def show(self):
		print("B")
		super().show()


class C(A):
	def show(self):
		print("C")
		super().show()


class D(B, C):
	def show(self):
		print("D")
		super().show()


value = D()
value.show()
print(D.mro())

# The lookup order is D -> B -> C -> A -> object.
# super() follows this MRO, so each implementation runs once.