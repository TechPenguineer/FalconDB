from genericpath import exists
import platform
import os
OS = platform.system()

Collection_Model = {
    "Name",
    "Id",
    "Timestamp"
}
class Collection:
    def CreateParentDir():
        COL_DIR = Collection.FindEnvData()+"\\.FalconDB"
        if not dir.exists(COL_DIR):
            os.mkdir(COL_DIR)
    def FindEnvData():
        if OS == "Windows":
            return os.getenv("APPDATA")
    def CreateCollection(collection_name):
            ENV = Collection.FindEnvData()
            Collection.CreateParentDir()
            collection_path=Collection.FindEnvData()+"\\.FalconDB\\"+collection_name
            COLLECTION_FOLDER = os.mkdir(collection_path, "rw")
            

            
            
Collection.CreateCollection()
    