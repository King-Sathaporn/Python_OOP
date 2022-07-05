class Employee:
    #create constructor, constructor is a method that is called when an object is created.
    #If you don't create a constructor, Python will create a default constructor.
    def __init__(self, name, salary, department):
        print("Employee object created")
        self.name = name
        self.salary = salary
        self.department = department
    
    def showData(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
    
    #create destructor, destructor is a method that is called when an object is deleted for restoring the memory.
    #If you don't create a destructor, Python will create a default destructor.
    def __del__(self):
        print("Employee object deleted")



obj_1 = Employee("John", 10000, "IT")
obj_1.showData()
obj_2 = Employee("Jane", 20000, "HR")
obj_2.showData()
obj_3 = Employee("Jack", 30000, "Sales")
obj_3.showData()