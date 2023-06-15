import time

class classlog():
    def __init__(self,classname):
        self.date=time.strftime("%Y-%m-%d", time.localtime())
        self.LogPath=f"Log/{self.date}-{classname}log.log"
        self.file = open(self.LogPath, 'a', encoding="utf-8")
        self.log("====================================================================")
        self.log("NEW INSTANCE RUNNING")
    
    def log(self,msg):
        self.file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + msg +"\n")
        self.file.flush()