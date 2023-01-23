import csv

class DataStorage:
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def save_data(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.data:
                writer.writerow(row)
