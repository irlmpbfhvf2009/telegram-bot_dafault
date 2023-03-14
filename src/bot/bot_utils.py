from src.common.utils import Logging
import datetime,time,json

class BotUtils():
    def setLogger():
        return  Logging(logger_level='DEBUG',file='log/'+str(datetime.datetime.now().date())+'.log')