import telebot
import random

# Це наш токен
TOKEN = '5996897495:AAFMDLzSz2bdHp8PThxLAlNMHje_RMUSzBs'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('crystal-ball-gypsy.mp4', 'rb')
    bot.send_animation(message.chat.id, sti)
    bot.send_message(message.chat.id, "Привіт. Я чарівна куля-гадалка."
                                      "Постав мені будь-яке питаня, на яке можна відповісти Так або Ні.")


text = ['Так! Будь готовий отримати суцільні ніштяки від Всесвіту.',
        'Авжеж так! Відчуваєш цей вайб успіху в повітрі? ',
        'Звісно! Ти рухаєшся в правильному напрямку — тримай хвилю!',
        'Так! Зійшла твоя щаслива зірка, отже все буде топчик.',
        'Ні, тримайся подалі від трешу.',
        'Воу-воу! Пригальмуй, це не те, що тобі потрібно!',
        'Ні, не варто. Не мінусуй у карму.',
        'Можливо все. Щоб не зашкваритись, дослухайся до голосу серця.',
        'Шанси рівні: 50 / 50. Та будь що — налаштовуй себе на відпадний фінал.',
        'Може бути, а може й ні! Звертай увагу на прикольні знаки довкола.']


@bot.message_handler(content_types=['text'])
def send_mem(message):
    x = random.randrange(0, len(text))
    bot.send_message(message.chat.id, text[x])


bot.polling(none_stop=True)
