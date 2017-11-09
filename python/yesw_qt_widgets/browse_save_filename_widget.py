#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------
#  Authur: 闫刚
#　Create date: '2017/11/9' '16:12'
# -----------------

from qtpy import QtWidgets

class BrowsSaveFileNameWidget(QtWidgets.QWidget):
    """
    """
    def __init__(self, open_location = "\.",file_filter = "*.*",parent=None):
        super(BrowsSaveFileNameWidget, self).__init__()

        self._file_name_lable = QtWidgets.QLabel("File Name")
        self._file_name_lineEdit = QtWidgets.QLineEdit()
        self._file_name_browseBtn = QtWidgets.QPushButton("Browse")

        self._open_location = open_location
        self._file_filter = file_filter

        self._main_layout = QtWidgets.QHBoxLayout()

        self._setupGui()
        self.setupActions()

    def _setupGui(self):
        """
        """
        self._main_layout.addWidget(self._file_name_lable)
        self._main_layout.addWidget(self._file_name_lineEdit)
        self._main_layout.addWidget(self._file_name_browseBtn)

        self._main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self._main_layout)

    def setupActions(self):
        """
        """
        self._file_name_browseBtn.clicked.connect(self.browseFile)

    def browseFile(self):
        """
        """
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'browse file', self._open_location, self._file_filter, '')[0]
        if not file_name:
            return

        self._file_name_lineEdit.setText(file_name)

    def setFileNameLable(self, new_label):
        """
        :new_label new label
        """
        if not new_label:
            return

        self._file_name_lable.setText(new_label)

    def setStartOpenLocation(self, new_location):
        """
        """
        if not new_location:
            return

        self._open_location = new_location

    def setFileFilter(self, file_filter):
        """
        """
        if not file_filter:
            return

        self._file_filter = file_filter

    def getFileName(self):
        return self._file_name_lineEdit.text()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = BrowsSaveFileNameWidget()
    w.show()

    app.exec_()
