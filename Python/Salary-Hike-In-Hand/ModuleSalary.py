from ModuleTaxpayer import Taxpayer

class Salary():
    def __init__(self,name,regime,salary) -> None:
        self.name = name
        self.regime = regime
        self.salary = salary

    def getMonthlyInhandSalary(self):
        taxOnSalary = self.getTaxOnSalary(self.name,self.regime,self.salary)
        grossInhandSalary = self.salary/12
        tds = self.getTdsAmount(taxOnSalary)
        netMonthlyInhandSalary = grossInhandSalary - tds
        return tds,netMonthlyInhandSalary

    @staticmethod
    def getTaxOnSalary(name,regime,salary):
        taxpayer = Taxpayer(name,regime,salary)
        return taxpayer.computeTax()

    @staticmethod
    def getTdsAmount(totalTax):
        return totalTax/12  

if __name__ == "__main__":
    s1 = Salary("Ram","new",1250000)
    print(f"{s1.name} {s1.getMonthlyInhandSalary()}")