def dices_ico():
    dices = {
        1: 'assets/ico/D1-ico.png', 
        2: 'assets/ico/D2-ico.png', 
        3: 'assets/ico/D3-ico.png', 
        4: 'assets/ico/D4-ico.png', 
        5: 'assets/ico/D5-ico.png', 
        6: 'assets/ico/D6-ico.png'
    }
    return dices

def comb_func():
    comb = {
                '1':            -1,
                '2':            -1,
                '3':            -1,
                '4':            -1,
                '5':            -1,
                '6':            -1,
                '3x':           -1,  # 3 of a kind
                '4x':           -1,  #  4 of a kind
                'FHouse':       -1,  # Full House  (2 of a kind and 3 of a kind)
                'small':        -1,  # Small Straight 
                'large':        -1,  # 11111111111
                'yy':           -1,  # Yatzee!
                'chance':       -1
            }
    return comb

def get_score(names):
    info = dict()

    for name in names:
        info[name] = comb_func()

    return info