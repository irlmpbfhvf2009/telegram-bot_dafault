import time,threading,tkinter,os,datetime,inspect,ctypes
import tkinter.font as tkFont
from tkinter import messagebox
from src.common.utils import Log,Logging
from src.gui.enum import GUIEnum
from src.gui.gui_utils import start_bot_process

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
            
        self.title(GUIEnum.TITLE.value)

        self.center_window(700,400)

        #self.log=Logging(file='log/'+str(datetime.datetime.now().date())+'.log',guiFile='log/gui_.log')
        self.resizable(width=False,height=False)
        fontStyle = tkFont.Font(family="Lucida Grande", size=16)
        self.label_time = tkinter.Label(self,font=fontStyle)
        self.label_botstate = tkinter.Label(self,text='444')
        self.label_appstate = tkinter.Label(self,text=GUIEnum.WEB_STATE.value)
        self.label_botusername = tkinter.Label(self,text=GUIEnum.BOT_USERNAME.value)
        self.label_version = tkinter.Label(self,text=GUIEnum.VERSION.value)
        self.label_token = tkinter.Label(self,text=GUIEnum.TOKEN.value)
        
        print(self.label_botstate.config().get('text'))
        
        self.button_app_run = tkinter.Button(self,text=GUIEnum.APP_RUN.value)
        self.button_bot_run = tkinter.Button(self,text=GUIEnum.BOT_RUN.value,command=start_bot_process(self))
        
        # 日誌輸出
        self.normalTextBox = tkinter.Text(self, width=98,height=10)
        self.normalTextBox.bind("<Key>", lambda e: self.ctrlEvent(e))
        
        # 布局
        self.label_time.place(x=50, y=20)
        self.label_botstate.place(x=50,y=60)
        self.label_appstate.place(x=50,y=90)
        self.label_botusername.place(x=50,y=120)
        self.label_token.place(x=50,y=150)
        self.label_version.place(x=50,y=180)

        self.button_bot_run.place(x=550, y=40)
        self.button_app_run.place(x=450, y=40)
        self.normalTextBox.place(x=5, y=250)
        
        # 執行緒
        self.time = threading.Thread(target=self.updateTime)
        self.time.start()
        
        
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
        while True:
            try:
                date = time.strftime("%Y-%m-%d   %H:%M:%S")
                self.label_time.config(text=date)
                self.update()
                time.sleep(1)
            except:
                break
    
    def run(self):
        self.mainloop()
    
    