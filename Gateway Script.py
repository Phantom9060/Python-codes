import os
import pymongo
import asyncio
import random
from paho.mqtt import client as mqtt_client
import time
from datetime import datetime
broker = 'IP address'
dbclient = pymongo.MongoClient("mongodb://")
db = dbclient["DBClient"]
col = db["Collection name"]
port = 1883
topic ='Topic'
mqttuser = 'username'
password = 'Password'
client_id = f'python-mqtt-{random.randint(0,100)}'
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Ready to receive data "+"\n")
        else:
            print("connection failed, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.username_pw_set(mqttuser, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata , msg):
        data1 = f"{msg.payload.decode('utf8')}"
        print(data1)
        data2 = str(data1)
        res = data2.find("|")
        if res == -1:
            index = data1.find("-")
            device_id = data2[0:index]
        else:
            ind = data1.find("-")
            index = data1.find("|")
            device_id = data2[0:ind]
        consumption = data2[index+1:]
        con= str(consumption)
        pub = float(con) #if the db is logging data in String comment this line         
        print("ID = ",device_id)
        print("consumption_value = ",pub)# if the db is logging data in Str put "con" instead of "pub" this line 
        mydict = { "device_id": device_id, "consumption":pub, "date": datetime.now()} #if the db is logging data in String at consumption use "con" instead of "pub" 
        x = col.insert_one(mydict)
        print(datetime.now())
        print("Record Successfully Inserted")
    client.subscribe(topic)
    client.on_message = on_message
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
if __name__=='__main__':
    run()
