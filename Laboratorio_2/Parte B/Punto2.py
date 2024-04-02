from PyQt5 import QtCore, QtGui, QtWidgets
from gpiozero import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 150, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: black; color: white;")  # Establecer el color de fondo y el color de texto
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 150, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: black; color: white;")  # Establecer el color de fondo y el color de texto
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(230, 240, 301, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 100)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(230, 290, 301, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setRange(0, 100)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 100, 131, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 200, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 510, 160, 25))
        self.label_3.setObjectName("label_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 450, 160, 25))
        self.label_4.setObjectName("label_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 480, 160, 25))
        self.label_5.setObjectName("label_6")
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

        self.pushButton.clicked.connect(self.led1btn)
        self.pushButton_2.clicked.connect(self.led2btn)

        self.horizontalSlider.valueChanged.connect(self.led1slider)
        self.horizontalSlider_2.valueChanged.connect(self.led2slider)

        # Inicializar el contador de clics
        self.click_count = 0
        #led1 = LED(23).off()
        #LED(22).off()
        self.click_count2 = 0

        # Inicializar el LED con intensidad 0 (apagado)
        #self.led1 = PWMLED(17)
        #self.led2 = PWMLED(27)
        #self.led3 = LED(23)
        #self.led4 = LED(22)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OFF"))
        self.pushButton_2.setText(_translate("MainWindow", "OFF"))
        self.label.setText(_translate("MainWindow", "Led\'s push button"))
        self.label_2.setText(_translate("MainWindow", "Led\'s slider"))
        self.label_3.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_4.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_5.setText(_translate("MainWindow", "Sergio Andres Lopez"))

    def led1btn(self):

        self.click_count += 1

        if self.click_count % 2 == 1:
            self.led3.on()
            self.pushButton.setText("ON")
            self.pushButton.setStyleSheet("background-color: red; color: black;")
        
        else: 
            self.led3.off()
            self.pushButton.setText("OFF")
            self.pushButton.setStyleSheet("background-color: black; color: white")
        
    def led2btn(self):
        self.click_count2 += 1
        
        if self.click_count2 % 2 == 1:
            self.led4.on()
            self.pushButton_2.setText("ON")
            self.pushButton_2.setStyleSheet("background-color: red; color: black;")
        
        else: 
            self.led4.off()
            self.pushButton_2.setText("OFF")
            self.pushButton_2.setStyleSheet("background-color: black; color: white")
        

    def led1slider(self, value):
        self.led1.value = value/100

    def led2slider(self, value):
        self.led2.value = value/100 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())