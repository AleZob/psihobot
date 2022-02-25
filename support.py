from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup

#создаёт клавиатуру во всём боте 6 - вопросы
def get_keyboard(what):
    width = 2
    if what == 1:#копки главного меню
        buttons = [
            types.InlineKeyboardButton(text="Релаксация", callback_data="do_first"),
            types.InlineKeyboardButton(text="Медитация-настройки", callback_data="do_second"),
            types.InlineKeyboardButton(text="Заземление", callback_data="do_third"),
            types.InlineKeyboardButton(text="Эмоции и факты",
                                       callback_data="do_fourth"),
        ]
    elif what == 2:#если нажато релаксация
        buttons = [
            types.InlineKeyboardButton(text="Посредством микродвижений", url="https://youtu.be/DkuU5nmcXfo"),
            types.InlineKeyboardButton(text="Активная релаксация", url="https://youtu.be/yIQIy_uQ6Qk"),
            types.InlineKeyboardButton(text="Назад", callback_data="do_back"),
        ]
    elif what == 3:#если нажато Медитация
        buttons = [types.InlineKeyboardButton(text="Назад!", callback_data="do_back")]
        width = 1
    elif what == 4:#если нажато Заземление
        buttons = [types.InlineKeyboardButton(text="Да!", callback_data="do_start-four"),
                   types.InlineKeyboardButton(text="Назад!", callback_data="do_back")
                   ]
        width = 1
    elif what == 5:#если нажато Ции...
        buttons = [types.InlineKeyboardButton(text="Да!", callback_data="do_start-five"),
                   types.InlineKeyboardButton(text="Назад!", callback_data="do_back")
                   ]
        width = 1
    elif what == 6:#Вариант кнопок для вопросов
        buttons = [types.InlineKeyboardButton(text="Далее!", callback_data="no_next"),
                   #types.InlineKeyboardButton(text="Отмена!", callback_data="no_back")
                   ]
        width = 1
    keyboard = types.InlineKeyboardMarkup(row_width=width, resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard

#список вопросов для заземления
Third = {
    "first":  "СТОП! Остановитесь на мгновение! \n"
              "Сделайте вдох и медленно выдохните.\n"
              "Отметьте, как вы дышите, свободно и расслабленно или зажато?\n"
              "Каким ощущается тело - живот, грудная клетка, спина? Лицо?",
    "second" :  "Назовите 5 предметов, вас окружающих",
    "third" :  "Найдите 4 звука",
    "fourth" :  "3 тактильных ощущения\n"
               "(почва под ногами, прикосновение одежды, касание ветра и т. д.) ",
    "fifth" :  "2 запаха (можно даже что-то специально понюхать! )",
    "sixth" :  "1 вкус (можно пофантазировать про лимон и вкусняшки!)",
    "seventh" : "Ты молодец 🤗"
}

#список вопросов для проверки ции...
Fourth = {
    "first":  "Шаг 1.\n"
              "Какую эмоцию я хочу изменить?\n"
              "Как эта эмоция отражается в теле?\n"
              "Насколько она интенсивна?",

    "second":  "Шаг 2.\n"
                "Что вызывает эту эмоцию?\n"
                "Описываем провоцирующее событие. "
                "Старайтесь описывать только факты, следите, чтобы не было оценки и осуждения. "
                "Если вы их обнаружите, переформулируйте безоценочно. "
                "Например, вместо оценочного суждения “я плохо справляюсь с работой” будет: “сегодня я сделала меньше, "
                "чем планировала”.",

    "third":   "Шаг 3.\n"
               "Что я думаю о ситуации?\n"
               "Приводим свои собственные, а затем все возможные способы и точки зрения интерпретации события. "
               "Проверяем, как они соответствуют фактам."
               "Например: “Друг не поделился мороженным, он меня ненавидит (моя интерпретация). "
               "Возможные интерпретации:"
               " “он был погружен в свои мысли, он был занят…”. Какое наиболее вероятное объяснение? "
               "Какие из этих фактов мы можем проверить? Пойти и задать прямо вопрос, например :)",

    "fourth":  "Шаг 4.\n"
                "Мне угрожает это?\n\n"
                "Воспринимаем ли мы это событие как угрозу для себя?"
                "Если да, то в чем проявляется угроза? "
                "Какие тревожные события и последствия я ожидаю от этой ситуации?\n\n"
                "А теперь подумайте, какой наиболее вероятный исход события!",

    "fifth":  "Шаг 5.\n"
               "Это конец?\n\n"
               "Представьте, что будет, если все-таки произойдет то, о чем вы беспокоитесь и тревожитесь. "
               "Затем представьте, как вы легко и хорошо справляетесь с ситуацией, не заостряя внимание на методе.",

    "sixth":  "Шаг 6.\n"
               "Насколько моя эмоция  (ее интенсивность и продолжительность) соответствует фактам реальности?",
}

#класс для отслеживания вопроса для заземления
class FirstMode(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()

#класс для отслеживания вопроса для проверки ции...
class SecondMode(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()