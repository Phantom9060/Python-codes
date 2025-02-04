import os
import sys
import time
import argparse
import logging
import csv
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        for topic in args.topic:
            client.subscribe(topic, qos=0)  # Set QoS as needed (0, 1, or 2)
    else:
        print("Failed to connect to MQTT broker")

def on_message(client, userdata, msg):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    message = msg.payload.decode()
    log_data(timestamp, message)
    print("ready")

# make changes to be required as per the db logging
def log_data(timestamp, message):
    log_file = os.path.expanduser("path address/data_log.csv")
    with open(log_file, mode='a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([timestamp, message])
        print("write")     

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MQTT data logger")
    parser.add_argument("-H", "--host", default="ip address", help="MQTT broker host address")
    parser.add_argument("-p", "--port", default=1883, type=int, help="MQTT broker port number")
    parser.add_argument("-t", "--topic", nargs='+', default=["Topic1", "Topic2", "Topic3", "Topic4", "Topic5", "Topic6", "Topic7", "Topic8", "Topic9",  "Topic10", "Topic11", "Topic12", "Topic13", "Topic14", "Topic15", "Topic16", "Topic17", "Topic18", "Topic19", "Topic20" , "Topic21", "Topic22", "Topic23", "], help="List of MQTT topics to subscribe to")
    parser.add_argument("-u", "--username", default="", help="MQTT username")
    parser.add_argument("-P", "--password", default="", help="MQTT password")
    args = parser.parse_args()
    print("Process")

    # Setup logging as per your DB 
    log_file = os.path.expanduser("path address /data_log.csv")
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(message)s")
    print("set")

    # Setup MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    if args.username:
        client.username_pw_set(args.username, args.password)

    client.connect(args.host, args.port, 60)
    

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
        sys.exit(0)
