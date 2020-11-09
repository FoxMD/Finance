import files
import sys
from qtpy import QtWidgets

# QT with Cpp
app = QtWidgets.QApplication(sys.argv)

fm = files.Filemanager()
window = files.MainWindow()

window.show()

sys.exit(app.exec_())

'''
data = []
fnames = ['column1', 'column2', 'column3']

data1 = {'column1': 'data11', 'column2': 'data12', 'column3': 'data13'}
data2 = {'column1': 'data21', 'column2': 'data22', 'column3': 'data23'}
data.append(data1)
data.append(data2)

fm.saveFile('_2020_juli.csv', fnames, data)
files = fm.listDirectory()
for f in files:
    print(f)

data = fm.loadFile("_2020_february.csv")
for row in data:
    print(row)

fm.updateFolderContent()
print(fm.getFolderContent())

data = []
fnames = ['Item', 'Comment', 'Price EUR', 'Price CZK', 'Date']

data1 = {'Item': 'Benzin/Nafta', 'Comment': 'Nafta', 'Price EUR': '50.23', 'Price CZK': '1220.6', 'Date': '6/22/2020'}
data2 = {'Item': 'Byt', 'Comment': 'Najem', 'Price EUR': '400', 'Price CZK': '10580.27', 'Date': '6/1/2020'}
data3 = {'Item': 'Benzin/Nafta', 'Comment': 'Nafta', 'Price EUR': '38.98', 'Price CZK': '998.52', 'Date': '6/3/2020'}
data4 = {'Item': 'Jidlo', 'Comment': ' ', 'Price EUR': '35.6', 'Price CZK': '888.66', 'Date': '6/16/2020'}

data.append(data1)
data.append(data2)
data.append(data3)
data.append(data4)

fm.saveFile('_2020_june.csv', fnames, data)
'''
