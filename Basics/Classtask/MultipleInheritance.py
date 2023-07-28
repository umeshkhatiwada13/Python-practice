# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Base class 2
class Employee:
    def __init__(self, emp_id, department):
        self.emp_id = emp_id
        self.department = department

    def display_employee_info(self):
        print(f"Employee ID: {self.emp_id}, Department: {self.department}")


# Derived class using multiple inheritance
class Student(Person, Employee):
    def __init__(self, name, age, student_id, major):
        # Call constructors of both base classes
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id=student_id, department=major)

    def display_student_info(self):
        # Call methods of both base classes
        self.display_info()
        self.display_employee_info()


# Create an instance of the Student class and demonstrate multiple inheritance
if __name__ == "__main__":
    student1 = Student("Alice", 20, student_id="12345", major="Computer Science")
    student1.display_student_info()
