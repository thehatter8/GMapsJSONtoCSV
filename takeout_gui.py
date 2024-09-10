import os
import json
import csv
import timeit
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys


class JSONtoCSVApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.base_dir = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("JSON to CSV Converter")
        self.setGeometry(300, 300, 400, 300)

        layout = QtWidgets.QVBoxLayout()

        # Folder selection
        self.folder_label = QtWidgets.QLabel("Select Base Directory:")
        self.folder_button = QtWidgets.QPushButton("Browse")
        self.folder_button.clicked.connect(self.browse_folder)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_button)

        # Process indicators
        self.steps = ["Combine JSON", "Separate Lat-Long", "Remove Duplicates"]
        self.labels = []
        for step in self.steps:
            hbox = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(step)
            icon = QtWidgets.QLabel()
            icon.setPixmap(QtGui.QPixmap("red_x.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio))
            self.labels.append(icon)
            hbox.addWidget(label)
            hbox.addWidget(icon)
            layout.addLayout(hbox)

        # Start button
        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self.run_process)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def browse_folder(self):
        self.base_dir = QFileDialog.getExistingDirectory(self, "Select Base Directory")
        if self.base_dir:
            self.folder_label.setText(f"Selected Directory: {self.base_dir}")
            self.start_button.setEnabled(True)

    def run_process(self):
        # Base directory paths and output file paths
        combined_json_file = os.path.join(self.base_dir, 'PrimaryOutput.json')
        latlong_csv = os.path.join(self.base_dir, 'latlongdata.csv')
        specific_locations_csv = os.path.join(self.base_dir, 'specific_locations.csv')
        latlong_no_duplicates_csv = os.path.join(self.base_dir, 'latlongdata_no_duplicates.csv')

        # Timer start
        start = timeit.default_timer()

        # Step 1: Combine JSON files into one
        combined_data = []
        for root, dirs, files in os.walk(self.base_dir):
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

        # Update icon to green checkmark
        self.labels[0].setPixmap(QtGui.QPixmap("green_check.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio))
        QtWidgets.QApplication.processEvents()

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
                                latlong_data.append([latitudeE7 / 1e7, longitudeE7 / 1e7])

                            if placeId and address:
                                specific_locations_data.append([placeId, address])

        with open(latlong_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Latitude', 'Longitude'])
            writer.writerows(latlong_data)

        with open(specific_locations_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['PlaceId', 'Address'])
            writer.writerows(specific_locations_data)

        # Update icon to green checkmark
        self.labels[1].setPixmap(QtGui.QPixmap("green_check.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio))
        QtWidgets.QApplication.processEvents()

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

        # Update icon to green checkmark
        self.labels[2].setPixmap(QtGui.QPixmap("green_check.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio))
        QtWidgets.QApplication.processEvents()

        # Timer stop
        stop = timeit.default_timer()
        runtime = stop - start

        # Show success popup
        QMessageBox.information(self, "Success", f"Process completed successfully!\nRuntime: {runtime:.2f} seconds")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = JSONtoCSVApp()
    window.show()
    sys.exit(app.exec_())
