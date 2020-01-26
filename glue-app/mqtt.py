#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime
import paho.mqtt.client as mqtt
import pymongo

mongoObj= object()
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/t/primenumber")
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = msg.payload 
    print(msg.topic+" "+str(payload))
    jsonData = json.loads(payload)
    now = datetime.now()
    jsonData.update({'date': now.strftime("%d/%m/%Y %H:%M")}) 
    

    print ('Connecting to mongodb...')
    myclient = pymongo.MongoClient("mongodb://virtualization:virtualization@localhost:27017/")
    mydb = myclient["primedb"]
    mycol = mydb["primecollection"]
    print ('Inserting Data..')
    print(mycol.insert_one(jsonData).inserted_id)
    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
