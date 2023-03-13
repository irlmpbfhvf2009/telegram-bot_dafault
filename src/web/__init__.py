import os,sys
from flask import Flask, render_template, jsonify, request
from gevent.pywsgi import WSGIServer
import mimetypes
from src.common.utils import Log
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

class App():
    def __init__(self,port):
        resourcesDir = '../../resources'
        templatesDir = '../../resources/templates'
        staticDir = '../../resources/static'

        if getattr(sys, 'frozen', False):
            template_folder = os.path.join(sys.executable, resourcesDir, 'templates')
            static_folder = os.path.join(sys.executable, resourcesDir, 'static')
            self.app = Flask(__name__, template_folder=template_folder,
                        static_folder=static_folder)
        else:
            self.app = Flask(__name__, template_folder=templatesDir,static_folder=staticDir)
            
        @self.app.route("/")
        async def index():
            return render_template(r'index.html')
        
        @self.app.route("/getLogList", methods=['get'])
        async def getLogList():
            return jsonify({'log': Log()._log['log_list']})
            
        @self.app.route("/getConfig", methods=['get'])
        async def getConfig():
            return jsonify({'botusername': 0,})
            # return jsonify({'botusername': sql.botusername,
            #                 'password': sql.password,
            #                 'inviteFriendsAutoClearTime': sql.inviteFriendsAutoClearTime,
            #                 'inviteFriendsSet': sql.inviteFriendsSet,
            #                 'followChannelSet': sql.followChannelSet,
            #                 'inviteFriendsQuantity': sql.inviteFriendsQuantity,
            #                 'deleteSeconds': sql.deleteSeconds,
            #                 'invitationBonusSet': sql.invitationBonusSet,
            #                 'inviteMembers': sql.inviteMembers,
            #                 'inviteEarnedOutstand': sql.inviteEarnedOutstand,
            #                 'inviteSettlementBonus': sql.inviteSettlementBonus,
            #                 'contactPerson': sql.contactPerson})


        @self.app.route("/editInviteFriends", methods=['post'])
        async def editInviteFriends():
            # sql.editInviteFriends(
            #     "False") if sql.inviteFriendsSet == "True" else sql.editInviteFriends("True")
            # string = "關閉[邀請好友限制發言]" if sql.inviteFriendsSet == "True" else "開啟[邀請好友限制發言]"
            # code = 0 if sql.inviteFriendsSet == "True" else 1
            # return jsonify({'code': code, 'msg': string})
            return jsonify({'code': 0, 'msg': '0'})

        @self.app.route("/editFollowChannel", methods=['post'])
        async def editFollowChannel():
            #sql.editFollowChannel(
            #    "False") if sql.followChannelSet == "True" else sql.editFollowChannel("True")
            #string = "關閉[關注頻道限制發言]" if sql.followChannelSet == "True" else "開啟[關注頻道限制發言]"
            #code = 0 if sql.followChannelSet == "True" else 1
            #return jsonify({'code': code, 'msg': string})
            return jsonify({'code': 0, 'msg': '0'})

        @self.app.route("/editPassword", methods=['post'])
        async def editPassword():
            try:
                #sql.editPassword(request.get_json()['password'])
                return jsonify({'code': 1,'msg':'修改成功'})
            except Exception as e:
                return jsonify({'code': 0,'msg':str(e)})

        @self.app.route("/editContactPerson", methods=['post'])
        async def editContactPerson():
            try:
                #sql.editContactPerson(request.get_json()['contactPerson'])
                return jsonify({'code': 1,'msg':'修改成功'})
            except Exception as e:
                return jsonify({'code': 0,'msg':str(e)})

        @self.app.route("/editInviteFriendsQuantity", methods=['post'])
        async def editInviteFriendsQuantity():
            try:
                #sql.editInviteFriendsQuantity(request.get_json()['inviteFriendsQuantity'])
                return jsonify({'code': 1,'msg':'修改成功'})
            except Exception as e:
                return jsonify({'code': 0,'msg':str(e)})

        @self.app.route("/editInviteFriendsAutoClearTime", methods=['post'])
        async def editInviteFriendsAutoClearTime():
            try:
                #sql.editInviteFriendsAutoClearTime(request.get_json()['inviteFriendsAutoClearTime'])
                return jsonify({'code': 1,'msg':'修改成功'})
            except Exception as e:
                return jsonify({'code': 0,'msg':str(e)})

        @self.app.route("/editDeleteSeconds", methods=['post'])
        async def editDeleteSeconds():
            try:
                #sql.editDeleteSeconds(request.get_json()['deleteSeconds'])
                return jsonify({'code': 1,'msg':'修改成功'})
            except Exception as e:
                return jsonify({'code': 0,'msg':str(e)})
        
        http_server = WSGIServer(('127.0.0.1', port), self.app)
        print(f"* Running on http://{http_server.address[0]}:{http_server.address[1]}")
        http_server.serve_forever()