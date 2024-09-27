def classValidator(func):
    def wrapper(*args):
        
        return func(*args)
    return wrapper

class Taxpayer():
    OLD_TAX_SLABS = [
        (0,250000,0.00),
        (250000,500000,0.05),
        (500000,1000000,0.20),
        (1000000,float("inf"),0.30)
    ]

    NEW_TAX_SLABS = [
        (0,300000,0.00),
        (300000,600000,0.05),
        (600000,900000,0.10),
        (900000,1200000,0.15),
        (1200000,1500000,0.20),
        (1500000,float("inf"),0.30)
    ]

    CESS = 0.04

    def __init__(self,name,regime,income) -> None:
        self.validateInit(name,regime)

        self.name = name
        self.regime = regime
        self.income = income

    def getTaxSlab(self):
        if(self.regime.lower() == "old"):
            self.taxSlab = self.OLD_TAX_SLABS
        else:
            self.taxSlab = self.NEW_TAX_SLABS
        print(self.taxSlab)
    
    def computeTax(self):
        self.grossTax = self.computeGrossTax(self.income,self.taxSlab)
        self.cessAmount = self.computeCessAmount(self.grossTax,self.CESS)
        self.netTax = self.grossTax + self.cessAmount

    @staticmethod
    def computeGrossTax(income,taxSlab):
        grossTax = 0
        for item in taxSlab:
            lowerLimit = item[0]
            upperLimit = item[1]
            taxPercentage = item[2]

            if(income < lowerLimit):
                break
            else:
                if(income > upperLimit):
                    grossTax+=((upperLimit-lowerLimit)*taxPercentage)
                else:
                    grossTax+=((income-lowerLimit)*taxPercentage)

        return grossTax
    
    @staticmethod
    def computeCessAmount(grossTax,cess):
        return grossTax*cess

    @staticmethod
    def validateInit(name,regime):
        if(type(name) is not str):
            raise TypeError("Name should be string")
        if(type(regime) is not str):
            raise TypeError("Regime should be string")
        
        if(regime.lower() == "old" or regime.lower() == "new"):
            pass
        else:
            raise Exception("Regime can either be 'new' or 'old'")
    


if __name__ == "__main__":
    t1 = Taxpayer("User1","new",500000)
    t1.getTaxSlab()
    t1.computeTax()