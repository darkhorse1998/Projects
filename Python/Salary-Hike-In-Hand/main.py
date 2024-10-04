from ModuleTaxpayer import Taxpayer
from ModuleValidators import classValidator
from ModuleIncomeHike import SalaryHike
from ModuleCtc import CTC
from tabulate import tabulate

@classValidator
def initiateSingleTaxpayer(name,regime,income):
    t1 = Taxpayer(name,regime,income)
    computedTax = t1.computeTax()
    print(f"\nTaxpayer details:\nName: {name}\nRegime: {regime}\nIncome: {income}\nNet Tax: INR {computedTax}")

def salaryHikeAnalysis(name,regime,currentIncome,hikedIncome):
    sh1 = SalaryHike(name,regime,currentIncome,hikedIncome)
    parameters = sh1.analyzeHikedIncome()
    print(f"\nTaxpayer details:\nName: {name}{'|':>19} Regime: {regime}\nCurrent Income: {currentIncome} | Hiked Income: {hikedIncome}")
    print(f"Tax on current income: INR {parameters[0]}\nTax on hiked income: INR {parameters[1]}")
    print(f"Post Tax current income: INR {parameters[2]}\nPost tax hiked income: INR {parameters[3]}")
    print(f"Increase in income(in value): INR {parameters[4]}\nIncrease in income(in percentage): {parameters[5]:.2f}%")

def newJobAnalysis(name,regime,oldCtc,newCtc):
    ctc1 = CTC(name,regime,oldCtc)
    ctc2 = CTC(name,regime,newCtc)
    oldTds,oldEstimatedMonthlySalary = ctc1.getEstimatedMonthlyInhandSalary()
    newTds,newEstimatedMonthlySalary = ctc2.getEstimatedMonthlyInhandSalary()
    increaseInMonthlySalary = newEstimatedMonthlySalary-oldEstimatedMonthlySalary
    increaseInTotalSalary = increaseInMonthlySalary*12
    percentageIncreaseInSalary = ((newEstimatedMonthlySalary/oldEstimatedMonthlySalary)-1)*100
    output = [
        ["Name:",name,"Regime:",regime],
        ["Current Estimated Monthly Salary:",f"INR {oldEstimatedMonthlySalary:.2f}","New Estimated Monthly Salary:",f"INR {newEstimatedMonthlySalary:.2f}"],
        ["Current TDS:",f"{oldTds:.2f}","New TDS:",f"{newTds:.2f}"],
        ["Increase in Total Salary:",f"INR {increaseInTotalSalary:.2f}","Increase in Monthly Salary:",f"INR {increaseInMonthlySalary:.2f}"],
        ["Percentage Increase in Salary:",f"INR {percentageIncreaseInSalary:.2f}%"]
    ]
    print(tabulate(output))

if __name__ == "__main__":
    while True:
        operation = input("\nEnter operation:\n"+
                          "1. Salary Hike Analysis\n"+
                          "2. Individual Income Tax Calculation\n"+
                          "3. Job Switch Analysis\n")
        validOperations = ["q","Q"]+[str(x) for x in range(1,4)]
        if(operation not in validOperations):
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