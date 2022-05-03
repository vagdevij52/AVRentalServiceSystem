from __future__ import print_function

import time

from pymongo import MongoClient
import json
from pathlib import Path


# ++++++++++++++++++++++++++++++++++++++Mongo DB+++++++++++++++++++#
while True:
    # code goes here
    client = MongoClient(
        "mongodb+srv://root:root1234@cluster1.ssmqr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('sensor_frame_data')
    # print(client.list_database_names())

    client = MongoClient(
            "mongodb+srv://root:root1234@cluster1.ssmqr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('sensor_frame_data')
        # print(client.list_database_names())
    records = db.LiveSensorData

        # Created or Switched to collection names: my_gfg_collection
    sensorData = Path("C:\Apps\CARLA_0.9.13\WindowsNoEditor\PythonAPI\examples\sensorData\data.json")
    if sensorData.is_file():
        sensorInfo = []

        print("Started Reading JSON file which contains multiple JSON document")
        with open("C:\Apps\CARLA_0.9.13\WindowsNoEditor\PythonAPI\examples\sensorData\data.json", 'r') as f:
            for frame in f:
                sensorDict = json.loads(frame)
                sensorInfo.append(sensorDict)


        # with open("/opt/carla-simulator/PythonAPI/examples/sensorData/data.json") as file:
        #     file_data = json.load(file)
        # for frame in open("/opt/carla-simulator/PythonAPI/examples/sensorData/data.json",'r'):
        #     sensorInfo.append(json.loads(frame))

        if isinstance(sensorInfo, list):
            # records.delete_many({})
            records.insert_many(sensorInfo)
        else:
            records.insert_one(sensorInfo)

        print("uploaded live data ")

    time.sleep(5)

