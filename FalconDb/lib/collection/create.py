from genericpath import exists
import platform
import os
from typing import Text
OS = platform.system()

Collection_Model = {
    "Name",
    "Id",
    "Timestamp"
}
class Collection:
    def CreateParentDir():
        COL_DIR = Collection.FindEnvData()+"\\FalconDB"
        if not exists(COL_DIR):
         os.mkdir(COL_DIR)
         print ("Created Datafolder")
    def FindEnvData():
        if OS == "Windows":
            return os.getenv("APPDATA")
    def CreateCollection(collection_name):
            nme = Text.lower(collection_name)
            ENV = Collection.FindEnvData()
            Collection.CreateParentDir()
            collection_path=Collection.FindEnvData()+"\\FalconDB\\"+nme
            print(collection_path)
            if not exists(collection_path):
                 COLLECTION_FOLDER = os.mkdir(collection_path)

            
            
Collection.CreateCollection("Turtles")
    