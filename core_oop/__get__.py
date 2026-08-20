"""Live explanation of ``__get__`` and method binding.

Run this file from the repository root with:

	python3 core_oop/__get__.py

The important observation is that accessing a function through an object is
not the same as accessing it through the class. The descriptor protocol makes
that difference possible.
"""


class MethodDescriptor:
	"""A small descriptor that binds an object to a function."""

	def __init__(self, function):
		self.function = function

	def __get__(self, instance, owner):
		"""Choose class access or instance access."""
		if instance is None:
			print(f"__get__: accessed through {owner.__name__}")
			return self.function

		print(f"__get__: accessed through {owner.__name__} instance")

		def bound_method(*args, **kwargs):
			return self.function(instance, *args, **kwargs)

		return bound_method


class Greeter:
	def greet(self, message):
		return f"{self.name} says: {message}"

	def __init__(self, name):
		self.name = name

	# Store the function inside a descriptor so __get__ controls access.
	greet = MethodDescriptor(greet)  # type: ignore[assignment]


def normal_binding_example():
	"""Show the problem: class and instance calls need different forms."""
	greeter = Greeter("Asha")

	print("Without a custom descriptor, the caller must understand both forms:")
	print(greeter.greet("Hello"))
	print(Greeter.greet(greeter, "Hello again"))


def descriptor_example():
	"""Show the solution: ``__get__`` controls both access forms."""
	greeter = Greeter("Ravi")

	print("\nDescriptor behavior:")
	class_access = Greeter.greet
	print(f"Class access returns: {type(class_access).__name__}")
	print(class_access(greeter, "Class call"))

	instance_access = greeter.greet
	print(f"Instance access returns: {type(instance_access).__name__}")
	print(instance_access("Instance call"))


def main():
	print("Without __get__, a function would not adapt to class access")
	normal_binding_example()
	descriptor_example()


if __name__ == "__main__":
	main()