#!/home/fabiuxtech/coding/learning_coding/Python/tracking_message_to_telegram_bot/bin/python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ciao Benvenuto nel bot di Fabiux')
    keyboard = [
        [InlineKeyboardButton('Stato di Dell XPS', callback_data='action1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Seleziona un\'azione:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    action = query.data

    if action == 'action1':
        query.edit_message_text(text='Verifico lo stato di Dell XPS')

updater = Updater('2086863893:AAG848UXv38R7N5nym-gUrlE6kPe-ow7hsQ', use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()