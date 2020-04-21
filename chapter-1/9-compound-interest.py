def compound_interest(acct_start):
    year_1 = acct_start * 1.04
    year_2 = year_1 * 1.04
    year_3 = year_2 * 1.04
    print(f'''
        Account Balance Projection
        __________________________
        Year 1:\t\t${'%.2f' % year_1}
        Year 2:\t\t${'%.2f' % year_2}
        Year 3:\t\t${'%.2f' % year_3}
        
    ''')
try:
    acct_bal = float(input('What is your account balance? $'))
    compound_interest(acct_bal)
except ValueError:
    print('account balance should be a number')