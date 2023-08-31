import telebot
from telebot import types

bot = telebot.TeleBot('6483356307:AAHEuX4FmibXZqJ8icaEHNDi0kISenNlnqc')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('🏙️ Тюмень', callback_data = 'city')
    markup.row(btn)
    bot.send_message(message.chat.id, f'<b>Привет {message.from_user.first_name}</b>\n  В каком городе вы хотите отдахнуть? 🤠', parse_mode = 'html', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'city':
        markup = types.InlineKeyboardMarkup()
        buttonTymcent = types.InlineKeyboardButton('Район Центральный ', callback_data = 'districtcent')
        buttonTymlen = types.InlineKeyboardButton('Район Ленинский ', callback_data = 'districtlen')
        buttonTymkal = types.InlineKeyboardButton('Район Калининский ', callback_data = 'districtkal')
        buttonTymvos = types.InlineKeyboardButton('Район Восточный ', callback_data = 'districtvos')
        
        markup.row(buttonTymcent, buttonTymlen)
        markup.row(buttonTymkal, buttonTymvos)
        bot.send_message(callback.message.chat.id, 'Районы где можно хорошо провести время: ', reply_markup = markup)


    if callback.data == 'districtcent':
        markup = types.InlineKeyboardMarkup()
        buttonTymCentRes = types.InlineKeyboardButton('Поесть', callback_data = 'restaurantcent')
        buttonTymCentAt = types.InlineKeyboardButton('Достопримечательности', callback_data = 'Attractionscent')
        buttonTymCentTh = types.InlineKeyboardButton('развлечения', callback_data = 'theatercent')
        markup.row(buttonTymCentRes)
        markup.row(buttonTymCentAt, buttonTymCentTh)
        bot.send_message(callback.message.chat.id, 'Места: ', reply_markup = markup)

    elif callback.data == 'restaurantcent':
        bot.send_message(callback.message.chat.id, 'Рестораны:\n -Cafe 15\86 , Адрес: ул. Володарского, 3\n -Ржавый ДЕД  Адрес: ул. Хохрякова, 47\n -Друзья говорят 5.0  Адрес: ​Улица Ю.-Р.Г. Эрвье, 32')
        
    elif callback.data == 'Attractionscent':
        bot.send_message(callback.message.chat.id, 'Достопримечательности:\n -Уличные музыкальные часы  Адрес: пересечение ул. Республики и ул. Мориса Тореза\n -Памятник бездомной собаки  Адрес: Ул. Орджоникидзе 63а перед зданием ЦУМа\n -Мост влюблённых  адрес: ул. Республики, д. 1')
    
    elif callback.data == 'theatercent':
        bot.send_message(callback.message.chat.id, 'развлечения:\n -ЛетоЛето(Аквапарк, развлекательный центр)  Адрес: адрес: ул. Щербакова 87\n - Городской парк культуры и отдыха  Адрес: Герцена, 63')
    



    if callback.data == 'districtlen':
        markup = types.InlineKeyboardMarkup()
        buttonTymLenRes = types.InlineKeyboardButton('Поесть', callback_data = 'restaurantlen')
        buttonTymLenAt = types.InlineKeyboardButton('Достопримечательности', callback_data = 'Attractionslen')
        
        markup.row(buttonTymLenRes, buttonTymLenAt)
        
        bot.send_message(callback.message.chat.id, 'Места: ', reply_markup = markup)

    elif callback.data == 'restaurantlen':
        bot.send_message(callback.message.chat.id, 'Рестораны:\n -Чито Грито, Адрес: ул. Холодильная, 132\n -Чум  Адрес: ул. Малыгина, 59, вх.12\n -Друзья говорят 5.0  Адрес: ​Улица Ю.-Р.Г. Эрвье, 32')
        
    elif callback.data == 'Attractionslen':
        bot.send_message(callback.message.chat.id, 'Достопримечательности:\n -Гилёвская роща\n -Музей «Ретро-техники им. В. В. Михайлова»  Адрес: ул. Велижанская, 69, стр. 3')
    

    

    if callback.data == 'districtkal':
        markup = types.InlineKeyboardMarkup()
        buttonTymKalRes = types.InlineKeyboardButton('Поесть', callback_data = 'restaurantkal')
        buttonTymKaLat = types.InlineKeyboardButton('Развлечения', callback_data = 'Attractionskal')
       
        markup.row(buttonTymKalRes,buttonTymKaLat)
        
        bot.send_message(callback.message.chat.id, 'Места: ', reply_markup = markup)

    elif callback.data == 'restaurantkal':
        bot.send_message(callback.message.chat.id, 'Рестораны:\n -Sovka coffee, Адрес: ул. Луначарского, 27\n -Творчество  Адрес: Молодёжная, 74 ст4')
        
    elif callback.data == 'Attractionskal':
        bot.send_message(callback.message.chat.id, 'Развлечения:\n -Форт арена адрес: ТЦ Арбат, ул. Николая Чаплина, 115а\n -Душа Сибири  адрес:  ул. Садовая, 73')
    


    if callback.data == 'districtvos':
        markup = types.InlineKeyboardMarkup()
        buttonTymVosRes = types.InlineKeyboardButton('Поесть', callback_data = 'restaurantvos')
        buttonTymVosLat = types.InlineKeyboardButton('Развлечения', callback_data = 'Attractionsvos')
        markup.row(buttonTymVosRes, buttonTymVosLat)
        bot.send_message(callback.message.chat.id, 'Куда вы хотите отправиться?', reply_markup = markup)

    elif callback.data == 'restaurantvos':
        bot.send_message(callback.message.chat.id, 'Рестораны:\n -Восточная долина, Адрес: ул. Вишнёвая, 1, 132\n -Чешский дворик  Адрес: ул. Широтная, 27/2, вх.12\n -Друзья говорят 5.0  Адрес: ​Улица Ю.-Р.Г. Эрвье, 32')
        
    elif callback.data == 'Attractionsvos':
        bot.send_message(callback.message.chat.id, 'Развлечения:\n -Джунгли 72 адрес: Широтная, 112 к2\n -Hlop Top  адрес: ТЦ Южный, ул. Мельникайте, 137')
    

    
    
bot.infinity_polling()

