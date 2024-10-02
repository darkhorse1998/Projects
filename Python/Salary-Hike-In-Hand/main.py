from ModuleTaxpayer import Taxpayer
from ModuleValidators import classValidator
from ModuleIncomeHike import SalaryHike
from ModuleCtc import CTC
import math

@classValidator
def initiateSingleTaxpayer(name,regime,income):
    t1 = Taxpayer(name,regime,income)
    computedTax = t1.computeTax()
    print(f"\nTaxpayer details:\nName: {name}\nRegime: {regime}\nIncome: {income}\nNet Tax: {computedTax}")

def salaryHikeAnalysis(name,regime,currentIncome,hikedIncome):
    sh1 = SalaryHike(name,regime,currentIncome,hikedIncome)
    # taxOnCurrentIncome,taxOnHikedIncome,netCurrentIncome,netHikedIncome,diffInIncome,percentageDiffIncome
    parameters = sh1.analyzeHikedIncome()
    print(f"\nTaxpayer details:\nName: {name}{'|':>19} Regime: {regime}\nCurrent Income: {currentIncome} | Hiked Income: {hikedIncome}")
    print(f"Tax on current income: {parameters[0]}\nTax on hiked income: {parameters[1]}")
    print(f"Post Tax current income: {parameters[2]}\nPost tax hiked income: {parameters[3]}")
    print(f"Increase in income(in value): {parameters[4]}\nIncrease in income(in percentage): {parameters[5]:.2f}")

def newJobAnalysis(name,regime,oldCtc,newCtc):
    ctc1 = CTC(name,regime,oldCtc)
    ctc2 = CTC(name,regime,newCtc)
    oldTds,oldEstimatedMonthlySalary = ctc1.getEstimatedMonthlyInhandSalary()
    newTds,newEstimatedMonthlySalary = ctc2.getEstimatedMonthlyInhandSalary()
    increaseInMonthlySalary = newEstimatedMonthlySalary-oldEstimatedMonthlySalary
    increaseInTotalSalary = increaseInMonthlySalary*12
    percentageIncreaseInSalary = ((newEstimatedMonthlySalary/oldEstimatedMonthlySalary)-1)*100
    print(f"\nTaxpayer details:\nName: {name} | Regime: {regime}")
    print(f"Current Estimated Monthly Salary: {math.floor(oldEstimatedMonthlySalary)} | New Estimated Monthly Salary: {math.floor(newEstimatedMonthlySalary)}")
    print(f"Increase in Total Salary: {math.floor(increaseInTotalSalary)} | Increase in Monthly Salary: {math.floor(increaseInMonthlySalary)}")
    print(f"Percentage Increase in Salary: {percentageIncreaseInSalary:.2f}")

if __name__ == "__main__":
    while True:
        operation = input("\nEnter operation:\n"+
                          "1. Salary Hike Analysis\n"+
                          "2. Individual Income Tax Calculation\n"+
                          "3. Job Switch Analysis\n")
        if(operation not in ["q","Q","1","2","3"]):
            print("Invalid operation! Please try again...")
            continue
        if(operation.lower() == "q"):
            break
        name = input("Enter name: ")
        regime = input("Enter regime (new/old): ")

        if (operation == "1"):
            currentIncome = int(input("Enter current income (integer) after all deductons except Standard Deduction: "))
            hikedIncome = int(input("Enter hiked income (integer) after all deductons except Standard Deduction: "))
            salaryHikeAnalysis(name,regime,currentIncome,hikedIncome)
        elif (operation == "2"):
            income = int(input("Enter income (integer) after all deductions except Standard Deduction: "))
            initiateSingleTaxpayer(name,regime,income)
        elif (operation == "3"):
            oldCtc = int(input("Enter previous job's CTC (integer): "))
            newCtc = int(input("Enter new job's CTC (integer): "))
            newJobAnalysis(name,regime,oldCtc,newCtc)
        else:
            print("Invalid operation! Please try again...")