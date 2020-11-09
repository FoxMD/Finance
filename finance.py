import files
import sys
from qtpy import QtWidgets

# QT with Cpp
app = QtWidgets.QApplication(sys.argv)
window = files.MainWindow()
window.show()

sys.exit(app.exec_())
