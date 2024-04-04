from PyQt5 import QtCore, QtGui, QtWidgets
from gpiozero import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(345, 100, 131, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 200, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 510, 160, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 450, 160, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 480, 160, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 380, 221, 151))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../Imagenes/images.png"))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pin_number = 21 
        self.button = Button(pin_number)

        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Estado de pin"))
        self.label_2.setText(_translate("MainWindow", "Alto o bajo"))
        self.label_3.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_4.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_5.setText(_translate("MainWindow", "Sergio Andres Lopez"))

    def update_label(self):

        if self.button.is_pressed:
            self.label_2.setText("Alto")
            self.label_2.setStyleSheet("color: red")
        else:
            self.label_2.setText("Bajo")
            self.label_2.setStyleSheet("color: blue")

        pass
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())