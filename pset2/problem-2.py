monthly_rate = annualInterestRate / 12.0
monthly_pay = 10
while balance > 0:
    temp = balance
    for i in range(12):
        temp -= monthly_pay
        temp += temp * monthly_rate
    if temp <= 0:
        balance = 0
    else:
        monthly_pay += 10
print('Lowest Payment:', monthly_pay)