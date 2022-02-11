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


## Notes

* outputWithDupes will likely contain multiple of the same coordinate pairs. I did some looking into my own data and found that almost all the duplicate coordinates were either my place of work, my home, or friend's home. If you're making some sort of heatmap, this is probably the file you want to use.

* finalNoDupes removes any duplicate coordinate pairs. If you want to make a map of every county/state you've visited, this is probably the file you want to use.


## Next version

* I will likely make this script into an actual function instead of loose code
* I want to add integration with QGIS as well. The ideas I listed under Notes would be a cool thing to add to this script
