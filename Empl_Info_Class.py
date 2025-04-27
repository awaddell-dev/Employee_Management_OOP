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
    
Emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")

Emp2 = Employee("Mark Jones", "39119", "IT", "Programmer")

Emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print(f"Employee 1 name: {Emp1.get_name()}\nEmployee 1 ID: {Emp1.get_id_number()}\nEmployee 1 department: {Emp1.get_department()}\nEmployee 1 job title: {Emp1.get_job_title()}")

print(f"Employee 2 name: {Emp2.get_name()}\nEmployee 2 ID: {Emp2.get_id_number()}\nEmployee 2 department: {Emp2.get_department()}\nEmployee 2 job title: {Emp2.get_job_title()}")

print(f"Employee 3 name: {Emp3.get_name()}\nEmployee 3 ID: {Emp3.get_id_number()}\nEmployee 3 department: {Emp3.get_department()}\nEmployee 3 job title: {Emp3.get_job_title()}")