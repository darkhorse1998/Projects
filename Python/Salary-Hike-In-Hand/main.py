from modules.Taxpayer import Taxpayer
from modules.Validators import classValidator

@classValidator
def initiateSingleTaxpayer(name,regime,income):
    t1 = Taxpayer(name,regime,income)
    computedTax = t1.computeTax()
    print(f"Taxpayer details:\nName: {name}\nRegime: {regime}\nIncome(post deductions): {income}\nNet Tax: {computedTax}")

if __name__ == "__main__":
    while True:
        name = input("Enter name: ")
        regime = input("Enter regime (new/old): ")
        income = int(input("Enter income (integer) after all deductions: "))

        if(name == "q" or regime == "q" or income == "q"):
            break
        initiateSingleTaxpayer(name,regime,income)