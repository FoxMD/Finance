import os
import csv

class Filemanager:
    root_dir = "./database/"

    def listDirectory(self):
        file_set = set()
        for dir_, _, files in os.walk(self.root_dir):
            for file_name in files:
                rel_dir = os.path.relpath(dir_, self.root_dir)
                rel_file = os.path.join(file_name)
                file_set.add(rel_file)
            return file_set

    def saveFile(self, filename, df):
        fnames = ['column1', 'column2', 'column3']
        data = []

        data1 = {'column1': 'data11', 'column2': 'data12', 'column3': 'data13'}
        data2 = {'column1': 'data21', 'column2': 'data22', 'column3': 'data23'}
        data.append(data1)
        data.append(data2)

        with open(self.root_dir + filename, 'w', encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fnames)
            writer.writeheader()
            for line in data:
                writer.writerow(line)


    def loadFile(self, filename):
        data = []
        with open(self.root_dir + filename, 'r', encoding="utf-8", newline="") as file:
            df = csv.reader(file, delimiter=',', quotechar='|')
            for row in df:
                data.append(row)

        return data
