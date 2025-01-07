## data to csv
import os
import csv
import json
import sys
import logging


generation_name = "dynamic.csv"
os.system("touch " + generation_name)



with open(generation_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Thing", "Thing", "Thing"])

    
    data = [
        {"ID": 1, "Name": "Thing", "Thing": 0},
        {"ID": 2, "Name": "Thing", "Thing": 0},
        {"ID": 3, "Name": "Thing", "Thing": 0}
    ]

    
    for row in data:
        writer.writerow(list(row.values()))