from datetime import datetime
from multiprocessing import Pool
import requests
import time
import pandas as pd

def APICalling(i):
    t = datetime.now()
    r = requests.get("https://ifconfig.co/")
    print(f"Call: {i} // Response: {r}, Time Stamp: {t}")

# Use this if they gave you a real csv
# timestamps = pd.read_csv("your_csv_file_here.csv")

# For demonstration I am going to ignore it and use the data provided as a list.

timestamps = ["20:07:30","20:07:30","20:07:30","20:07:30","20:07:30",]
# timestamps = ["09:15:25","11:58:23","13:45:09","13:45:09","13:45:09","17:22:00","17:22:00"]

calls_to_make = {}

for item in timestamps:
    try:
        calls_to_make[item] += 1
    except:
        calls_to_make[item] = 1

print(calls_to_make)

print(list(calls_to_make.keys()))

# This is the first entry in the timestamp list.
# It is acting like a pointer.
#This method assumes your list is sorted, if not a sort function should be added.
next_call_time = 0

script_start_time = datetime.now().strftime("%H:%M:%S")

while next_call_time < len(list(calls_to_make.keys())):
    current_time = str(datetime.now().strftime("%H:%M:%S"))
    print(current_time)
    if current_time == list(calls_to_make.keys())[next_call_time]:
        p = Pool(calls_to_make[current_time])
        p.map(APICalling, range(calls_to_make[current_time]))
        time.sleep(1)
    else:
        time.sleep(1)
