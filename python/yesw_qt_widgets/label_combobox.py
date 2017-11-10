#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------
#  Authur: 闫刚
#　Create date: '2017/11/10' '10:51'
# -----------------

from qtpy import QtWidgets

class LabelComboBox(QtWidgets.QWidget):
    """
    """
    def __init__(self, parent=None):
        super(LabelComboBox, self).__init__(parent=parent)

        self._label = QtWidgets.QLabel("combo label")
        self._comboBox = QtWidgets.QComboBox()

        self._mainLayout = QtWidgets.QHBoxLayout()
        self._mainLayout.addWidget(self._label)
        self._mainLayout.addWidget(self._comboBox)

        self.setLayout(self._mainLayout)

    def setLabel(self, label):
        """
        """
        self._label.setText(label)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = LabelComboBox()
    w.setLabel("new")
    w.show()

    app.exec_()
