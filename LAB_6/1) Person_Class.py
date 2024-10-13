class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# Create two instances of the Person class
person1 = Person("John", 30)
person2 = Person("Jane", 25)

# Print their name and age
print(person1)
print(person2)