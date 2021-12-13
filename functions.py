

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