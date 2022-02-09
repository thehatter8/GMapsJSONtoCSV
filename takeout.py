import timeit
import json
import csv
import os

start = timeit.default_timer()
maindir = '{SOMEFOLDER}\\Takeout\\Location History\\Semantic Location History\\'
features = []
for folder in os.listdir(maindir):
    jsonFileList = os.listdir(maindir+folder)
    for jsonFile in jsonFileList:
        with open(maindir+folder+"\\"+str(jsonFile), 'r', encoding="utf8") as f:
            data = json.load(f)
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
    #line below is probably why/how I get dupes. Need to figure out better placement so it doesn't run every single loop.
    with open('{SOMEDIR}\MapProject\\outputWithDupes.csv', 'a', newline='') as testFile:
        writer = csv.DictWriter(testFile, fieldnames=fields)
        writer.writeheader()
        for loc in features:
            writer.writerow(loc)
testFile.close()
with open('{SOMEDIR}\\MapProject\\outputWithDupes.csv', 'r') as in_file, open('{SOMEDIR}\\MapProject\\finalNoDupes.csv','w') as out_file:
    seen = set()
    for line in in_file:
        if line in seen: continue
        seen.add(line)
        out_file.write(line)
stop = timeit.default_timer()
print('Runtime: ', stop - start) 
