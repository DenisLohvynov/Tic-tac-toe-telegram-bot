from random import randint


def __determine_X_or_O(name: str):
    """
    По имени доски выдает чем ходит игрок
    """
    X = 0
    O = 0
    for i in name:
        if i=="X":
            X+=1
        elif i=="O":
            O+=1
    if X==O:
        return "X"
    return "O"

def get_new_name(name: str, t: int) -> str:
    return name[:t] + __determine_X_or_O(name) + name[t+1:]


def get_random(name: str, what: str = 'N') -> int:
    """
    Вернет имя с кодом
    """
    if not what in ('X', 'O'):
        what = __determine_X_or_O(name)
    l = [i for i in range(9) if name[i]=="N"]
    s = len(l)
    t = l[randint(0, s-1)]
    return name[:t]+what+name[t+1:]


def if_end(name: str) -> int:
    """
    0 - еще не конец

    1 - победа или поражение

    2 - ничья 
    """
    E = 0
    for i in name:
        if i in ('X', 'O'):
            E+=1
    if E == 9:
        return 2
    
    if (name[0]==name[1]==name[2] and name[0]!='N') or (name[3]==name[4]==name[5] and name[3]!='N') or (name[6]==name[7]==name[8] and name[6]!='N') or (name[0]==name[3]==name[6] and name[3]!='N') or (name[1]==name[4]==name[7] and name[4]!='N') or (name[2]==name[5]==name[8] and name[2]!='N') or (name[0]==name[4]==name[8] and name[0]!='N') or (name[2]==name[4]==name[6] and name[4]!='N'):
        return 1
    return 0
