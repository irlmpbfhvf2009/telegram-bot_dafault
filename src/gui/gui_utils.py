from telegram import TelegramError
from multiprocessing import Process
from tkinter import messagebox
from src.sql.__init__ import DBHP
import tkinter
from src.gui.enum import GUIEnum

class start_bot_process():
    def __init__(self,tk):
        ...
        # super().__init__()
        tk.label_botstate.config(text=GUIEnum.BOT_STATE.value,command=self.start(tk))
        # print(tk.label_botstate.config().get('text'))
    def start(self,tk):
        tk.label_botstate.config(text="test")
        # try:
            # from src.bot.__init__ import Telegram_Bot
            # bot = Process(target=Telegram_Bot().run())
        #     bot.start()
        #     self.botPid=bot.pid
        #     self.button_bot_run.config(text="停止BOT",command=self.botStop)
        #     self.label_botstate.config(text="BOT状态：已启动")
        #     self.label_botusername.config(text="机器人："+DBHP().botusername)
        # except TelegramError as e:
        #     if str(e) == "Invalid token":
        #         messagebox.showwarning('Invalid token', '请检查config.ini')
        #         self.log.info("Invalid token")
        # except Exception as e:
        #     self.log.info(str(e))