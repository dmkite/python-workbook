from math import *

def distance_calc(pt1, pt2):
    r_pt1 = (radians(pt1[0]), radians(pt1[1]))
    r_pt2 = (radians(pt2[0]), radians(pt2[1]))
    (t1, g1) = r_pt1
    (t2, g2) = r_pt2
    arc_cos_calc = sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2)
    distance = 6371.01 * acos(arc_cos_calc)
    print(f'{distance}km')

# try: 
t1 = int(input('Lat 1: '))
g1 = int(input('Lon 1: '))

t2 = int(input('Lat 2: '))
g2 = int(input('Lon 2: '))

distance_calc((t1,g1), (t1,g2))
# except ValueError:
#     print('coords must be integers')
