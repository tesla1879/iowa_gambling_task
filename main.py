# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iowa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot


class List:
    def __init__(self):
        # self.stackA
        self.make_list()

    def make_list(self):
        protolist = np.random.randint(-200, 200, 10)
        protolist = np.random.normal(50, 200, 10).astype(int)
        # list1 = np.array([-140, 58, 135, 2, -158, -185, 146, 100, 65, -183])
        # np.random.shuffle(protolist)
        # for _ in range(10):
        #     probability = np.random.rand()
        #     threshold = fee_count

        print(protolist)


# List()


class Ui_MainWindow(object):

    def __init__(self):
        self.listA = np.zeros(10).astype(int)
        self.listB = np.zeros(10).astype(int)
        self.listC = np.zeros(10).astype(int)
        self.listD = np.zeros(10).astype(int)
        self.counter = 0
        self.episode = 1
        self.init_lists()

    def init_lists(self):
        self.listA = np.random.normal(np.random.randint(10, 50), np.random.randint(100, 200), 10).astype(int)
        self.listB = np.random.normal(np.random.randint(10, 50), np.random.randint(100, 200), 10).astype(int)
        self.listC = np.random.normal(np.random.randint(10, 50), np.random.randint(100, 200), 10).astype(int)
        self.listD = np.random.normal(np.random.randint(10, 50), np.random.randint(100, 200), 10).astype(int)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 600)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButtonA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonA.setGeometry(QtCore.QRect(220, 160, 141, 201))
        self.pushButtonA.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButtonA.setText("")
        self.pushButtonA.setObjectName("pushButtonA")
        self.pushButtonA.clicked.connect(self.btnA_on_click)

        self.pushButtonB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonB.setGeometry(QtCore.QRect(390, 160, 141, 201))
        self.pushButtonB.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButtonB.setText("")
        self.pushButtonB.setObjectName("pushButtonB")
        self.pushButtonB.clicked.connect(self.btnB_on_click)

        self.pushButtonC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonC.setGeometry(QtCore.QRect(560, 160, 141, 201))
        self.pushButtonC.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButtonC.setText("")
        self.pushButtonC.setObjectName("pushButtonC")
        self.pushButtonC.clicked.connect(self.btnC_on_click)

        self.pushButtonD = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonD.setGeometry(QtCore.QRect(730, 160, 141, 201))
        self.pushButtonD.setStyleSheet("background-image: url(./resources/cardrr.png);")
        self.pushButtonD.setText("")
        self.pushButtonD.setObjectName("pushButtonD")
        self.pushButtonD.clicked.connect(self.btnD_on_click)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(370, 30, 251, 41))
        self.title.setStyleSheet("font: 75 20pt \"Titr\";")
        self.title.setObjectName("title")
        self.counter_label = QtWidgets.QLabel(self.centralwidget)
        self.counter_label.setGeometry(QtCore.QRect(800, 380, 71, 31))
        self.counter_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.counter_label.setObjectName("counter_label")
        self.counter_number = QtWidgets.QLabel(self.centralwidget)
        self.counter_number.setGeometry(QtCore.QRect(780, 390, 57, 16))
        self.counter_number.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.counter_number.setObjectName("counter_number")
        self.gain_counter = QtWidgets.QLabel(self.centralwidget)
        self.gain_counter.setGeometry(QtCore.QRect(780, 420, 57, 15))
        self.gain_counter.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.gain_counter.setObjectName("gain_counter")
        self.gain = QtWidgets.QLabel(self.centralwidget)
        self.gain.setGeometry(QtCore.QRect(800, 410, 71, 31))
        self.gain.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.gain.setObjectName("gain")
        self.episode_label = QtWidgets.QLabel(self.centralwidget)
        self.episode_label.setGeometry(QtCore.QRect(800, 440, 71, 31))
        self.episode_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.episode_label.setObjectName("episode_label")
        self.episode_counter = QtWidgets.QLabel(self.centralwidget)
        self.episode_counter.setGeometry(QtCore.QRect(780, 450, 57, 16))
        self.episode_counter.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.episode_counter.setObjectName("episode_counter")
        self.total_score_counter = QtWidgets.QLabel(self.centralwidget)
        self.total_score_counter.setGeometry(QtCore.QRect(610, 390, 57, 15))
        self.total_score_counter.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.total_score_counter.setObjectName("total_score_counter")
        self.total_score_label = QtWidgets.QLabel(self.centralwidget)
        self.total_score_label.setGeometry(QtCore.QRect(630, 380, 71, 31))
        self.total_score_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.total_score_label.setObjectName("total_score_label")
        self.card_a = QtWidgets.QLabel(self.centralwidget)
        self.card_a.setGeometry(QtCore.QRect(280, 120, 16, 31))
        self.card_a.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.card_a.setObjectName("card_a")
        self.card_b = QtWidgets.QLabel(self.centralwidget)
        self.card_b.setGeometry(QtCore.QRect(460, 120, 16, 31))
        self.card_b.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.card_b.setObjectName("card_b")
        self.card_c = QtWidgets.QLabel(self.centralwidget)
        self.card_c.setGeometry(QtCore.QRect(620, 120, 16, 31))
        self.card_c.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.card_c.setObjectName("card_c")
        self.card_d = QtWidgets.QLabel(self.centralwidget)
        self.card_d.setGeometry(QtCore.QRect(790, 120, 16, 31))
        self.card_d.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.card_d.setObjectName("card_d")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # @pyqtSlot()
    def btnA_on_click(self):
        if self.episode < 2:
            if self.counter > 9:
                self.episode += 1
                self.counter = 0
            if self.episode < 2:
                self.gain_counter.setText(str(self.listA[self.counter]))
                self.counter += 1
                self.counter_number.setText(str(self.counter))
                self.episode_counter.setText(str(self.episode))
                print(self.listA)
                self.counter_number.setText(str(self.counter))
                self.episode_counter.setText(str(self.episode))
                # self.episode_counter.setText(str(int(self.episode_counter.text()) + 1))
                self.card_a.setStyleSheet("color: red; font: 14pt")

                # self.episode_counter.setText(str(int(self.episode_counter.text()) + 1))
                self.card_a.setStyleSheet("color: red; font: 14pt")
            else:
                self.title.setText("پایان")
        print(f"A: counter {self.counter}")


    def btnB_on_click(self):
        print('Button B')
        # self.episode_counter.setText(str(int(self.episode_counter.text()) + 1))
        self.card_a.setStyleSheet("color: red; font: 14pt")

    def btnC_on_click(self):
        print('Button C')
        # self.episode_counter.setText(str(int(self.episode_counter.text()) + 1))
        self.card_a.setStyleSheet("color: red; font: 14pt")

    def btnD_on_click(self):
        print('Button D')
        # self.episode_counter.setText(str(int(self.episode_counter.text()) + 1))
        self.card_a.setStyleSheet("color: red; font: 14pt")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "روی کارت ها کلیک کنید"))
        self.counter_label.setText(_translate("MainWindow", "شماره:"))
        self.counter_number.setText(_translate("MainWindow", "0"))
        self.gain_counter.setText(_translate("MainWindow", "0"))
        self.gain.setText(_translate("MainWindow", "سود:"))
        self.episode_label.setText(_translate("MainWindow", "اپیسود:"))
        self.episode_counter.setText(_translate("MainWindow", "1"))
        self.total_score_counter.setText(_translate("MainWindow", "0"))
        self.total_score_label.setText(_translate("MainWindow", "مجموع:"))
        self.card_a.setText(_translate("MainWindow", "A"))
        self.card_b.setText(_translate("MainWindow", "B"))
        self.card_c.setText(_translate("MainWindow", "C"))
        self.card_d.setText(_translate("MainWindow", "D"))


# import img_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
