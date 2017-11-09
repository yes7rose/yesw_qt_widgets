#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------
#  Authur: 闫刚
#　Create date: '2017/11/7' '15:30'
# -----------------

from qtpy import QtWidgets

class BrowsDirNameWidget(QtWidgets.QWidget):
    """
    """

    def __init__(self, open_location="\.", parent=None):
        super(BrowsDirNameWidget, self).__init__()

        self._dir_name_lable = QtWidgets.QLabel("Dir Name")
        self._dir_name_lineEdit = QtWidgets.QLineEdit()
        self._dir_name_browseBtn = QtWidgets.QPushButton("Browse")

        self._open_location = open_location
        self._dir_name_lineEdit.setText(open_location)

        self._main_layout = QtWidgets.QHBoxLayout()

        self.setupGui()
        self.setupActions()

    def setupGui(self):
        """
        """
        self._main_layout.addWidget(self._dir_name_lable)
        self._main_layout.addWidget(self._dir_name_lineEdit)
        self._main_layout.addWidget(self._dir_name_browseBtn)

        self._main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self._main_layout)

    def setupActions(self):
        """
        """
        self._dir_name_browseBtn.clicked.connect(self.browseDir)

    def setStartOpenLocation(self, new_location):
        """
        """
        if not new_location:
            return

        self._open_location = new_location

    def browseDir(self):
        """
        """
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'browse file', self._open_location)
        # print(dir_name)
        if not dir_name:
            return

        self._dir_name_lineEdit.setText(dir_name)

    def setDirNameLable(self, new_label):
        """
        :new_label new label
        """
        if not new_label:
            return

        self._dir_name_lable.setText(new_label)

    def getDirName(self):
        return self._dir_name_lineEdit.text()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    w = BrowsDirNameWidget()
    w.show()

    app.exec_()