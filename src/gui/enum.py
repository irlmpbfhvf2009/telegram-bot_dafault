from enum import Enum

class GUIEnum(Enum):
    GUI_TITLE = "telegram-bot"
    BOT_USERNAME = "机器人："
    VERSION = "版本号："
    TOKEN = "TOKEN："
    
    BOT_STATE_START = "BOT状态：running"
    BOT_STATE_STOP = "BOT状态：stop"
    BOT_BTN_START = "启动BOT"
    BOT_BTN_STOP = "停止BOT"
    
    WEB_STATE_START = "WEB状态：running"
    WEB_STATE_STOP = "WEB状态：stop"
    WEB_BTN_START = "开启网页"
    # WEB_BTN_STOP = "关闭网页"
    