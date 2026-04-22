

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        #USER = 'aacuser' 
        #PASS = 'SNHU123' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        #
        try:
            #
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            #self.client = MongoClient('mongosh -u "aacuser" -p "SNHU123" --authenticationDatabase "admin"')
            self.database = self.client['%s' % (DB)] 
            self.collection = self.database['%s' % (COL)]
            print("Connection successful")
        except errors.ConnectionError as e:
            print("Could not connect to Database")

    # Create a method to return the next available record number for use in the create method
            
    # Create method in CRUD. 
    def create(self, data):
        if data is not None: 
            createData = self.database.animals.insert_one(data)  # data should be dictionary
            return createData.acknowledged
            #Checks if creation was succesful
            if createData == 0:
                return True
            return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Read method in CRUD.
    def read(self, query):#query is data being queried
        if query is not None:
            readData = self.database.animals.find(query)
            result = list(readData)
            return result
        else:
            raise Exception("Nothing to read, query parameter is empty")
            return list()
        
    # Update method in CRUD
    def update(self, oldData, newData):
        if oldData and newData is not None:
            updatedData = self.database.animals.update_many(oldData, {"$set": newData})
        else:
            raise Exception("Nothing to update, data parameter is empty")
        return updatedData
    
    # Delete method in CRUD
    def delete(self, data):
        if data is not None:
            deletedData = self.database.animals.delete_many(data)
        else:
            raise Exception("Nothing to update, data parameter is empty")
        return deletedData.deleted_count