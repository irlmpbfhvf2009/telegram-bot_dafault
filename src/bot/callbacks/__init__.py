from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from src.common.enum import STATES,CALLBACKSENUM
from src.bot.keyboard.__init__ import keyboard
from src.common.utils import logger as log
class callbacks():
    global globalForKeyboard
    globalForKeyboard = keyboard()
    
    def start(update:Update,context:CallbackContext):
        # 限制邀請人數才能發言
        if update.message.chat.type == 'private':
            context.bot.send_message(chat_id = update.effective_chat.id,text=CALLBACKSENUM.START.value,
                                     reply_markup=ReplyKeyboardMarkup(globalForKeyboard.wordFlowKeyboard))
            
            if str(update.effective_chat.id) == str(update.message.from_user.id):
                return STATES.WORKFLOW
            
    def wordFlow(update:Update,context:CallbackContext):
        keyword = update.message.text
        messageFromUser = f"[{str(update.message.from_user.id)}] {update.message.from_user.first_name} : {keyword}"
        log.info(messageFromUser)
        
        # results = context.bot.search_messages(chat_id=-100123456789, query=keyword) 
        results = context.bot.get_chat().message

        