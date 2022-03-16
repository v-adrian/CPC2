# Testing Employee.py

from Employee import *

employee = Employee("John Smith", 45000)
manager = Manager("Jane Doe", 60000, "Widgets")
executive = Executive("Weird Guy", 90000, "Thingies")

print(repr(employee))
print(repr(manager))
print(repr(executive))
