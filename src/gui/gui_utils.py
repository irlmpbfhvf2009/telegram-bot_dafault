from src.common.enum import GUIEnum
from src.bot.__init__ import run as bot_run
from multiprocessing import Process
from src.common.utils import logger
import time


class common():
    def __init__(self,tk):
        self.tk = tk
        
    def updateTime(self):
        while True:
            try:
                date = time.strftime("%Y-%m-%d   %H:%M:%S")
                self.tk.label_time.config(text=date)
                self.tk.update()
                time.sleep(1)
            except:
                break
            
    def ctrlEvent(self,event):
        if(12==event.state and event.keysym=='c' ):
            return
        else:
            return "break"
        
class bot_process():
    def __init__(self,tk):
        self.tk = tk
        self.bot = Process(target = bot_run)
        
    def start_bot_process(self):
        self.tk.label_botstate.config(text=GUIEnum.BOT_STATE_START.value, fg="green",anchor="w", justify="left")
        self.tk.button_botstate.config(text=GUIEnum.BOT_BTN_STOP.value,command=self.stop_bot_process)
        self.bot.start()
        
        
    def stop_bot_process(self):
        print(self.bot.is_alive())
        if self.bot.is_alive():
            self.tk.label_botstate.config(text=GUIEnum.BOT_STATE_STOP.value , fg="red",anchor="w", justify="left")
            self.tk.button_botstate.config(text=GUIEnum.BOT_BTN_START.value,command=self.start_bot_process)
            self.bot.terminate()
            self.bot.join()
            logger.info("Bot process terminated")

class web_process():
    def __init__(self,tk):
        self.tk = tk
        # self.web = Process(target = web_run)
        self.start_web_process()
        
    def start_web_process(self):
        self.tk.label_webstate.config(text=GUIEnum.WEB_STATE_START.value, fg="green",anchor="w", justify="left")
        self.tk.button_webstate.config(text=GUIEnum.WEB_BTN_START.value,command=self.stop_web_process)
        
    def stop_web_process(self):
        self.tk.label_webstate.config(text=GUIEnum.WEB_STATE_STOP.value, fg="red",anchor="w", justify="left")
        self.tk.button_webstate.config(text=GUIEnum.WEB_BTN_START.value,command=self.start_web_process)
        logger.info("Web process terminated")
