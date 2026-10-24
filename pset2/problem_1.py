monthly_rate = annualInterestRate / 12.0
for i in range(12):
    min_monthly_pay = monthlyPaymentRate * balance
    balance -= min_monthly_pay
    balance += balance * monthly_rate
print('Remaining balance: %.2f' % balance)