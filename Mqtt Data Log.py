# This script enables the user to fetch data from a MQTT and store it in local as .xls file 
# Script Owner & creator : Kiran Kumar N 

import paho.mqtt.client as mqtt
import xlwt
import xlrd
from datetime import datetime
import os

# Configuration - Replace these values with your actual settings
MQTT_BROKER_IP = "your.broker.ip"     # MQTT broker IP address
MQTT_PORT = 1883                      # MQTT broker port
MQTT_TOPIC = "your/data/topic"        # Topic to subscribe to
EXCEL_FILE = "received_data.xls"      # Output Excel file name

existing_data = []

# Initialize or load existing Excel data
if os.path.exists(EXCEL_FILE):
    try:
        workbook = xlrd.open_workbook(EXCEL_FILE)
        sheet = workbook.sheet_by_index(0)
        for row_idx in range(sheet.nrows):
            existing_data.append(sheet.row_values(row_idx))
    except Exception as e:
        print(f"Error reading existing file: {e}")
        existing_data = [["Timestamp", "Message"]]
else:
    existing_data = [["Timestamp", "Message"]]

def write_to_excel(data):
    """Writes all data to the Excel file"""
    try:
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("MQTT Data")
        
        # Write all rows
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                sheet.write(row_idx, col_idx, value)
        
        workbook.save(EXCEL_FILE)
        print(f"Data successfully written to {EXCEL_FILE}")
    except Exception as e:
        print(f"Error writing to Excel: {e}")

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        payload = msg.payload.decode("utf-8")
        print(f"Received message: {payload}")
        
        # Add new entry to data
        existing_data.append([timestamp, payload])
        
        # Update Excel file
        write_to_excel(existing_data)
    except Exception as e:
        print(f"Error processing message: {e}")

# MQTT Client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(MQTT_BROKER_IP, MQTT_PORT, 60)
except Exception as e:
    print(f"Connection error: {e}")
    exit(1)

print(f"Listening for messages on topic '{MQTT_TOPIC}'...")
client.loop_forever()
