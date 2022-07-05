class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def showData(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Department: ", self.department)

    def __del__(self):
        pass



obj_1 = Employee("John", 10000, "IT")
obj_2 = Employee("Jane", 20000, "HR")
obj_3 = Employee("Jack", 30000, "Sales")

#isinstance is used to check if an object is an instance of a class.
print(isinstance(obj_1, Employee))

#dir is used to get all the attributes and methods of an object.
print(dir(obj_1))#list all attributes and methods of an object.
print(obj_1.showData)#get the method of an object.

#check class of an object.
print(obj_1.__class__)