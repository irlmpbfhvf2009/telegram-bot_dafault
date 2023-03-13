from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton ,KeyboardButton,ReplyKeyboardMarkup,TelegramError
from telegram.ext import Updater,Filters, CallbackContext,CommandHandler,MessageHandler,ConversationHandler,CallbackQueryHandler,ChatMemberHandler
import datetime,time,json
from src.bot.enum import Admin,General
from src.common.utils import Logging

class Telegram_Bot():
    def __init__(self):
        log = Logging(logger_level='DEBUG',file='log/'+str(datetime.datetime.now().date())+'.log')
        log.info("123")
        def start(update: Update, context: CallbackContext):
            print('123')

        def cancel(update: Update, context: CallbackContext):
            return ConversationHandler.END
        
        self.updater = Updater("5855785269:AAH9bvPpYudd2wSAvMnBTiKakCeoB92_Z_8")
        self.updater.dispatcher.add_handler(
            ConversationHandler(
                 entry_points=[CommandHandler('start', start),],
                 states={
                        General.START:[CommandHandler('start', start)],
                 },fallbacks=[CommandHandler('cancel', cancel)]
            ))
        
    def run (self):
        self.updater.start_polling()
        self.updater.idle()
        self.updater.stop()
        
