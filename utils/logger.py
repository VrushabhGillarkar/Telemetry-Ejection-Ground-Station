import csv
import os

class CSVLogger:
    def __init__(self, filename, headers=None):
        self.filename = filename
        self.headers = headers

        # Create folder if not exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # If file does not exist, create and write headers
        if headers and not os.path.exists(filename):
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

    def log_row(self, row):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
