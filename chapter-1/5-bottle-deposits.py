less_than_liter = int(input('How many bottles do you have that are smaller than 1L?\n'))
greater_than_liter = int(input('How many bottles do you have that are bigger than 1L?\n'))

sum = float(((less_than_liter * 10) + (greater_than_liter * 25)) / 100)

print(f'Your refund is ${round(sum, 2)}.')