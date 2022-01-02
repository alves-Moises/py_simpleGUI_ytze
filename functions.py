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
                'pp':           -1,  # 4 iguais
                '23x':          -1,  # par e trinca
                'es':           -1,  # 1-5 
                'ytz':          -1,  # Yatze! 
                'yy':           -1,   # 11111111111
                '0':            -1
            }
    return comb

def get_score(names):
    info = {}

    for name in names:
        info[name] = comb_func()

    return info