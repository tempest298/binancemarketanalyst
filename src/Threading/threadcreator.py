from threading import Thread
class ThreadHandler():
    def __init__(self,ThreadFunc,Args):
        self.ThreadInstance = Thread(target=ThreadFunc,args=(Args,))
        self.ThreadInstanceSet = True
        self.isThreadRunning = False
    def StartThread(self):
        if self.ThreadInstanceSet and self.isThreadRunning == False:
            self.ThreadInstance.start()
            return True
        else:
            print("Thread instance is not set or already started.")
            return False
    def GetThreadInstance(self):
        return self.ThreadInstance