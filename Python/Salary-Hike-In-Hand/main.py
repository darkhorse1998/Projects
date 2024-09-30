from ModuleTaxpayer import Taxpayer
from ModuleValidators import classValidator
from ModuleIncomeHike import SalaryHike

@classValidator
def initiateSingleTaxpayer(name,regime,income):
    t1 = Taxpayer(name,regime,income)
    computedTax = t1.computeTax()
    print(f"Taxpayer details:\nName: {name}\nRegime: {regime}\nIncome(post deductions): {income}\nNet Tax: {computedTax}")

def salaryHikeAnalysis(name,regime,currentIncome,hikedIncome):
    sh1 = SalaryHike(name,regime,currentIncome,hikedIncome)
    # taxOnCurrentIncome,taxOnHikedIncome,netCurrentIncome,netHikedIncome,diffInIncome,percentageDiffIncome
    parameters = sh1.analyzeHikedIncome()
    print(f"Taxpayer details:\nName: {name}{'|':>19} Regime: {regime}\nCurrent Income: {currentIncome} | Hiked Income: {hikedIncome}")
    print(f"Tax on current income: {parameters[0]}\nTax on hiked income: {parameters[1]}")
    print(f"Post Tax current income: {parameters[2]}\nPost tax hiked income: {parameters[3]}")
    print(f"Increase in income(in value): {parameters[4]}\nIncrease in income(in percentage): {parameters[5]:.2f}")

if __name__ == "__main__":
    while True:
        operation = input("\nEnter operation:\n"+
                          "1. Salary Hike Analysis\n"+
                          "2. Individual Income Tax Calculation\n")
        if(operation.lower() == "q"):
            break
        name = input("Enter name: ")
        regime = input("Enter regime (new/old): ")

        if (operation == "1"):
            currentIncome = int(input("Enter current income (integer) after all deductons: "))
            hikedIncome = int(input("Enter hiked income (integer) after all deductons: "))
            salaryHikeAnalysis(name,regime,currentIncome,hikedIncome)
        elif (operation == "2"):
            income = int(input("Enter income (integer) after all deductions: "))
            initiateSingleTaxpayer(name,regime,income)