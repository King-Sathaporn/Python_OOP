from Employee import Employee

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