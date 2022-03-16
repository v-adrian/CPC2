class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def __repr__(self):
        return "{} has a salary of {:.02f}".format(self._name, self._salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return "{} has a salary of {:.02f} and manages the {} department".format(self._name, self._salary, self._department)


class Executive(Manager):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)
    
    def __repr__(self):
        return "{} has a salary of {:.02f} and is the executive for the {} department".format(self._name, self._salary, self._department)
