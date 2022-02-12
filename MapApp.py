from PyQt5 import QtWidgets, QtGui, uic
import PyQt5
import sys
from PyQt5.QtCore import QByteArray, Qt
from geocoder import show_map, get_ll_spn


class MapApp(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, coord1, coord2, z):
        super(MapApp, self).__init__()
        uic.loadUi('map5.ui', self)
        self.show()
        self.add_params = dict()
        self.centre = f"{coord1},{coord2}"
        self.z = z
        self.show_map()
        self.search_button.clicked.connect(self.show_object)

    def show_map(self):
        mode = self.map_mode.currentText()
        if mode == 'Схема':
            mode = 'map'
        elif mode == 'Гибрид':
            mode = 'sat,skl'
        elif mode == 'Спутник':
            mode = 'sat'

        img = show_map(self.centre, self.z, map_type=mode, add_params=self.add_params)
        pixmap = PyQt5.QtGui.QPixmap()
        pixmap.loadFromData(QByteArray(img))
        self.map_label.setPixmap(pixmap)

    def keyPressEvent(self, event):
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

    def show_object(self):
        ll, spn = get_ll_spn(self.search_line.text())
        self.centre = ll
        if 'pt' in self.add_params:
            self.add_params['pt'] = f"{self.add_params}~{f'{ll},pm2rdm'}"
        else:
            self.add_params["pt"] = f"{ll},pm2rdm"


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ll, spn = get_ll_spn('Ветлужская 89')
    map_app = MapApp(*ll.split(','), 14)
    # map_app = MapApp(sys.argv[1], sys.argv[2], sys.argv[3])
    map_app.show()
    sys.exit(app.exec())
    #  sys.argv[1], sys.argv[2], sys.argv[3]
    #  *ll.split(','), 14