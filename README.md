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
````C:\\Users\\yourname\\Documents\\Takeout\\```` where the first folder/file within ``Takeout`` is ``Location History`` and ``archive_browser.html``
3. Navigate to ````Takeout\\Location History\\Semantic Location History```` and note that the folders are all years. Copy the JSON files from each year into a new folder called ``all`` like this:

    ``Semantic Location History\\all\\2020_AUGUST.json``
    
    ``Semantic Location History\\all\\2021_MAY.json``, etc
4. Update the script to your file location
5. Choose an output location for the csv file
6. Run the script
7. Do something cool with the data or don't
