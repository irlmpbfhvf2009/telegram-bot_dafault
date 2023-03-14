###### BOT說明
>[bot使用方法](#bot使用方法)  
[开启监听频道权限](#开启监听频道权限)  

###### 開發事項  
>[專案結構](#專案結構)  
[專案架構](#專案架構)  
[SQL](#SQLITE3)  
[功能進度](#功能進度)  


#### 更新資訊

###### 1.6.4
* 優化介面
* 廣告功能調整(發送第四次廣告,前三次訊息刪除)
* 資料表advertiseRecord (groupId,messageId)
* 統整vite網頁畫面
* config判斷 token檢查
###### 1.6.3
* 完成 UI介面
* 全域logger
* 優化程式碼
###### 1.6.2
* tkinter UI介面
* multiprocessing 多核心運算
* 定義版本號
###### 1.6.1
* API新增
* 查詢、修改config群組
###### 1.6.0
* 侦测机器人所在群组有无权限
* 侦测机器人所在频道有无权限
* 定义3种lor.warning  

        'NoneType' object is not subscriptable       机器人无订阅频道(故无法启动订阅发言权功能)  
        Message can't be deleted                     机器人在群组无足够权限删除消息  
        Not enough rights to manage chat invite link 机器人在群组无足够权限取得邀请连结  



## 开启监听频道权限  
>1.首先我们TG找到BotFather 打开跟他的会话窗口，发送 /setprivacy  
2.点选Disable
<picture>
  <img alt="Shows mode." src="https://img-blog.csdnimg.cn/img_convert/6ed7818985d811d5445ff88cc88b029b.png">
</picture>  



## bot使用方法
>config.ini 填入Token  
run main.py 執行機器人  


## 專案結構  
Telegram-Bot/  
|-- main.py  
|-- main.spec  
|-- config.ini  
|-- telegram-bot.db  
|-- README.md  
|-- requirements.txt  
|-- log/  
&emsp;&emsp;|-- * files *  
|-- resources/  
&emsp;&emsp;|-- favcon.ico  
    |-- static/  
&emsp;&emsp;&emsp;&emsp;|-- * files *  
&emsp;&emsp;|-- templates/  
&emsp;&emsp;&emsp;&emsp;|-- * files *  
|-- src/  
&emsp;&emsp;|-- bot/  
&emsp;&emsp;&emsp;&emsp;|-- bot.py  
&emsp;&emsp;&emsp;&emsp;|-- utils/  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-- _button.py  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-- _config.py  
&emsp;&emsp;|-- common/  
&emsp;&emsp;&emsp;&emsp;|-- logger.py  
&emsp;&emsp;&emsp;&emsp;|-- utils.py  
&emsp;&emsp;|-- sql/  
&emsp;&emsp;&emsp;&emsp;|-- sql指令/  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|-- * files *  
&emsp;&emsp;&emsp;&emsp;|-- sql.py  
&emsp;&emsp;|-- tkinter/  
&emsp;&emsp;&emsp;&emsp;|-- gui.py  
&emsp;&emsp;|-- web/  
&emsp;&emsp;&emsp;&emsp;|-- app.py  

## 这是一个使用Python编写的Telegram机器人程序。其中包含了一个ConversationHandler，用于处理机器人与用户之间的会话交互。 
#### 1.用户交互逻辑
* start：用户发送/start命令，启动机器人，进入START状态
* choose：用户点击inline keyboard上的按钮，根据不同按钮的callback_data进入不同的状态
* wordFlow：用户发送文本消息，根据当前状态进入不同的状态，进行不同的操作
* changePassword：用户进入修改密码流程，输入旧密码和新密码，保存新密码并返回上一级状态
* setInviteFriendsQuantity：用户进入设置邀请好友数量流程，输入数量，保存数量并返回上一级状态
* setInviteFriendsAutoClearTime：用户进入设置自动清理邀请好友时间流程，输入时间，保存时间并返回上一级状态
* selectGroup：用户进入选择群组流程，输入群组名称，保存群组名称并返回上一级状态
* deleteMsgForSecond：用户进入设置撤回消息时间流程，输入时间，保存时间并返回上一级状态
* getTheRight：用户进入抢答流程，机器人向群组发送抢答问题，第一个回答的用户获胜，保存获胜用户信息并返回上一级状态
* adminWork：用户进入管理员工作流程，输入命令，执行相应的管理员操作并返回上一级状态
* setInvitemembers：用户进入设置邀请会员流程，输入会员ID，保存会员ID并返回上一级状态
* setInviteearnedoutstand：用户进入设置邀请奖励流程，输入奖励金额，保存奖励金额并返回上一级状态
* setInvitesettlementBonus：用户进入设置邀请结算流程，输入结算金额，保存结算金额并返回上一级状态
* setContactPerson：用户进入设置联系人流程，输入联系人信息，保存联系人信息并返回上一级状态
* billing：用户进入计费流程，进行计费操作，计费成功后返回上一级状态
* queryBilling：用户进入查询计费流程，进行计费查询操作，查询成功后返回上一级状态
* groupSetAdvertiseTime：用户进入设置群组广告时间流程，输入广告时间，保存广告时间并返回上一级状态
* groupSetAdvertiseContent：用户进入设置群组广告内容流程，输入广告内容，保存广告内容并返回上一级状态
* groupSpecifyDeleteAdvertiseContent：用户进入指定删除群组广告内容流程，输入要删除的广告内容ID，删除广告内容并返回上一级状态


## SQLITE3
SCHEMAS:telegram-bot.db
#### TABLE : config  組態設定
###### column: key,value
>password(密碼)  
botuserName 機器人用戶名  
inviteFriendsAutoClearTime 邀請好友記錄清除日期  
inviteFriendsSet 邀請好友發言權開關  
followChannelSet 關注頻道發言權開關  
inviteFriendsQuantity 邀請好友數量  
description 描述  

#### TABLE : invitationLimit 邀請好友紀錄
groupId 群組id,  
groupTitle 群組名稱,  
inviteId 邀請人ID,  
inviteAccount 邀請人帳號,  
beInvited 被邀請人JSON,  
invitationStartDate 邀請日期,  
invitationEndDate 過期日期,  
invitationDate X日清除一次
#### TABLE : manager 管理員
userId 用戶id,  
userName 用戶名稱,  
useGroupTitle 使用的群組名稱,  
useGroupId 使用的群組id,  
isManager 判斷是否為管理員
#### TABLE : lastGroupMessageId 紀錄最後訊息id
groupId 群組id,  
lastMessageId 訊息id
#### TABLE : joinGroup 機器人管理的群組
userId 用戶id,  
userName 用戶名稱,  
groupId 群組id,  
groupTitle 群組名稱,  
link 邀請連結
#### TABLE : joinChannel 機器人管理的頻道
userId 用戶id,  
userName 用戶名稱,  
channelId 頻道id,  
channelTitle 頻道名稱,  
link 邀請連結
#### TABLE : inviteToMakeMoney 邀請好友賺獎金( 邀请6位成员，赚取1.2元未结算，已经结算0元，满100元请联系@xx结算。)
userId 用戶id,  
userName 用戶名稱,  
groupId 群組id,  
groupTitle 群組名稱,  
beInvited 被邀請人JSON,  
outstandingAmount 未結算金額,  
settlementAmount 總結算金額
#### TABLE : joinGroupRecord 入群紀錄
userId 用戶id,  
userName 用戶名稱,  
groupId 群組id,  
groupTitle 群組名稱,  
invite 邀請人,  
joinGroupTime 入群時間



## 功能進度
- [ ] 设置每天禁言时间  
- [x] 删除指定时间内的重复发言，设置间隔时间发广告。  
- [x] 设置邀请指定人数后才能发言,设置几天数为一个周期。 您@用户：您需要邀请2位好友后可以正常发言  
- [x] 设置关注指定频道成员才能发言。没有达标甚至提醒内容。 您@用户：您需要关注频道 @xx 后可以正常发言  
- [ ] 分析当日，昨天新进成员 流失成员，被邀请成员，活跃度成员  
- [x] 增加提示信息控制 xx秒自动删除掉  
