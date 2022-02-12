from PyQt5 import QtWidgets, QtGui, uic
import PyQt5
import sys
from PyQt5.QtCore import QByteArray, Qt
from geocoder import show_map, get_ll_spn


class MapApp(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, coord1, coord2, z):
        super(MapApp, self).__init__()
        uic.loadUi('map1.ui', self)
        self.show()
        self.x, self.y = [coord1, coord2]
        self.centre = f"{self.x},{self.y}"
        self.z = z
        self.show_map()

    def show_map(self):

        img = show_map(f"{self.x},{self.y}", self.z)
        pixmap = PyQt5.QtGui.QPixmap()
        pixmap.loadFromData(QByteArray(img))
        self.map_label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.y += 90 // self.z
            if self.y >= 90:
                self.y = -89
            self.show_map()
            print("Вверх")
        elif key == Qt.Key_Down:
            self.y -= 90 // self.z
            if self.y <= -90:
                self.y = 89
            self.show_map()
            print("Вниз")
        elif key == Qt.Key_Left:
            self.x -= 180 // self.z
            if self.x <= -180:
                self.x = 179
            self.show_map()
            print("Влево")
        elif key == Qt.Key_Right:
            self.x += 180 // self.z
            if self.x >= 180:
                self.x = -179
            self.show_map()
            print("Враво")


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    # ll, spn = get_ll_spn('Ветлужская 89')
    # map_app = MapApp(*ll.split(','), 14)
    map_app = MapApp(58.044926530791386, 56.09480283862304, 1)
    map_app.show()
    sys.exit(app.exec())
    #  sys.argv[1], sys.argv[2], sys.argv[3]
    #  *ll.split(','), 14
