class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Create objects to represent different students
student1 = Student("John", 20)
student2 = Student("Alice", 22)
student3 = Student("Bob", 21)

# Print the student details
print(student1)
print(student2)
print(student3)