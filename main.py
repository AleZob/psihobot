from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import BadRequest
from aiogram.dispatcher import FSMContext

from support import get_keyboard, Third, Fourth, FirstMode, SecondMode
from tokennn import TOKEN


bot = Bot(token=TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(state='*', commands='start')
async def cmd_start(message: types.Message, state:FSMContext):
    await state.finish()
    await message.answer("Привет!\nЗдесь есть:", reply_markup=get_keyboard(1))

@dp.message_handler(state='*', commands='back')
async def cmd_start(message: types.Message, state:FSMContext):
    await state.finish()
    await message.reply("Ты отменил дейсвие и вернулся в Главное меню", reply_markup=get_keyboard(1))

@dp.message_handler(state='*', commands='help')
async def cmd_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("""Привет!
    Я бот созданный помочь тебе
    У меня есть команды:
    /start -- вызывает главное меню
    /help -- отправляет этот текст
    /back -- отмена действия и возврат в главное меню""")

@dp.errors_handler(exception=BadRequest)
async def error_bot_blocked(update: types.Update, exception: BadRequest):
    print(f"Сообщение: {update}\nОшибка: {exception}")
    return True


#ниже - обработка всех действий

@dp.callback_query_handler(Text(startswith="do_"), state="*")
async def inline_funk_comp(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split("_")[1]
    if action.startswith("start-"):
        action = call.data.split("-")[1]
        if action == "four":
            await call.message.edit_text(Third["first"], reply_markup=get_keyboard(6))
            await FirstMode.Q1.set()
            await call.answer()
        elif action == "five":
            await call.message.edit_text(Fourth["first"], reply_markup=get_keyboard(6))
            await SecondMode.Q1.set()
            await call.answer()
    elif action == "first":
        await call.message.edit_text("Хороший выбор!\nВот варианты:", reply_markup=get_keyboard(2))
        await call.answer()
    elif action == "second":
        await call.message.edit_text("Этот раздел в разработке", reply_markup=get_keyboard(3))
        await call.answer()
    elif action == "third":
        await call.message.edit_text("Эта простая практика очень помогает, когда одолевают разные болезненные мысли.\n"
                                     "Она помогает сделать передышку и заземлиться, выйти из роящихся в голове мыслей.\n"
                                     "Вы готовы?",
                                     reply_markup=get_keyboard(4))
        await call.answer()
    elif action == "fourth":
        await call.message.edit_text("Вы выбрали вариант:\n"
                                     "Эмоции и факты\n"
                                     "Продолжить?",
                                     reply_markup=get_keyboard(5))
        await call.answer()
    elif action == "back":
        await state.finish()
        await call.message.edit_text("Привет!\nЗдесь есть:", reply_markup=get_keyboard(1))
        await call.answer()



@dp.callback_query_handler(Text(startswith="no_"), state="*")
async def inline_funk_comp(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split("_")[1]
    if action == "next":
        current_state = await state.get_state()
        if "FirstMode:Q1" == current_state:
            await FirstMode.next()
            await call.message.edit_text(Third["second"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "FirstMode:Q2" == current_state:
            await FirstMode.next()
            await call.message.edit_text(Third["third"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "FirstMode:Q3" == current_state:
            await FirstMode.next()
            await call.message.edit_text(Third["fourth"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "FirstMode:Q4" == current_state:
            await FirstMode.next()
            await call.message.edit_text(Third["fifth"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "FirstMode:Q5" == current_state:
            await FirstMode.next()
            await call.message.edit_text(Third["sixth"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "FirstMode:Q6" == current_state:
            await FirstMode.next()
            await call.message.edit_text(Third["seventh"], reply_markup=get_keyboard(6))
            await call.answer()
        elif"FirstMode:Q7" == current_state:
            await state.finish()
            await call.message.edit_text("Молодец!\nТы закончил Заземление!\nПопробуешь что то новое?",
                                         reply_markup=get_keyboard(1))
            await call.answer()
        elif "SecondMode:Q1" == current_state:
            await SecondMode.next()
            await call.message.edit_text(Fourth["second"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "SecondMode:Q2" == current_state:
            await SecondMode.next()
            await call.message.edit_text(Fourth["third"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "SecondMode:Q3" == current_state:
            await SecondMode.next()
            await call.message.edit_text(Fourth["fourth"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "SecondMode:Q4" == current_state:
            await SecondMode.next()
            await call.message.edit_text(Fourth["fifth"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "SecondMode:Q5" == current_state:
            await SecondMode.next()
            await call.message.edit_text(Fourth["sixth"], reply_markup=get_keyboard(6))
            await call.answer()
        elif "SecondMode:Q6" == current_state:
            await state.finish()
            await call.message.edit_text("Молодец!\nТы закончил Эмоции и факты!\nПопробуешь что то новое?",
                                         reply_markup=get_keyboard(1))
            await call.answer()
    #elif action == "back":
    #    await state.finish()
    #    await call.message.edit_text("Ты отмения действие!", reply_markup=get_keyboard(1))
    #   await call.answer()





if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)