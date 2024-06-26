import copy
from copy import deepcopy


class Address:
    def __init__(self, street, city, suite, country):
        self.street = street
        self.city = city
        self.suite = suite
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, #{self.suite}, {self.country}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("#123", "London", 0, "UK"))
    aux_office_employee = Employee("", Address("#123B", "London", 0, "UK"))

    @staticmethod
    def __new_employee(prototype: Employee, name, suite):
        emp = copy.deepcopy(prototype)
        emp.name = name
        emp.address.suite = suite
        return emp

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


john = EmployeeFactory.new_main_office_employee("John", 501)
jane = EmployeeFactory.new_aux_office_employee("Jane", 200)

print(john)
print(jane)
