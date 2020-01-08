import json
import pickle
from pymongo import MongoClient
import redis

    
class Storage:
    
    def __init__(self, data, protocol):
        self.data = data
        self.protocol = protocol
    
    def serialization(self):
        if self.protocol == 'json':
            return json.dumps(self.data)
        elif self.protocol == 'pickle':
            return pickle.dumps(self.data)
        else:
            raise ValueError("Wrong serialization protocol")

    def deserialization(self):
        if self.protocol == 'json':
            return json.loads(self.data)
        elif self.protocol == 'pickle':
            return pickle.loads(self.data)
        else:
            raise ValueError("Wrong serialization protocol")
            
    def get_data(self):
        pass
    
    def set_data(self):
        pass
            
    
class MongoStorage(Storage):
    def __init__(self, data, protocol, host="localhost", port=27017):
        super().__init__(data, protocol)
        self.client = MongoClient(host, port)
        self.db = self.client.test_database
        self.collection = self.db.test_collection
        self.deserial_data = self.deserialization()
        self.serial_data = self.serialization()
        
    def get_data(self):
        return self.collection.find({})
        
    def set_data(self):
        self.collection.insert_one(self.serial_data)
    

class RedisStorage(Storage):
    def __init__(self, data, protocol):
        super().__init__(data, protocol)
        self.r = redis.Redis()
        self.serial_data = self.serialization()
        self.deserial_data = self.deserialization()
        
    def get_data(self):
        return self.r.get('protocol'), self.r.get('data')
        
    def set_data(self):
        self.r.set('protocol' + self.protocol)
        self.r.set('data' + self.serial_data)
