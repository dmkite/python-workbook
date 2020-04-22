def make_change(num):
    coin_types = (200, 100, 25, 10, 5, 1)
    coin_dict = {
        200: "Toonies",
        100: "Loonies",
        25: "Quarters",
        10: "Dimes",
        5: "Nickels",
        1: "Pennies"
    }
    change = {}

    for c in coin_types:
        if num >= c:
            num -= c
            coin_type = coin_dict[c]
            if change.get(coin_type):
                change[coin_type] += 1
            else:
                change[coin_type] = 1
        if num == 0:
            break
    
    print(change)

change_to_make = int(input('How many cents? '))
make_change(change_to_make)
            
            
