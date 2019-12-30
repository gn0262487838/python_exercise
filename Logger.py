import logging
import getpass
import os 

'''

客制一個通用的logger，以方便記錄。

'''
class Logger(object):

    """
    ::param FILENAME:str
        if you have idea for filename , then fill in.
    
    ::method debug(message:str)
        logging level 10

    ::method info(message:str)
        logging level 20

    ::method warning(message:str)
        logging level 30

    ::method error(message:str)
        logging level 40

    ::method critical(message:str)
        logging level 50

        ::method setLevel(level)
        if `logging level` than `level`,then show stdout on console.
        example:
                > Logger = Logger()
                > Logger.setLevel(logging.INFO)
                > Logger.debug("it's good")
                
                > Logger.info("come on")
                  "come on"

    ::method disable(message:str)
        only use formal env.
        this function has hide all stdout. 
    
    ::method Close(message:str)
        remove handler, flush and close.

    """
    def __init__(self, FILENAME=None):

        # get user's name
        self.USERNAME = getpass.getuser()
        # set file name
        self.FILENAME = self.USERNAME if FILENAME == None else FILENAME 
        # set path
        self.path = "\\LOG\\"
        if not os.path.isdir(self.path): 
            os.mkdir(self.path)
        # set stdout
        self.FORMAT = "%(asctime)s %(levelname)s %(name)s %(thread)d %(message)s"
        
        # build user's logger
        self.logger = logging.getLogger(self.USERNAME)
        # build user's formatter
        self.formatter = logging.Formatter(self.FORMAT)
        # build user's streamhandler(整流物件其功用是輸出到console)
        self.streamhandler = logging.StreamHandler()
        # build user's filehandler(整流物件其功用是輸出到file)
        self.filehandler = logging.FileHandler(self.path + self.FILENAME + ".log")
        
        # set parameters
        self.streamhandler.setFormatter(self.formatter)
        self.filehandler.setFormatter(self.formatter)
        self.logger.setLevel(logging.DEBUG)  # 低於此等級就不輸出...
        self.logger.addHandler(self.streamhandler)
        self.logger.addHandler(self.filehandler)
    
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        # 參數exc_info可幫助紀錄錯誤訊息，在try except上很好用。
        self.logger.error(msg, exc_info=True)

    def critical(self, msg):
        self.logger.critical(msg)

    def setLevel(self, level):
        self.logger.setLevel(level)

    def diable(self, levelNum=None):
        # 以往在開發時，需要在一些地方紀錄log，開發完成後就要去刪除那些指令。
        # 使用disable即可不必刪除那些指令且console也不會輸出log紀錄喔~
        if levelNum == None:
            levelNum = 50

        logging.disable(levelNum)

    def Close(self):
        self.logger.removeHandler(self.streamhandler)
        self.logger.removeHandler(self.filehandler)
        self.streamhandler.flush()
        self.filehandler.flush()
        self.streamhandler.close()
        self.filehandler.close()

if __name__=="__main__":
    pass
