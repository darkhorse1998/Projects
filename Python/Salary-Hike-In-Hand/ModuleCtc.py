from ModuleSalary import Salary

class CTC():

    CTC_FACTOR = 12/14

    def __init__(self,name,regime,ctc) -> None:
        self.name = name
        self.regime = regime
        self.ctc = ctc
    
    def getEstimatedMonthlyInhandSalary(self):
        estimatedGrossSalary = self.computeEstimatedGrossSalary(self.ctc,self.CTC_FACTOR)
        return self.computeMonthlyInhandSalary(self.name,self.regime,estimatedGrossSalary)

    @staticmethod
    def computeMonthlyInhandSalary(name,regime,grossSalary):
        salary = Salary(name,regime,grossSalary)
        return salary.getMonthlyInhandSalary()
    
    @staticmethod
    def computeEstimatedGrossSalary(ctc,ctc_factor):
        return ctc*ctc_factor

if __name__ == "__main__":
    ctc = CTC("Ram","new",1323544)
    print(ctc.getEstimatedMonthlyInhandSalary())