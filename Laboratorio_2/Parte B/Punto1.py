from PyQt5 import QtCore, QtGui, QtWidgets
from gpiozero import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(250, 210, 311, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 180)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(390, 150, 51, 25))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 331, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 205, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(96, 205, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 160, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 450, 160, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 480, 160, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 380, 221, 151))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../Imagenes/images.png"))
        self.label_7.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.horizontalSlider.valueChanged.connect(self.controlServ)

        self.serv1 = Servo(19)
        self.serv2 = Servo(16)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ingresa el número del servomotor a seleccionar"))
        self.label_2.setText(_translate("MainWindow", "Grados: 0 °"))
        self.label_3.setText(_translate("MainWindow", "Servomotor: "))
        self.label_4.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_5.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_6.setText(_translate("MainWindow", "Sergio ANdres Lopez"))

    def controlServ(self, value):

        Servomotor = self.textEdit.toPlainText()
        
        if Servomotor == '1' :
            pos = value / 180
            print (pos)
            self.serv1.value = pos
            self.label_2.setText("Grados: {} °".format(value))
            self.label_3.setText("Servomotor: 1")
            self.label_3.setStyleSheet("color: black")

        elif Servomotor == '2' :
            self.serv2.value = value / 180
            self.label_2.setText("Grados: {} °".format(value))
            self.label_3.setText("Servomotor: 2")
            self.label_3.setStyleSheet("color: black")
        
        else:
            self.label_2.setText("Grados: 0")
            self.label_3.setText("No seleccionado")
            self.label_3.setStyleSheet("color: red")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
