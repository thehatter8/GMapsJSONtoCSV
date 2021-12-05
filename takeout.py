import pandas as pd
import json
import csv
import os

for file in os.listdir('C:\\SOME FOLDER\\Takeout\\Location History\\Semantic Location History\\all'):
    jsonFile = f"C:\\SOME FOLDER\\Takeout\\Location History\\Semantic Location History\\all\\{file}"
    with open(jsonFile, 'r') as f:
        data = json.load(f)
    features = []
    for obj in data:
        for item in enumerate(data[obj]):
            try:
                latitudeE7 = int(item[1]['placeVisit']['location']['latitudeE7'])
                longitudeE7 = int(item[1]['placeVisit']['location']['longitudeE7'])
                latitude = latitudeE7/10000000
                longitude = longitudeE7/10000000
                features.append({'latitude':latitude,'longitude':longitude})
            except:
                print('--')

    fields = ['latitude','longitude']
    with open('C:\\SOME FOLDER\\output.csv', 'a', newline='') as testFile:
        writer = csv.DictWriter(testFile, fieldnames=fields)
        writer.writeheader()
        for loc in features:
            writer.writerow(loc)
testFile.close()
