#imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
#variables
updater = Updater(token='1070149077:AAFzahRVuCQdWt8HyTUypp_g0G4aSIXmSaQ', use_context=True)
dispatcher = updater.dispatcher
#functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a POS. Don't talk to me!")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
def setdate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a POS")
def jaathagam(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I will predict the future!")
#main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

setdate_handler = CommandHandler('setdate', setdate)
dispatcher.add_handler(setdate_handler)

jaathagam_handler = CommandHandler('jaathagam', jaathagam)
dispatcher.add_handler(jaathagam_handler)

updater.start_polling()
print("I am working la dei!")