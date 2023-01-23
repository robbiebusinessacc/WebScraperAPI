import csv

class DataStorage:
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def to_csv(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.data)
