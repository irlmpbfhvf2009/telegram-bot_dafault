import tkinter as tk
from tkinter import ttk
from threading import Thread

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # 設定視窗標題
        self.title("My App")

        # 設定視窗大小和位置
        self.geometry("800x600+100+100")

        # 建立一個 notebook 控制元件，用來顯示多個頁面
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # 建立 Flask 頁面
        self.flask_page = tk.Frame(self.notebook)
        self.notebook.add(self.flask_page, text="Flask")

        # 啟動 Flask 應用程式
        # self.flask_thread = Thread(target=app.run)
        # self.flask_thread.start()

        # 建立 Telegram Bot 頁面
        self.telegram_page = tk.Frame(self.notebook)
        self.notebook.add(self.telegram_page, text="Telegram Bot")

        # 啟動 Telegram Bot
        # self.telegram_thread = Thread(target=bot.polling)
        # self.telegram_thread.start()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()