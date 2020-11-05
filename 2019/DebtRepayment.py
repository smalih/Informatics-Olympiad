import math
from decimal import *


# Need to refine, output should be 116.55, not 116.58

variables = input()

interest, repayment = variables.split(" ")

debt = 100
amount_repaid = 0
interest = Decimal((int(interest)/100) + 1)
repayment = Decimal(int(repayment)/100)


while debt!= 0:
    debt = Decimal(debt*interest).quantize(Decimal('.01'), rounding=ROUND_UP)
    dr = Decimal(debt * repayment).quantize(Decimal('.01'), rounding=ROUND_UP)

    if dr < 50:
        if debt>= 50:
            amount_repaid+=50
            debt-=50
        else:
            amount_repaid+=debt
            debt-=debt

    else:
        if (dr) > debt:
            amount_repaid += debt
            debt -= debt
        else:
            amount_repaid += dr
            debt-= dr
print(amount_repaid)

print("\nSolomon Malih - Colchester Royal Grammar School")
