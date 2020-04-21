def compute_weight(widget_ct, gizmo_ct):
    print(f'{widget_ct * 75 + gizmo_ct * 112}g') 
try:
    w_ct = int(input('How many widgets are in your order?\n'))
    g_ct = int(input('How many gizmos are in your order?\n'))
    compute_weight(w_ct, g_ct)
except ValueError:
    print('I need a number.')
    