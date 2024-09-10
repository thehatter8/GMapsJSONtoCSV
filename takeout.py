import os
import json
import csv
import timeit


# Base directory paths and output file paths
base_dir = r'C:\\MapProject\\Location_History_Timeline\\Location_History'
combined_json_file = r'C:\\MapProject\\PrimaryOutput.json'
latlong_csv = r'C:\\MapProject\\latlongdata.csv'
specific_locations_csv = r'C:\\MapProject\\specific_locations.csv'
latlong_no_duplicates_csv = r'C:\\MapProject\\latlongdata_no_duplicates.csv'

# Step 0: Timer!!!!
start = timeit.default_timer()

# Step 1: Combine JSON files into one
combined_data = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        combined_data.extend(data)
                    elif isinstance(data, dict):
                        combined_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file: {file_path} - {e}")

with open(combined_json_file, 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)

print(f"Combined JSON data saved to {combined_json_file}")

# Step 2: Separate into lat-long and specific locations
latlong_data = []
specific_locations_data = []

with open(combined_json_file, 'r') as infile:
    data = json.load(infile)
    
    for item in data:
        if "timelineObjects" in item:
            for obj in item["timelineObjects"]:
                if "placeVisit" in obj:
                    location = obj["placeVisit"].get("location", {})
                    
                    latitudeE7 = location.get("latitudeE7")
                    longitudeE7 = location.get("longitudeE7")
                    placeId = location.get("placeId")
                    address = location.get("address")
                    
                    if latitudeE7 and longitudeE7:
                        latlong_data.append([latitudeE7 / 1e7, longitudeE7 / 1e7])  # Convert to normal latitude/longitude

                    if placeId and address:
                        specific_locations_data.append([placeId, address])

with open(latlong_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Latitude', 'Longitude'])  # CSV header
    writer.writerows(latlong_data)

with open(specific_locations_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['PlaceId', 'Address'])  # CSV header
    writer.writerows(specific_locations_data)

print(f"Latitude and longitude data saved to {latlong_csv}")
print(f"Place ID and address data saved to {specific_locations_csv}")

# Step 3: Remove duplicates from the lat-long CSV
unique_latlongs = set()
cleaned_data = []

with open(latlong_csv, 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    cleaned_data.append(header)
    
    for row in reader:
        latlong_tuple = (float(row[0]), float(row[1]))
        if latlong_tuple not in unique_latlongs:
            unique_latlongs.add(latlong_tuple)
            cleaned_data.append(row)

with open(latlong_no_duplicates_csv, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(cleaned_data)

print(f"Data without duplicates saved to {latlong_no_duplicates_csv}")

# Step ???: TIMER!!!!!
stop = timeit.default_timer()
print('Runtime: ', stop - start) 
