"""``cls`` and ``@classmethod``: the problem with hard-coded classes.

Without ``cls``, alternate constructors would need to name ``Student``
directly and would return the wrong type for subclasses. A class method gets
the receiving class automatically, so the solution remains reusable.
"""


class Student:
	school = "Dhanushya Prep"
	student_count = 0

	def __init__(self, name: str, course: str):
		self.name = name
		self.course = course
		Student.student_count += 1

	def describe(self):
		"""An instance method receives the object as ``self``."""
		return f"{self.name} studies {self.course} at {self.school}."

	@classmethod
	def from_text(cls, text: str):
		"""Create a student from the class's alternate input format."""
		name, course = text.split(",")
		return cls(name.strip(), course.strip())

	@classmethod
	def change_school(cls, new_school: str):
		"""Change data shared by every student of this class."""
		cls.school = new_school

	@classmethod
	def total_students(cls):
		return cls.student_count


class OnlineStudent(Student):
	"""A subclass proves why ``cls`` is better than hard-coding ``Student``."""

	pass


def hard_coded_factory(text: str):
	name, course = text.split(",")
	return Student(name.strip(), course.strip())


def main():
	print("WITHOUT CLS")
	hard_coded = hard_coded_factory("Mina, Data Structures")
	print(f"Hard-coded factory returned: {type(hard_coded).__name__}")

	print("\nWITH CLS")
	first = Student("Asha", "Python")
	second = Student.from_text("Ravi, Object-Oriented Programming")

	print(first.describe())
	print(second.describe())
	print(f"Created students: {Student.total_students()}")

	Student.change_school("Dhanushya Advanced Prep")
	print(f"Shared school after change: {first.school}")

	online = OnlineStudent.from_text("Mina, Data Structures")
	print(f"Factory returned: {type(online).__name__}")
	print(online.describe())


if __name__ == "__main__":
	main()