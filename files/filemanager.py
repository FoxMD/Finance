import os
import csv
import files

class Filemanager:
    root_dir = "./database/"
    encryption = files.Encryption()

    def listDirectory(self):
        file_set = set()
        for dir_, _, files in os.walk(self.root_dir):
            for file_name in files:
                rel_dir = os.path.relpath(dir_, self.root_dir)
                rel_file = os.path.join(file_name)
                file_set.add(rel_file)
            return file_set

    def saveFile(self, filename, header, df):
        with open(self.root_dir + filename, 'w', encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.encryption.cryptHeader(header))
            writer.writeheader()
            for line in df:
                writer.writerow(self.encryption.cryptFile(line))


    def loadFile(self, filename):
        data = []
        with open(self.root_dir + filename, 'r', encoding="utf-8", newline="") as file:
            df = csv.reader(file, delimiter=',', quotechar='|')
            for row in df:
                data.append(row)

        return data
