# импорт нужных библиотек
import telebot
import wikipedia
wikipedia.set_lang('ru')

bot = telebot.TeleBot("1168155077:AAGm2sS9pYykci5X0_GKA606AyTuyM-DFaQ")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я ВикиБот. Пиши мне, что хочешь найти, я помогу')

@bot.message_handler(content_types=['text'])
def seach_page(message):
    search = message.text
    m = wikipedia.page(search)
    bot.send_message(message.chat.id, m.url)


bot.polling()

