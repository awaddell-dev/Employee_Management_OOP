Employee Management OOP

Overview

This project demonstrates the use of Object-Oriented Programming (OOP) concepts in Python through the creation of an Employee class. The Employee class encapsulates the attributes and behaviors of an employee, including their name, ID number, department, and job title. It allows for setting and getting these attributes using getter and setter methods.

Features
Encapsulation: Employee attributes are private and can only be accessed or modified through getter and setter methods.

Object-Oriented Design: The project demonstrates the creation and usage of Python classes and objects.

Flexible Employee Information Management: Allows adding and updating employee information easily.


Code Example -

class Employee:

    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def set_name(self, new_name):
        self.__name = new_name

    def set_id_number(self, new_id_number):
        self.__id_number = new_id_number

    def set_department(self, new_department):
        self.__department = new_department

    def set_job_title(self, new_job_title):
        self.__job_title = new_job_title

# Creating Employee instances
Emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
Emp2 = Employee("Mark Jones", "39119", "IT", "Programmer")
Emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Display employee information

print(f"Employee 1 name: {Emp1.get_name()}\nEmployee 1 ID: {Emp1.get_id_number()}\nEmployee 1 department: {Emp1.get_department()}\nEmployee 1 job title: {Emp1.get_job_title()}")

print(f"Employee 2 name: {Emp2.get_name()}\nEmployee 2 ID: {Emp2.get_id_number()}\nEmployee 2 department: {Emp2.get_department()}\nEmployee 2 job title: {Emp2.get_job_title()}")

print(f"Employee 3 name: {Emp3.get_name()}\nEmployee 3 ID: {Emp3.get_id_number()}\nEmployee 3 department: {Emp3.get_department()}\nEmployee 3 job title: {Emp3.get_job_title()}")

How to Use:
Clone or download the repository to your local machine.

Run the Empl_Info_Class.py file to see the example of employee management using OOP.

Modify the employee details or create new employees by instantiating the Employee class.

File Structure:

Empl_Info_Class.py: Main Python file containing the Employee class and a demonstration of employee data management.

Requirements: 
Python 3.x

License: 
This project is open-source and available under the MIT License.

