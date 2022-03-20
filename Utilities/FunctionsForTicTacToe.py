from random import randint, choice
from .types_X_O import ResultOfGame


def __determine_X_or_O(name: str) -> str:
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


def get_new_name(name: str, t: int, X: str|None = None) -> str:
    if X==None:
        return name[:t] + __determine_X_or_O(name) + name[t+1:]
    return name[:t] + X + name[t+1:]


def get_random(name: str, what: str = 'N') -> int:
    """
    Вернет имя с кодом
    """
    if not what in ('X', 'O'):
        what = __determine_X_or_O(name)
    l = [i for i in range(9) if name[i]=="N"]
    t = choice(l)
    return name[:t]+what+name[t+1:]


def if_end(name: str) -> ResultOfGame:    
    if (name[0]==name[1]==name[2] and name[0]!='N') or (name[3]==name[4]==name[5] and name[3]!='N') or (name[6]==name[7]==name[8] and name[6]!='N') or (name[0]==name[3]==name[6] and name[3]!='N') or (name[1]==name[4]==name[7] and name[4]!='N') or (name[2]==name[5]==name[8] and name[2]!='N') or (name[0]==name[4]==name[8] and name[0]!='N') or (name[2]==name[4]==name[6] and name[4]!='N'):
        return ResultOfGame.WIN
    E = 0
    for i in name:
        if i in ('X', 'O'):
            E+=1
    if E == 9:
        return ResultOfGame.DRAW
    return ResultOfGame.CONTINUE
