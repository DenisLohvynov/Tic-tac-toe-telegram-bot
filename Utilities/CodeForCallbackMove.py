from secrets import choice
from aiogram.utils.deep_linking import decode_payload
from random import choice

def code(name: str) -> str:
    """
    Кодирует имя перед записью в кнопку
    """
    code = ""
    for i in range(3):
        temp = name[3*i:i*3+3]
        if temp=="NNN":
            code+="0"
        elif temp=="NNO":
            code+="1"
        elif temp=="NNX":
            code+="2"
        elif temp=="NON":
            code+="3"
        elif temp=="NOO":
            code+="4"
        elif temp=="NOX":
            code+="5"
        elif temp=="NXN":
            code+="6"
        elif temp=="NXO":
            code+="7"
        elif temp=="NXX":
            code+="8"
        # __________________
        elif temp=="ONN":
            code+="q"
        elif temp=="ONO":
            code+="w"
        elif temp=="ONX":
            code+="e"
        elif temp=="OON":
            code+="r"
        elif temp=="OOO":
            code+="t"
        elif temp=="OOX":
            code+="y"
        elif temp=="OXN":
            code+="u"
        elif temp=="OXO":
            code+="i"
        elif temp=="OXX":
            code+="o"
        # __________________
        elif temp=="XNN":
            code+="a"
        elif temp=="XNO":
            code+="s"
        elif temp=="XNX":
            code+="d"
        elif temp=="XON":
            code+="f"
        elif temp=="XOO":
            code+="g"
        elif temp=="XOX":
            code+="h"
        elif temp=="XXN":
            code+="j"
        elif temp=="XXO":
            code+="k"
        elif temp=="XXX":
            code+="l"
    return code


def decode(code: str) -> str:
    """
    декодирует имя полученное от кнопки
    """
    name = ""
    for i in code:
        if i=="0":
            name+="NNN"
        elif i=="1":
            name+="NNO"
        elif i=="2":
            name+="NNX"
        elif i=="3":
            name+="NON"
        elif i=="4":
            name+="NOO"
        elif i=="5":
            name+="NOX"
        elif i=="6":
            name+="NXN"
        elif i=="7":
            name+="NXO"
        elif i=="8":
            name+="NXX"
        # __________________
        elif i=="q":
            name+="ONN"
        elif i=="w":
            name+="ONO"
        elif i=="e":
            name+="ONX"
        elif i=="r":
            name+="OON"
        elif i=="t":
            name+="OOO"
        elif i=="y":
            name+="OOX"
        elif i=="u":
            name+="OXN"
        elif i=="i":
            name+="OXO"
        elif i=="o":
            name+="OXX"
        # __________________
        elif i=="a":
            name+="XNN"
        elif i=="s":
            name+="XNO"
        elif i=="d":
            name+="XNX"
        elif i=="f":
            name+="XON"
        elif i=="g":
            name+="XOO"
        elif i=="h":
            name+="XOX"
        elif i=="j":
            name+="XXN"
        elif i=="k":
            name+="XXO"
        elif i=="l":
            name+="XXX"
    return name


def decode_greetings_2_0(args: str, id_O_X: str) -> tuple:
    payload = decode_payload(args)
    X_O = payload[0] if payload[0]!='?' else choice(('X', 'O'))
    id_X_O, inline_id = payload[1:].split(' ') # id first, plays X_O
    id_X = id_X_O if X_O=='X' else id_O_X
    id_O = id_X_O if X_O=='O' else id_O_X
    return id_X, id_O, inline_id


def decode_data_from_markup(keyboards: list, i: int = 1) -> dict:
    """
    i = 1 - your turn
    i = 6 - not your turn
    returns dictionary with such keys (name, id_X, id_O, message_id_X, message_id_O, inline_id)
    """
    name = keyboards[0][0]["callback_data"][i:]
    id_X = keyboards[0][1]["callback_data"][i:]
    id_O = keyboards[0][2]["callback_data"][i:]
    message_id_X = keyboards[1][0]["callback_data"][i:]
    message_id_O = keyboards[1][1]["callback_data"][i:]
    inline_id = keyboards[1][2]["callback_data"][i:]
    return {
        'name': name,
        'id_X': id_X,
        'message_id_X': message_id_X,
        'id_O': id_O,
        'message_id_O': message_id_O,
        'inline_id': inline_id
        }

