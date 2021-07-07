# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iowa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 600)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonD = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonD.setGeometry(QtCore.QRect(730, 160, 141, 201))
        self.pushButtonD.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButtonD.setText("")
        self.pushButtonD.setObjectName("pushButtonD")
        self.pushButtonD.clicked.connect(self.btnD_on_click)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 160, 141, 201))
        self.pushButton_2.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 160, 141, 201))
        self.pushButton_3.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 160, 141, 201))
        self.pushButton_4.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 30, 251, 41))
        self.label.setStyleSheet("font: 75 20pt \"Titr\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 380, 71, 31))
        self.label_2.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 390, 57, 16))
        self.label_3.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(780, 420, 57, 15))
        self.label_9.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(800, 410, 71, 31))
        self.label_4.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 440, 71, 31))
        self.label_5.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(780, 450, 57, 16))
        self.label_8.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 390, 57, 15))
        self.label_10.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(630, 380, 71, 31))
        self.label_11.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 120, 16, 31))
        self.label_12.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 120, 16, 31))
        self.label_13.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(620, 120, 16, 31))
        self.label_14.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(790, 120, 16, 31))
        self.label_15.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # @pyqtSlot()
    def btnD_on_click(self):
        print('Button D')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "روی کارت ها کلیک کنید"))
        self.label_2.setText(_translate("MainWindow", "شماره:"))
        self.label_3.setText(_translate("MainWindow", "1"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "سود:"))
        self.label_5.setText(_translate("MainWindow", "اپیسود:"))
        self.label_8.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "مجموع:"))
        self.label_12.setText(_translate("MainWindow", "A"))
        self.label_13.setText(_translate("MainWindow", "B"))
        self.label_14.setText(_translate("MainWindow", "C"))
        self.label_15.setText(_translate("MainWindow", "D"))


# import img_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
