import files

fm = files.Filemanager()
encryption = files.Encryption()

data = []
fnames = ['column1', 'column2', 'column3']

data1 = {'column1': 'data11', 'column2': 'data12', 'column3': 'data13'}
data2 = {'column1': 'data21', 'column2': 'data22', 'column3': 'data23'}
data.append(data1)
data.append(data2)

fm.saveFile('_2020_february.csv', fnames, data)
files = fm.listDirectory()
for f in files:
    print(f)

data = fm.loadFile("_2020_february.csv")
for row in data:
    print(row)
