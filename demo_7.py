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
        super().__init__(name, salary, self.__department) #? Subclass can get the attributes and methods of superclass using super().
        self.__age = age
    def _showData(self):
        super()._showData()
        print("Age: ", self.__age)
        print("\n")

class Programmer(Employee):
    __department = "Programmer"
    def __init__(self, name, salary, OT, skills):
        super().__init__(name, salary,self.__department)
        self.__OT = OT
        self.__skills = skills
        super()._showData()
    
    def _showData(self):
        super()._showData()
        print("OT: ", self.__OT)
        print("Skills: ", self.__skills)
        print("\n")

class Sales(Employee):
    __department = "Sales"
    def __init__(self, name, salary, commission):
        super().__init__(name, salary, self.__department)
        self.__commission = commission
    
    def _showData(self):
        super()._showData()
        print("Commission: ", self.__commission)
        print("\n")
    
    def _calculateSalary(self):
        return self.__salary + self.__commission


accounting = Accounting("John", 10000, 30)
accounting._showData()

programmer = Programmer("Mary", 20000, 10, ["Python", "JavaScript, Golang"])

sales = Sales("Tom", 30000, 2500)

print(accounting.__str__())
print(programmer.__str__())
print(sales.__str__())

accounting._showData()
programmer._showData()
sales._showData()