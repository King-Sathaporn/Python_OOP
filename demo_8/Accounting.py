from Employee import Employee

class Accounting(Employee):
    __department = "Accounting"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__department) #? Subclass can get the attributes and methods of superclass using super().
        self.__age = age
    def _showData(self):
        super()._showData()
        print("Age: ", self.__age)
        print("\n")