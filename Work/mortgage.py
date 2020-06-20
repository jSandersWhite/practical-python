# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
totalPaid = 0.0
paymentCount = 0
extraPaymentStartMonth = int(input('Input month to start extra payments: '))
extraPaymentEndMonth = int(input('Input month to end extra pamyents: '))
extraPaymentAmount = int(input('Extra payment amount: '))

while principal > 0:
    paymentCount = paymentCount + 1
    if (principal < payment):
        payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - payment
    totalPaid = totalPaid + payment

    if paymentCount > extraPaymentStartMonth and paymentCount <= extraPaymentEndMonth:
        principal = principal - extraPaymentAmount
        totalPaid = totalPaid + extraPaymentAmount
    
    print(paymentCount, round(totalPaid, 2), round(principal, 2))

print('Total Paid:', round(totalPaid, 2), 'Months:', paymentCount)