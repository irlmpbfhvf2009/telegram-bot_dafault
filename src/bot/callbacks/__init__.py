from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from src.common.enum import STATES,CALLBACKSENUM
from src.bot.keyboard.__init__ import keyboard

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
