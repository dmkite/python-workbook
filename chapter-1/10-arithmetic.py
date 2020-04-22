import math

def arithmetic(a, b):
    print(f'sum: {a + b}')
    print(f'difference: {a - b}')
    print(f'product: {a * b}')
    print(f'quotient: {a / b}')
    print(f'log 10: {math.log10(a)}')
    print(f'a^b: {a ** b}')


try:
    a = int(input('Provide a value for \'a\': '))
    b = int(input('Provide a value for \'b\': '))
    arithmetic(a, b)
except ValueError:
    print('a and b must be integers')