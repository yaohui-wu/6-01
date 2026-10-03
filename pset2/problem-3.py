rate = annualInterestRate / 12.0
low = balance / 12.0
high = (balance*(1+rate)**12) / 12.0
while balance != 0:
    temp = balance
    pay = low + (high-low)/2.0
    for i in range(12):
        temp -= pay
        temp += temp * rate
    if abs(temp) < 0.01:
        balance = 0
    elif temp < -0.01:
        high = pay
    else:
        low = pay
print('Lowest Payment: %.2f' % pay)