from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Utilities import CodeForCallbackMove

def choose_cross_or_zero() -> InlineKeyboardMarkup:
    """
    Возвращает кнопки для выбора игры за крестики или нолики
    """
    # markup = InlineKeyboardMarkup()
    X = InlineKeyboardButton("Крестиками", callback_data="Cross")
    O = InlineKeyboardButton("Ноликами", callback_data="Zero")
    return InlineKeyboardMarkup().add(X, O)


def choose_move(name: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    l = (InlineKeyboardButton(str(i), callback_data=str(i)+CodeForCallbackMove.code(name)) for i in range(1, 10))
    for i in range(3):
        markup.add(next(l), next(l), next(l))
    return markup


def not_your_turn() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    l = (InlineKeyboardButton(str(i), callback_data="OpponentTurn") for i in range(1, 10))
    for i in range(3):
        markup.add(next(l), next(l), next(l))
    return markup
