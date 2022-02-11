import timeit
import json
import csv
import os

# Mostly for my own curiosity
start = timeit.default_timer()

# Set {SOMEDIR} As shown in README or set to a custom directory
maindir = '{SOMEDIR}\\Takeout\\Location History\\Semantic Location History\\'
features = []

# Gets list of years you have data for, and iterates through the months of each year
for folder in os.listdir(maindir):
    jsonFileList = os.listdir(maindir+folder)
    for jsonFile in jsonFileList:
        currentFile = maindir+folder+"\\"+str(jsonFile)
        with open(currentFile, 'r', encoding="utf8") as f:
            data = json.load(f)
        for obj in data:
            for item in enumerate(data[obj]):
                try:
                    latitudeE7 = int(item[1]['placeVisit']['location']['latitudeE7'])
                    longitudeE7 = int(item[1]['placeVisit']['location']['longitudeE7'])
                    # E7 here is Scientific notation for lat/long * 10^7, so this returns them to GPS coords
                    latitude = latitudeE7/10000000
                    longitude = longitudeE7/10000000
                    features.append({'latitude':latitude,'longitude':longitude})
                except:
                    print('Current item is not lat/long')

# Creates a CSV file which allows duplicate coordinates, which come from visiting the same location multiple times
fields = ['latitude','longitude']
with open('{SOMEDIR}\\outputWithDupes.csv', 'a', newline='') as testFile:
    writer = csv.DictWriter(testFile, fieldnames=fields)
    writer.writeheader()
    for loc in features:
        writer.writerow(loc)
testFile.close()

# Checks the previous CSV for duplicates and creates a new CSV without any duplicated coordinate pairs
with open('{SOMEDIR}\\outputWithDupes.csv', 'r') as in_file, open('{SOMEDIR}\\finalNoDupes.csv','w') as out_file:
    seen = set()
    for line in in_file:
        if line in seen: continue
        seen.add(line)
        out_file.write(line)
stop = timeit.default_timer()
print('Runtime: ', stop - start) 
