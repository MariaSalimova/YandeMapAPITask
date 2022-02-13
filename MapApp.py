from PyQt5 import QtWidgets, QtGui
import PyQt5
import sys
from PyQt5.QtCore import QByteArray, Qt
from geocoder import show_map, get_ll_spn
from window import Ui_MainWindow


class MapApp(PyQt5.QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, coord1, coord2, z):
        super(MapApp, self).__init__()
        self.setupUi(self)
        self.add_params = dict()
        self.x, self.y = map(float, (coord1, coord2))
        self.centre = f"{coord1},{coord2}"
        self.z = z
        self.clearFocus()
        self.show_map()
        self.search_button.clicked.connect(self.show_object)
        self.reset.clicked.connect(self.clear_point)
        self.map_mode.currentIndexChanged.connect(self.show_map)

    def show_map(self):
        self.map_mode.clearFocus()
        mode = self.map_mode.currentText()
        if mode == 'Схема':
            mode = 'map'
        elif mode == 'Гибрид':
            mode = 'sat,skl'
        elif mode == 'Спутник':
            mode = 'sat'

        img = show_map(",".join((map(str, (self.x, self.y)))), self.z, map_type=mode, add_params=self.add_params)
        pixmap = PyQt5.QtGui.QPixmap()
        pixmap.loadFromData(QByteArray(img))
        self.map_label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        pass
        # key = event.key()
        # if key == Qt.Key_PageUp:
        #     self.z += 1
        #     if self.z > 17:
        #         self.z = 17
        #     self.show_map()
        # elif key == Qt.Key_PageDown:
        #     self.z -= 1
        #     if self.z < 0:
        #         self.z = 0
        #     self.show_map()
        # elif key == 1062:
        #     self.y += 90 / (self.z * 1000)
        #     if self.y >= 90:
        #         self.y = -89
        #     self.show_map()
        #     print("Вверх")
        # elif key == 1067:
        #     self.y -= 90 / (self.z * 1000)
        #     if self.y <= -90:
        #         self.y = 89
        #     self.show_map()
        #     print("Вниз")
        # elif key == 1060:
        #     self.x -= 180 / (self.z * 1000)
        #     if self.x <= -180:
        #         self.x = 179
        #     self.show_map()
        #     print("Влево")
        # elif key == 1042:
        #     self.x += 180 / (self.z * 1000)
        #     if self.x >= 180:
        #         self.x = -179
        #     self.show_map()
        #     print("Враво")

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_PageUp:
            self.z += 1
            if self.z > 17:
                self.z = 17
            self.show_map()
        elif key == Qt.Key_PageDown:
            self.z -= 1
            if self.z < 0:
                self.z = 0
            self.show_map()
        elif key == Qt.Key_Up:
            self.y += 90 / (self.z * 2000)
            if self.y >= 90:
                self.y = -89
            self.show_map()
            print("Вверх")
        elif key == Qt.Key_Down:
            self.y -= 90 / (self.z * 2000)
            if self.y <= -90:
                self.y = 89
            self.show_map()
            print("Вниз")
        elif key == Qt.Key_Left:
            self.x -= 180 / (self.z * 2000)
            if self.x <= -180:
                self.x = 179
            self.show_map()
            print("Влево")
        elif key == Qt.Key_Right:
            self.x += 180 / (self.z * 2000)
            if self.x >= 180:
                self.x = -179
            self.show_map()
            print("Враво")

    def show_object(self):
        ll, spn = get_ll_spn(self.search_line.text())
        self.x, self.y = map(float, ll.split(','))
        self.add_params["pt"] = f"{ll},pm2rdm"
        self.show_map()

    def clear_point(self):
        self.add_params.pop("pt")
        self.show_map()


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ll, spn = get_ll_spn('Ветлужская 89')
    map_app = MapApp(*ll.split(','), 14)
    # map_app = MapApp(sys.argv[1], sys.argv[2], sys.argv[3])
    map_app.show()
    sys.exit(app.exec())
    #  sys.argv[1], sys.argv[2], sys.argv[3]
    #  *ll.split(','), 14