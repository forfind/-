# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DATE_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(248, 302)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 191, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 31, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 81, 31))
        self.label_2.setObjectName("label_2")
        self.gbtn = QtWidgets.QPushButton(self.centralwidget)
        self.gbtn.setGeometry(QtCore.QRect(190, 10, 51, 31))
        self.gbtn.setObjectName("gbtn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 230, 231, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbtn = QtWidgets.QPushButton(self.layoutWidget)
        self.lbtn.setObjectName("lbtn")
        self.horizontalLayout.addWidget(self.lbtn)
        self.nowbtn = QtWidgets.QPushButton(self.layoutWidget)
        self.nowbtn.setObjectName("nowbtn")
        self.horizontalLayout.addWidget(self.nowbtn)
        self.nbtn = QtWidgets.QPushButton(self.layoutWidget)
        self.nbtn.setObjectName("nbtn")
        self.horizontalLayout.addWidget(self.nbtn)
        self.lE_y = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_y.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.lE_y.setObjectName("lE_y")
        self.lE_m = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_m.setGeometry(QtCore.QRect(110, 10, 41, 31))
        self.lE_m.setObjectName("lE_m")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "年"))
        self.label_2.setText(_translate("MainWindow", "月"))
        self.gbtn.setText(_translate("MainWindow", "Go"))
        self.lbtn.setText(_translate("MainWindow", "上一月"))
        self.nowbtn.setText(_translate("MainWindow", "当前月"))
        self.nbtn.setText(_translate("MainWindow", "下一月"))
