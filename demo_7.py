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

    #create function calculate salary per year
    def _getIncome(self):
        return self.__salary * 12
    
    def __str__(self) -> str:
        return (f"Name: {self.__name}, Salary: {self.__salary}, Department: {self.__department}, Salary per year: {self._getIncome()}")

class Accounting(Employee):
    __department = "Accounting"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, age, self.__department) #? Subclass can get the attributes and methods of superclass using super().

class Programmer(Employee):
    __department = "Programmer"
    def __init__(self, name, salary, OT):
        super().__init__(name, salary, OT,self.__department)
        super()._showData()

class Sales(Employee):
    __department = "Sales"
    def __init__(self, name, salary, commission):
        super().__init__(name, salary, commission, self.__department)
        print("Sales's salary per year: ", super()._getIncome())

accounting = Accounting("John", 10000)
accounting._showData()

programmer = Programmer("Mary", 20000)

sales = Sales("Tom", 30000)

print(accounting.__str__())
print(programmer.__str__())
print(sales.__str__())