#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class MongoClass:
    MONGO_HOST = 'mongodb://timber_mongodb_1'
    MONGO_PORT = 27017
    MONGO_DB = 'primedb'
    MONGO_CLIENT = object()
    MONGO_DB_OBJ = object()

    def __init__(self):
        print ('Connecting to mongodb...')
        self.MONGO_CLIENT = MongoClient(self.MONGO_HOST, self.MONGO_PORT)
        # self.MONGO_CLIENT = MongoClient()
        self.MONGO_DB = self.MONGO_CLIENT[self.MONGO_DB]

    def insert_one(self, postObj):
        return self.MONGO_DB.insert_one(postObj)

    def close_connection(self):
        print ('disconnecting from mongodb...')
        self.MONGO_CLIENT.close()