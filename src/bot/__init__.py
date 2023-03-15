from telegram.ext import Updater,Filters,CommandHandler,MessageHandler,ConversationHandler,CallbackQueryHandler,ChatMemberHandler
from src.common.enum import STATES,BOTEnum
from src.bot.callbacks.__init__ import callbacks
from src.common.utils import logger
import time

class Telegram_Bot():
    def __init__(self):
        
        self.updater = Updater(BOTEnum.TOKEN.value)
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(
            ConversationHandler(
                entry_points=[CommandHandler('start', callbacks.start),
                                # CallbackQueryHandler(choose),
                                # MessageHandler(filters=Filters.all & (~ Filters.command), callback=wordFlow)
                            ],
                states={
                    STATES.START:[CommandHandler('start', callbacks.start)],
                    # STATES.WORKFLOW: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=wordFlow)],
                    # STATES.CHANGEPASSWORD: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=changePassword)],
                    # STATES.SETINVITEFRIENDSQUANTITY: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=setInviteFriendsQuantity)],
                    # STATES.SETINVITEFRIENDSAUTOCLEARTIME: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=setInviteFriendsAutoClearTime)],
                    # STATES.SELECTGROUP: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=selectGroup)],
                    # STATES.DELETEMSGFORSECOND: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=deleteMsgForSecond)],
                    # STATES.GETTHERIGHT: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=getTheRight)],
                    # STATES.ADMINWORK: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=adminWork)],
                    # STATES.SETINVITEMEMBERS: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=setInvitemembers)],
                    # STATES.SETINVITEEARNEDOUTSTAND: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=setInviteearnedoutstand)],
                    # STATES.SETINVITESETTLEMENTBONUS: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=setInvitesettlementBonus)],
                    # STATES.SETCONTACTPERSON: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=setContactPerson)],
                    # STATES.BILLINGSESSION: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=billing)],
                    # STATES.QUERYBILLINGSESSION: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=queryBilling)],

                    # # 广告会话
                    # STATES.GROUPSETADVERTISETIME: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=groupSetAdvertiseTime)],
                    # STATES.GROUPSETADVERTISECONTENT: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=groupSetAdvertiseContent)],
                    # STATES.GROUPSPECIFYDELETEADVERTISECONTENT: [MessageHandler(filters=Filters.text & (~ Filters.command), callback=groupSpecifyDeleteAdvertiseContent)],
                },fallbacks=[CommandHandler('start', callbacks.start),
                            #  CallbackQueryHandler(choose),MessageHandler(filters=Filters.text & (~ Filters.command), callback=wordFlow)
                             ]))

        # self.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, joinGroup))
        # self.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, leftGroup))
        # self.dispatcher.add_handler(MessageHandler(Filters.update.channel_post, channel_post))
        # self.dispatcher.add_handler(ChatMemberHandler(channel, ChatMemberHandler.MY_CHAT_MEMBER))
        
def run ():
    start = time.time()
    tb=Telegram_Bot()
    tb.updater.start_polling()
    end = time.time()
    logger.info(f"BOT : {tb.updater.bot.username} 已启动  執行時間：{round((end - start),2)}秒")

    tb.updater.idle()
    tb.updater.stop()
        
