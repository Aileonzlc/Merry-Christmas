# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QLabel, QHBoxLayout,QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, QSize, Qt, QMetaObject


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 540)
        MainWindow.setMinimumSize(QSize(400, 540))
        MainWindow.setMaximumSize(QSize(400, 540))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/ico/logo.ico"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.giflabel = QLabel(self.centralwidget)
        self.giflabel.setAlignment(Qt.AlignCenter)
        self.giflabel.setObjectName("giflabel")
        self.horizontalLayout.addWidget(self.giflabel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Merry Christmas"))
import resource_rc
