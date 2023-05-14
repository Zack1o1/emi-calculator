#  The EMI (Equated Monthly Installment) formula is used to 
# calculate the fixed monthly payment that a borrower needs to make towards a loan,
# which includes both the principal amount and the interest. The formula to calculate EMI is as follows:

#  EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)

# Where:
# EMI = Equated Monthly Installment
# P = Principal loan amount
# r = Monthly interest rate (annual interest rate divided by 12 and multiplied by 0.01)
# n = Number of monthly installments

# loan amount
p = float(input('Enter loan amount: '))

# rate
r = float(input('Enter interest rate: '))

# number of installments
n = float(input('Enter tenure in months: '))



def emi_calculator(p,r,n):
    ra = float(r/12/100)
    return (p * ra * pow(1 + ra, n)) / (pow(1 + ra, n) - 1)

   