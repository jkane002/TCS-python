#!/usr/bin/python
# Doesn't include bonus part
class Employee():
    emp_count = 0
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
    def displayCount(self):
        print("Total employee count is %s " % (emp_count))
    def displayEmployee(self):
        print("Name: ", self.name + "Salary: ", self.salary)
