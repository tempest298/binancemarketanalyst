class CacheDatabase:
    __instance = None
    @staticmethod
    def getInstance():
        if CacheDatabase.__instance == None:
            CacheDatabase()
        return CacheDatabase.__instance
    def __init__(self):
        if CacheDatabase.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CacheDatabase.__instance = self
            self.Database = {}
    def getDatabase(self):
        return self.Database
    def setObject(self,Key,Object):
        if(isinstance(Key,str)):
            self.Database[Key] = Object
        else:
            raise Exception("Key parameter should be an instance of String at setObject function.")
    def getObject(self,Key):
        if(isinstance(Key,str)):
            return self.Database[Key]
        else:
            raise Exception("Key parameter should be an instance of String at setObject function.")
            return False
    def isKeySet(self,Key):
        try:
            test = self.Database[Key]
            return True
        except KeyError as KE:
            return False
    def removeKey(self,Key): ##check
        try:
            del self.Database[Key]
            return True
        except:
            return False #Key is not set.