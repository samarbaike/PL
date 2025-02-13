from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_API_TOKEN' with the token you got from BotFather
API_TOKEN = 8027658252:AAH53Ut2uIkZsTyztyivDssIls4-mQ3hZC0

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot. How can I help you? 😊")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    # Set up the bot with the API token
    updater = Updater(API_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for different commands and messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
