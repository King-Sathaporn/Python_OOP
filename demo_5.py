class Employee:
    def __init__(self, name, salary, department):
        #instance variable
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
    
    #class variable, Class variable is shared by all the instances of the class.
    _min_salary = 10000
    _max_salary = 100000

obj_1 = Employee("John", 20000, "IT")
obj_1._showData()
print("Min salary: ", Employee._min_salary)