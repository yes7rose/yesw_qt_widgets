#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------
#  Authur: 闫刚
#　Create date: '2017/11/8' '11:07'
# -----------------

from qtpy import QtWidgets

class LabelSpinBox(QtWidgets.QWidget):
    """
    """
    def __init__(self, parent=None):
        super(LabelSpinBox, self).__init__(parent=parent)

        self._label = QtWidgets.QLabel("spin_name")
        self._spinbox = QtWidgets.QSpinBox()
        self._spinbox.setMinimum(0)
        self._spinbox.setMaximum(20000)

        self._mainLayout = QtWidgets.QHBoxLayout()

        self._mainLayout.addWidget(self._label)
        self._mainLayout.addWidget(self._spinbox)
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        self._mainLayout.addStretch()

        self.setLayout(self._mainLayout)

    def setSpinStartValue(self, value):
        """
        """
        self._spinbox.setValue(value)

    def setLabel(self, label):
        """
        """
        self._label.setText(label)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = LabelSpinBox()
    w.setLabel("new")
    w.show()

    app.exec_()