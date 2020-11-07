import os


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
        with open(filename, 'w', encoding="utf-8", newline="") as file:
            pass

    def loadFile(self, filename):
        with open(filename, 'r', encoding="utf-8", newline="") as file:
            pass
