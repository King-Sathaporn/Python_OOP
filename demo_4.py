#Access Modifier
#() Public: can be accessed from anywhere
#(_) Private: can only be accessed from the class
#(__) Protected: can only be accessed from the class and its subclasses

class Employee:
    def __init__(self, name, salary, department):
        self._name = name #_name is a private attribute
        self.__salary = salary #__salary is a protected attribute
        self.__department = department  #__department is a protected attribute
    
    def _showData(self):
        '''
        print("Name: ", self._name)
        print("Salary: ", self.__salary)
        print("Department: ", self.__department)
        '''
        print("Name: ", self._name)
        print("Salary: ", self.getSalary())
        print("Department: ", self.getDepartment())

    #Create setter method for set the value of private attribute
    def setSalary(self, salary):
        self.__salary = salary
    
    def setDepartment(self, department):
        self.__department = department
    
    def getDepartment(self):
        return self.__department
    
    #Create getter method for get the value of private attribute
    def getSalary(self):
        return self.__salary

obj_1 = Employee("John", 10000, "IT")
obj_1._showData()

#? We can't access the private attribute with out the underscore(_).
obj_1.name = "Jane"
obj_1.salary = 20000
obj_1.department = "HR"
obj_1._showData()

#? We can access the private attribute with the underscore(_), but can't access the protected attribute with the double underscore(__).
obj_1._name = "Jane"
obj_1.__salary = 20000
obj_1.__department = "HR"
obj_1._showData()

obj_1.setSalary(30000)
obj_1.setDepartment("Sales")
obj_1._showData()

salary = obj_1.getSalary()
print("Object 1 salary: ", salary)
obj_1._showData()