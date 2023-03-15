from enum import Enum

class DBHPEnum(Enum):
    DB_NAME = "telegram-bot.db"
    BOT_STATE = "BOT状态：未启动"
    WEB_STATE = "网页状态：未启动"
    BOT_USERNAME = "机器人："
    VERSION = "版本号："
    TOKEN = "TOKEN："
    APP_RUN = "开启网页"
    BOT_RUN = "启动BOT"
    
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
    
class BOTEnum(Enum):
    TOKEN = "5855785269:AAH9bvPpYudd2wSAvMnBTiKakCeoB92_Z_8"
    
class CALLBACKSENUM(Enum):
    START = "What con this bot do?\nPlease tap on START"

class STATES(Enum):
    # 初始状态，通过 /start 命令或点击按钮触发。
    START = 0
    # 处理普通文本消息的状态，用于处理用户输入的一般消息。
    WORKFLOW = 1
    # 处理修改密码的状态。
    CHANGEPASSWORD = 2
    # 处理设置邀请好友数量的状态。
    SETINVITEFRIENDSQUANTITY = 3
    # 理设置自动清理邀请好友数量的状态。
    SETINVITEFRIENDSAUTOCLEARTIME = 4
    # 处理选择群组的状态。
    SELECTGROUP = 5
    # 处理设置删除消息时间的状态。
    DELETEMSGFORSECOND = 6
    # 处理获取权限的状态。
    GETTHERIGHT = 7
    # 处理管理员工作的状态。
    ADMINWORK = 8
    # 处理设置邀请成员的状态。
    SETINVITEMEMBERS = 9
    # 处理设置邀请奖励的状态。
    SETINVITEEARNEDOUTSTAND = 10
    # 处理设置邀请结算奖励的状态。
    SETINVITESETTLEMENTBONUS = 11
    # 处理设置联系人的状态。
    SETCONTACTPERSON = 12
    # 处理开启计费会话的状态。
    BILLINGSESSION = 13
    # 处理查询计费会话的状态。
    QUERYBILLINGSESSION = 14
    # 处理设置群组广告时间的状态。
    GROUPSETADVERTISETIME = 15
    # 处理设置群组广告内容的状态。
    GROUPSETADVERTISECONTENT = 16
    # 处理删除指定群组广告内容的状态。
    GROUPSPECIFYDELETEADVERTISECONTENT = 17
    