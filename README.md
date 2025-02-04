Python Codes - Edge Computing & Data Logging from MQTT

Overview
This repository contains Python scripts designed for edge computing, data acquisition, and storage. The scripts facilitate:
Receiving data from end nodes and storing it in an in-house MongoDB.
Fetching data from MQTT topics and storing it in a .xls file.
Receiving data from multiple MQTT topics and logging it in .csv format.

Folder Structure

python-codes/
│── edge_to_mongodb.py       # Stores end-node data in MongoDB
│── mqtt_to_xls.py           # Logs MQTT data into an Excel file
│── mqtt_to_csv.py           # Logs MQTT data into a CSV file
│── README.md                # Project documentation

Scripts Description

1. edge_to_mongodb.py

This script:
Receives data from edge nodes.
Stores the data in an in-house MongoDB database.
Provides robust logging and error handling.
Usage:
python edge_to_mongodb.py

2. mqtt_to_xls.py

This script:
Connects to an MQTT broker.
Subscribes to specified topics.
Logs the received messages into an Excel (.xls) file.
Usage:
python mqtt_to_xls.py -H <broker_ip> -p <port> -t <topic> -u <username> -P <password>

3. mqtt_to_csv.py
This script:
Subscribes to multiple MQTT topics.

Receives and logs data into a CSV file.
Appends timestamps to each entry for tracking.
Usage:
python mqtt_to_csv.py -H <broker_ip> -p <port> -t <topic1> <topic2> -u <username> -P <password>

Requirements
Ensure you have the following dependencies installed:
pip install paho-mqtt pymongo openpyxl

Configuration
Modify the broker address, database credentials, and file paths in each script as required.

Contributions
Feel free to fork this repository and submit pull requests for enhancements.

