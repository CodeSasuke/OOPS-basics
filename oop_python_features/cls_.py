"""Live examples of ``cls`` and ``@classmethod`` in Python."""


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


def main():
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