import socket,os,logging,datetime
import tkinter

class Logger(logging.Logger):
    def __init__(self,
                 name='root',
                 logger_level= None,
                 file=None,
                #  guiFile=None,
                 logger_format = " [%(asctime)s]  %(levelname)s %(filename)s [ line:%(lineno)d ] %(message)s"
                 ):
        super().__init__(name)

        self.logger = logging.getLogger(name)
        self.setLevel(logger_level)
        fmt = logging.Formatter(logger_format)
        
        if file:
            file_handler = logging.FileHandler(file,'a','utf-8')
            file_handler.setLevel(logger_level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # if guiFile:
        #     gui_file_handler = logging.FileHandler(guiFile,'a','utf-8')
        #     gui_file_handler.setLevel(logger_level)
        #     gui_file_handler.setFormatter(fmt)
        #     self.addHandler(gui_file_handler)

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logger_level)
        self.stream_handler.setFormatter(fmt)
        self.addHandler(self.stream_handler)
        

class DirsUtils():
    def __init__(self):
        self.initalizeProjectDirectory = self.createInitialFolder()
        self.currentPath = self.currentDirectory()
        
    def makedirs(self,path=None):
        if not os.path.isdir(path):
            return os.makedirs(path, mode=511, exist_ok=False)

    # 當前目錄
    def currentDirectory(self):
        # return os.path.abspath(os.path.dirname(__file__)) #當前檔案位置
        return os.getcwd().replace('\\','/') 

    # 上級目錄
    def parentDirectory():
        return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # 上上級目錄
    def doubleParentDirectory():
        return os.path.abspath(os.path.join(os.getcwd(), "../.."))
    
    # 初始化專案目錄
    def createInitialFolder(self):
        currentPath = self.currentDirectory() + '/log'
        self.makedirs(path=currentPath)

class CheckPort():
    def chick_port(port=None, host='127.0.0.1'):
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((host, int(port)))
            return True
        except socket.error:
            return False
        finally:
            if s:
                s.close()


class ReadLog:
    def __init__(self):
        self._log=self.get_log()
    
    def find_new_log(self):
        dir = os.path.abspath(os.getcwd())+"\log"
        file_lists = os.listdir(dir)
        file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
                    if not os.path.isdir(dir + "\\" + fn) else 0)
        log = os.path.join(dir, file_lists[-1])
        return log

    def red_logs(self):
        log_path = self.find_new_log()
        with open(log_path,'rb') as f:
            log_size = os.path.getsize(log_path) 
            offset = -100
            if log_size == 0:
                return ''
            while True:
                if (abs(offset) >= log_size):
                    f.seek(-log_size, 2)
                    data = f.readlines()
                    return data
                data = f.readlines()
                if (len(data) > 1):
                    return data
                else:
                    offset *= 2

    def get_log(self):
        line_number = [0]
        try:
            log_data = self.red_logs()
        except:
            return {'log_list' : ''}

        if len(log_data) - line_number[0] > 0:
            log_difference = len(log_data) - line_number[0]
            log_list = []
            for i in range(log_difference):
                log_i = log_data[-(i+1)].decode('utf-8')
                log_list.insert(0,log_i)
        _log = {
            'log_list' : log_list
        }
        line_number.append(len(log_data))
        return _log
    
DirsUtils().initalizeProjectDirectory
logger = Logger(logger_level='DEBUG',file='log/'+str(datetime.datetime.now().date())+'.log')
