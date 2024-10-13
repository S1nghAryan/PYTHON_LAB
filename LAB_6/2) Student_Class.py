class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}"

# Create an instance of the Student class
student = Student("John", 2)

# Print the student's details
print(student)