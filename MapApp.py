import PyQt5.QtWidgets
from PyQt5 import uic
import sys


class MapApp(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, coord1, coord2, z):
        super.__init__()
        uic.loadUi('map1.ui', self)


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    map_app = MapApp()
    map_app.show()
    sys.exit(app.exec())