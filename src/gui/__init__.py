import threading,tkinter,os,datetime,inspect,ctypes
import tkinter.font as tkFont
from tkinter import messagebox,ttk
from src.common.enum import GUIEnum
from src.gui.gui_utils import bot_process,web_process,common
from src.common.utils import logger
import logging


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
            
        self.title(GUIEnum.GUI_TITLE.value)
        self.center_window(700,400)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        self.frameOne = tkinter.Frame(self.notebook)
        self.frameTwo = tkinter.Frame(self.notebook)
        
        #self.log=Logging(file='log/'+str(datetime.datetime.now().date())+'.log',guiFile='log/gui_.log')
        self.resizable(width=False,height=False)
        fontStyle = tkFont.Font(family="Lucida Grande", size=16)
        self.label_time = tkinter.Label(self.frameOne,font=fontStyle)
        self.label_botstate = tkinter.Label(self.frameOne,text=GUIEnum.BOT_STATE_STOP.value, fg="red",anchor="w", justify="left")
        self.label_webstate = tkinter.Label(self.frameOne,text=GUIEnum.WEB_STATE_STOP.value, fg="red",anchor="w", justify="left")
        self.label_botusername = tkinter.Label(self.frameOne,text=GUIEnum.BOT_USERNAME.value)
        self.label_version = tkinter.Label(self.frameOne,text=GUIEnum.VERSION.value)
        self.label_token = tkinter.Label(self.frameOne,text=GUIEnum.TOKEN.value)
        
        
        self.button_botstate = tkinter.Button(self.frameOne,command=self.bot_process,width=9,height=2,text=GUIEnum.BOT_BTN_START.value)
        self.button_webstate = tkinter.Button(self.frameOne,command=self.web_process,width=9,height=2,text=GUIEnum.WEB_BTN_START.value)
        
        # 日誌輸出
        self.normalTextBox = tkinter.Text(self, width=98,height=10)
        self.normalTextBox.bind("<Key>", lambda e: common.ctrlEvent(e))
        
        logger.info("日志初始化完成")
        
        # 布局
        self.label_time.place(x=50, y=20)
        self.label_botstate.place(x=50,y=60)
        self.label_webstate.place(x=50,y=90)
        self.label_botusername.place(x=50,y=120)
        self.label_token.place(x=50,y=150)
        self.label_version.place(x=50,y=180)

        self.button_botstate.place(x=550, y=40)
        self.button_webstate.place(x=450, y=40)
        self.normalTextBox.place(x=5, y=250)
        
        # 執行緒
        self.time = threading.Thread(target=self.updateTime)
        self.time.start()
        
        # 分页
        self.notebook.add(self.frameOne, text='选项卡1')
        self.notebook.add(self.frameTwo, text='日至')
        
        self.protocol('WM_DELETE_WINDOW', self.wm_delete_window)
        
    
        
        
    def center_window(self,w, h):
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    def log_output(self,log):
        self.normalTextBox.insert(tkinter.END,log)
        self.normalTextBox.see(tkinter.END)
        
    def updateTime(self):
        common(self).updateTime()
    
    def bot_process(self):
        self.bot = bot_process(self)
        self.bot.start_bot_process()
    
    def web_process(self):
        return web_process(self)

    def wm_delete_window(self):
        try:
            self.bot.stop_bot_process()
        except:
            pass
        finally:
            self.destroy()
            self.quit()
            
    
    def run(self):
        self.mainloop()
    
class TkinterHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
    def emit(self, record):
        msg = self.format(record)
        self.text_widget.config(state=tkinter.NORMAL)
        self.text_widget.insert(tkinter.END, msg + '\n')
        self.text_widget.config(state=tkinter.DISABLED)
        self.text_widget.yview(tkinter.END)