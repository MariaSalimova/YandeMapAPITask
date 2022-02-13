from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QComboBox
from PyQt5.uic.properties import QtGui


class OurComboBox(QComboBox):

    def keyPressEvent(self, event):
        # key = event.key()
        # if key not in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right]:
        # super(OurComboBox, self).keyPressEvent(event)
        self.clearFocus()
        pass

    def keyReleaseEvent(self, event):
        # key = event.key()
        # if key not in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right]:
        # super(OurComboBox, self).keyReleaseEvent(event)
        self.clearFocus()
        pass


class OurLineEdit(QLineEdit):

    def keyPressEvent(self, event):
        # key = event.key()
        # if key not in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right]:
        super(OurLineEdit, self).keyPressEvent(event)

    def keyReleaseEvent(self, event):
        # key = event.key()
        # if key not in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right]:
        super(OurLineEdit, self).keyReleaseEvent(event)
