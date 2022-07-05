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