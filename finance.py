import files

fm = files.Filemanager()
encryption = files.Encryption()

fm.saveFile('_2020_february.csv', '22')
files = fm.listDirectory()
for f in files:
    print(f)

data = fm.loadFile("_2020_february.csv")
for row in data:
    print(row)
