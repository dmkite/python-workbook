def mpg_to_lp100k(mpg):
    kms = mile_to_km(mpg, 'km')
    liters = liter_to_gal(1, 'l')
    l_per_100km = liters * 100 / kms
    print(f'{round(l_per_100km,1) } L/100k')
    
def mile_to_km(val, desired_unit):
    if desired_unit != 'km' and desired_unit != 'mi':
        raise ValueError('Unit must be "km" or "mi"')
    try:
        return float(val) * 0.621371 if desired_unit is 'km' else float(val) * 1.60934
    except ValueError:
        raise ValueError('value must be an integer or float')

def liter_to_gal(val, desired_unit):
    if desired_unit != 'l' and desired_unit != 'g':
        raise ValueError('Unit must be "l" or "g"')
    try:
        return val * 0.264172 if desired_unit is 'g' else val * 3.78541
    except ValueError:
        raise ValueError('value must be an integer or float')


mpg = input("What is the mpg? ")
mpg_to_lp100k(mpg)
