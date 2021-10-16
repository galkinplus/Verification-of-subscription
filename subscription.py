import telebot
from telebot import types

token = "00000000:bot token"    # bot token
channel = "@channel"    # the channel to which the user should be subscribed

check = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
but1 = types.KeyboardButton("Button")    # attraction button
check.add(but1)

bot = telebot.TeleBot(token)

#    Message after pressing the start button indicating
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, text="Hi! It's me!\n\n"
                                           "Do you want to get a cool sticker in VK?\n\n"
                                           "Then subscribe to the channel\n👇👇👇\n\n"
                                           "[CHANNEL](https://t.me/channel)\n\nAnd then hit the get button\n\n"
                                           "*Get a sticker for free*", reply_markup=check, parse_mode='Markdown')

#    Checks whether the user is subscribed to the channel, if subscribed gives us a sticker,
#    if not subscribed asks to subscribe
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "Get a sticker for free":
        status = ['creator', 'administrator', 'member']
        for i in status:
            if i == bot.get_chat_member(chat_id=channel, user_id=message.from_user.id).status:
                chat_id = message.chat.id
                bot.send_message(chat_id, "Great, now you can get the sticker!\n\n", disable_web_page_preview=True)
                break
        else:
            chat_id = message.chat.id
            bot.send_message(chat_id, text="To get a sticker you need to subscribe to the channel.\n"
                                            "👇👇👇\n\n[CHANNEL](https://t.me/channel)", parse_mode='Markdown')

bot.polling(none_stop=True)