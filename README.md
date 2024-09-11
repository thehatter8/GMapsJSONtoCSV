# GMapsJSONtoCSV
Converts Google Takeout historical data for Google Maps from JSON to 2-column CSV with long/latitude

## Try the new takeout_gui.py!! (ignore all warnings)

## Downloading your Takeout data

1. Visit takeout.google.com
2. Scroll down or search for 'Location History'
3. Under 'Multiple File Types' ensure 'JSON' is selected
4. Click through the next few steps, receive the email from Google (or directly download depending on file size), download the data


## Setup

1. Extract the .zip (etc) file to any location
2. Have the folder setup something like the following:
``C:\\MapProject\whatever you want as long as it leads to Location History`` etc
    * Check the ```base_dir``` variable and either change your files to my folder layout or change my code to yours, I don't care.
    * Do (or don't) this for all the other variables at the top
3. Make sure your python environment has the right packages installed. I really hope you know how to do that if you're reading this.
4. Run the takeout.py script (or the fancy new takeout_gui.py!!)
5. Do something cool with the data or don't


## Notes

* latlongdata.csv will almost definitely contain multiple of the same coordinate pairs. I did some looking into my own data and found that almost all the duplicate coordinates were either my place of work, my home, or friend's home. If you're making some sort of heatmap, this is probably the file you want to use.

* latlongdata_no_duplicates removes any duplicate coordinate pairs. If you want to make a map of every county/state you've visited, this is probably the file you want to use.


## Next version

* I will die if I have to make another version of this
* Add integration with my CSVMappy Project. Maybe make it run in one script, idk
