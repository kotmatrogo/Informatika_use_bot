
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7138053354:AAEmj1yzXl4W1cGVPAYyXNmm1BbooztfwaQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

urlkb = InlineKeyboardMarkup(row_width=3)

urlButton1 = InlineKeyboardButton(text='1️⃣ задание', callback_data='button1')
urlButton2 = InlineKeyboardButton(text='2️⃣ задание', callback_data='button2')
urlButton3 = InlineKeyboardButton(text='3️⃣ задание', callback_data='button3')
urlButton4 = InlineKeyboardButton(text='4️⃣ задание', callback_data='button4')
urlButton5 = InlineKeyboardButton(text='5️⃣ задание', callback_data='button5')
urlButton6 = InlineKeyboardButton(text='6️⃣ задание', callback_data='button6')
urlButton7 = InlineKeyboardButton(text='7️⃣ задание', callback_data='button7')
urlButton8 = InlineKeyboardButton(text='8️⃣ задание', callback_data='button8')
urlButton9 = InlineKeyboardButton(text='9️⃣ задание', callback_data='button9')
urlButton10 = InlineKeyboardButton(text='1️⃣0️⃣ задание', callback_data='button10')
urlkb.add(urlButton1, urlButton2, urlButton3, urlButton4, urlButton5, urlButton6, urlButton7, urlButton8, urlButton9, urlButton10)

kbb = InlineKeyboardMarkup(row_width=1)
back_buttom = InlineKeyboardButton(text='Назад', callback_data='start')
kbb.add(back_buttom)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет 👋!  Я Виртуальный помощник для подготовки к ОГЭ по информатике!  "
                        "Выбери задание от 1 до 10, а я тебе обязательно отвечу как его решать.", reply_markup=urlkb)

@dp.callback_query_handler(lambda c: c.data == "start")
async def start_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выбери задание от 1 до 10, а я тебе обязательно отвечу как его решать.', reply_markup=urlkb)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task1, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task2, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task3, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task4, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task5, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button6')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task6, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button7')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task7, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button8')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task8, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button9')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task9, reply_markup=kbb)

@dp.callback_query_handler(lambda c: c.data == 'button10')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, task10, reply_markup=kbb)

task1 = "Задание №1.\nЭто задание посвятили кодированию информации и единицам измерения её количества. Чтобы справиться " \
        "с № 1, нужно помнить, что 1 байт содержит 8 бит, и опираться на условия задачи.\n\n ПРИМЕР ЗАДАНИЯ 1\n  В кодировке КОИ-8 " \
        "каждый символ кодируется 8 битами. Вова написал текст (в нем нет лишних пробелов): «Школьные предметы: ОБЖ, химия," \
        " физика, алгебра, биология, география, литература, информатика». Ученик удалил из списка название одного предмета, " \
        "а также лишние запятую и пробел — два пробела не должны идти подряд. При этом размер нового предложения в данной " \
        "кодировке оказался на 11 байт меньше, чем размер исходного предложения. Напишите в ответе вычеркнутое название " \
        "предмета.\n\n РЕШЕНИЕ\n Поскольку один символ кодируется 8 битами или одним байтом, из текста удалили 11 символов. " \
        "Заметим, что лишние запятая и пробел занимают два байта. Значит, название предмета, которое удалили из списка, должно" \
        " состоять из девяти букв, поскольку (11−2):1=9 символов. Из всего списка только одно название предмета состоит из 9 букв — география.\n"

task2 = "Задание №2.\nВ этом задании условие даёт нам числовой код с зашифрованным паролем и ключ к нему. Всё, что " \
        "нужно, — перевести код в слово по этому ключу.\n\n ПРИМЕР ЗАДАНИЯ 2\nВася и Петя играли в шпионов и кодировали " \
        "сообщение собственным шифром. Фрагмент кодовой таблицы приведен ниже:\nК = @+\nЛ = ~+\nМ = +@\nН = @~+\nО = +\n" \
        "П = ~\n\nРЕШЕНИЕ\nУчитывая условие, что буквы в сообщении не повторяются, расшифруем код:\n+ ~ + ~ + @ @ ~ + = ОЛПМН." \
        " Всего букв в сообщении 5.\n Ответ: 5."

task3 = "Задание №3.\nЭто задание на основы математической логики. Чтобы решить его, нужно понимать базовые определения из математики" \
        " и уметь пользоваться логическими операторами.\n\nПРИМЕР ЗАДАНИЯ 3\n\n Напишите наибольшее целое число x, для которого" \
        " истинно высказывание:\nНЕ (X <= 11) И НЕ (X >= 17).\n\nРЕШЕНИЕ\nЗапишем выражение в виде\n(X > 11) И (X < 17). Значит," \
        " наибольшее число, для которого высказывание будет истинным — 16.\nОтвет: 16."

task4 = "Задание №4.\nЭто задание об информационных моделях данных, которые представлены в виде таблиц. Чтобы справиться с ним, нужно" \
        " уметь анализировать их, чтобы найти кратчайший путь по данным из условия.\n\n"

task5 = "Задание №5.\nЭто задание экзамена проверит, умеет ли ученик 9 класса работать с алгоритмами и знает ли их свойства. " \
        "\n\n"

task6 = "Задание №6.\nЭто задание ОГЭ по информатике проверит, как хорошо школьник знает операторы одного из 5 предложенных языков " \
        "программирования. Для того чтобы решить эту задачу, можно выбрать любой знакомый язык.\n\n"

task7 = "Задание №7.\nЭто задание на принципы адресации в интернете. Чтобы правильно выполнить его, повторите, из каких частей состоит" \
        " URL.\n\n"

task8 = "Задание №8.\nЭто задание покажет, понимает ли школьник, как работает выдача по запросам в поисковых системах. Если хотите " \
        "справиться с ним, повторите темы «Средства и методика поиска информации в сети Интернет» и «Построение запросов»." \
        " Советуем добавить материалы по ним в ваш план для подготовки к ОГЭ по информатике.\n\n"

task9 = "Задание №9.\nЭто задание, которое покажет, хорошо ли ученик умеет воспринимать информацию, которую подали в виде схемы. " \
        "Конкретно в № 9 ему нужно будет найти количество таких путей из одного города в другой, чтобы они обязательно " \
        "проходили через третий. Решить эту задачу будет проще всего с помощью дерева. В нём можно перечислить все пути," \
        " а после просто подсчитать их.\n\n"

task10 = "Задание №10.\nЭто последнее задание 1-й части экзамена. Оно посвящено системам счисления. Чтобы как можно лучше подготовиться" \
         " к ОГЭ по информатике, советуем отработать этот тип задач.\n\n"

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
