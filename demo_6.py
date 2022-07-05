#Class Employee is superclass.
#Class Programmer is subclass of class Employee.

class Employee:

    _min_salary = 10000
    _max_salary = 100000

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department 
    
    def _showData(self):
        print("Name: ", self.getName())
        print("Salary: ", self.getSalary())
        print("Department: ", self.getDepartment())

    def setSalary(self, salary):
        self.__salary = salary
    
    def setDepartment(self, department):
        self.__department = department
    
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department

#----------------------------------------#
class Accounting(Employee):
    def __init__(self):
        pass

class Programmer(Employee):
    pass

class Sales(Employee):
    pass
#----------------------------------------#
#subclass can get the attributes and methods of superclass
accounting = Accounting()
programmer = Programmer()
sales = Sales()

