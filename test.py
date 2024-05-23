class Person:
    def __init__(self, name, age):
        self._protected_attribute = 'This is a protected attribute.'
        self.name = name
        self.age = age


class Employee(Person):
    def display_protected_attribute(self):
        print(self._protected_attribute)


employee = Employee('Jane Doe', 25)
employee.display_protected_attribute()  # This is a protected attribute.
print(employee._protected_attribute)    # This is a protected attribute.