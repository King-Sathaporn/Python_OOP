#create a class
class Employee:
    #create method
    def detail(self, name, salary, department):
        #create Attributes
        self.name = name
        self.salary = salary
        self.department = department
    
    def showData(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Department: ", self.department)

#create an object
obj_1 = Employee()
#call method
obj_1.detail("John", 10000, "IT")
obj_1.showData()

obj_2 = Employee()
obj_2.detail("Jane", 20000, "HR")
obj_2.showData()

obj_3 = Employee()
obj_3.detail("Jack", 30000, "Sales")
obj_3.showData()