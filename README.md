# GMapsJSONtoCSV
Converts Google Takeout historical data for Google Maps from JSON to 2-column CSV with long/latitude

## Downloading your Takeout data

1. Visit takeout.google.com
2. Scroll down or search for 'Location History'
3. Under 'Multiple File Types' ensure 'JSON' is selected
4. Click through the next few steps, receive the email from Google (or directly download depending on file size), download the data


## Setup

1. Extract the .zip (etc) file to any location
2. Have the folder setup something like the following:
``C:\Users\yourname\\Documents\\Takeout\\Location History\\Semantic Location History\\2021`` etc
4. Update {SOMEDIR} within the code to your file location. This may be in your Documents as suggested, or anywhere else you may want to do this.
5. Choose an output location for the csv file by updating the {SOMEDIR} field
6. Run the script
7. Do something cool with the data or don't
