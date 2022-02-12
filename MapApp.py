import PyQt5.QtWidgets
import PyQt5.QtGui
from PyQt5 import uic
import sys
from PyQt5.QtCore import QByteArray
from geocoder import show_map


class MapApp(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, coord1, coord2, z):
        super(MapApp, self).__init__()
        uic.loadUi('map1.ui', self)
        self.show()
        self.centre = f"{coord1},{coord2}"
        self.z = z
        self.show_map()

    def show_map(self):
        img = show_map(self.centre, self.z)
        pixmap = PyQt5.QtGui.QPixmap()
        pixmap.loadFromData(QByteArray(img))
        self.map_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    # ll, spn = get_ll_spn('Ветлужская 89')
    map_app = MapApp(sys.argv[1], sys.argv[2], sys.argv[3])
    map_app.show()
    sys.exit(app.exec())
    #  sys.argv[1], sys.argv[2], sys.argv[3]
    #  *ll.split(','), 14