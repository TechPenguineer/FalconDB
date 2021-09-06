import platform
import os
OS = platform.system()

class Collection:
    def FindEnvData():
        if OS == "Windows":
            return os.getenv("APPDATA")
        
    def CreateCollection(args):
            ENV = Collection.FindEnvData()
            collection_path=Collection.FindEnvData()