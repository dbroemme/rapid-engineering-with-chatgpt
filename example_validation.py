class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.name = name
        self.age = age
