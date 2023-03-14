from telegram import InlineKeyboardMarkup, InlineKeyboardButton ,KeyboardButton


class keyboard():
    def __init__(self):
        self.wordFlowKeyboard = self.wordFlowKeyboardBtn()
        
        
    def wordFlowKeyboardBtn(self):
        return [[KeyboardButton("如何将我添加到您的群组"),KeyboardButton("管理面板")],
                    [KeyboardButton("如何将我添加到您的频道"),KeyboardButton("支援团队列表")],
                    [KeyboardButton("管理员设置")]]