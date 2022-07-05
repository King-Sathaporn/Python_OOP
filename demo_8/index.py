from Accounting import Accounting
from Programmer import Programmer
from Sale import Sale


accounting = Accounting("John", 10000, 30)
programmer = Programmer("Mary", 20000, 10, ["Python", "JavaScript, Golang"])
sales = Sale("Tom", 30000, 2500)

accounting._showData()
programmer._showData()
sales._showData()