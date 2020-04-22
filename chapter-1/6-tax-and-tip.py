cost = float(input('How much did your meal cost?\n'))
rounded_cost = '%.2f' % cost
tax = cost * .075
rounded_tax = '%.2f' % tax
tip = cost * .18
rounded_tip = '%.2f' % tip
total = '%.2f' % (cost + tax + tip)

print(f'Meal:\t${rounded_cost}\nTax:\t${rounded_tax}\nTip:\t${rounded_tip}\nTotal:\t${total}')