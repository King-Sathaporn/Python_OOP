from Employee import Employee

class Sale(Employee):
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