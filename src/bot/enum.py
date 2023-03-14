from enum import Enum

class BOTEnum(Enum):
    TOKEN = "5855785269:AAH9bvPpYudd2wSAvMnBTiKakCeoB92_Z_8"
    
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
    