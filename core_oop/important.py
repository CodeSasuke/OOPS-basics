"""Problem and solution prompt for method binding.

Without descriptors, Python would need special-case code to turn a function
stored on a class into a bound method. The descriptor protocol solves this:
``__get__`` receives the instance and returns the correctly bound callable.
See ``__get__.py`` for the runnable final example.
"""

print("WITHOUT DESCRIPTORS")
print("A class would need separate logic to attach self to every method call")
print("\nWITH DESCRIPTORS")
print("__get__ performs that binding automatically")

# A particularly difficult question is:

# If methods are internally functions stored inside a class, what mechanism automatically supplies self when accessed through an object?

# Expected topic: descriptors and bound methods.