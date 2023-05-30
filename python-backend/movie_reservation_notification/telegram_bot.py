import telegram

bot = telegram.Bot(token='5900184100:AAHwtH_6wRuJv9goEyuM8RdzA_1SCGXs2ow')

for i in bot.getUpdates():
    print(i.message)

# bot.sendMessage(chat_id=6137914993, text="테스트입니다")