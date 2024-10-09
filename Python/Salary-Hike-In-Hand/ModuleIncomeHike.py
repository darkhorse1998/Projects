from ModuleTaxpayer import Taxpayer

class SalaryHike(Taxpayer):
    def __init__(self,name,regime,currentIncome,hikedIncome):
        self.name = name
        self.regime = regime
        self.currentIncome = currentIncome
        self.hikedIncome = hikedIncome
    
    def analyzeHikedIncome(self):
        taxOnCurrentIncome = self.getIncomeTax(self.name,self.regime,self.currentIncome)
        taxOnHikedIncome = self.getIncomeTax(self.name,self.regime,self.hikedIncome)
        netCurrentIncome = self.currentIncome - taxOnCurrentIncome
        netHikedIncome = self.hikedIncome - taxOnHikedIncome
        diffInIncome = netHikedIncome - netCurrentIncome
        percentageDiffIncome = (diffInIncome/netCurrentIncome)*100

        self.netCurrentIncome = netCurrentIncome
        self.netHikedIncome = netHikedIncome
        return taxOnCurrentIncome,taxOnHikedIncome,netCurrentIncome,netHikedIncome,diffInIncome,percentageDiffIncome

    @staticmethod
    def getIncomeTax(name,regime,income):
        taxpayer = Taxpayer(name,regime,income)
        return taxpayer.computeTax()
    
if __name__ == "__main__":
    sh1 = SalaryHike("Ram","new",1250000,2000000)
    response = sh1.analyzeHikedIncome()
    print(response)