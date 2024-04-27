from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 500, 191, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_imagen = QtWidgets.QLabel(self.centralwidget)
        self.label_imagen.setGeometry(QtCore.QRect(200, 50, 400, 300))
        self.label_imagen.setObjectName("label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 380, 380, 20))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 160, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 450, 160, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 480, 160, 25))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 540, 160, 25))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(580, 430, 221, 151))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../Robotica/Laboratorio_2/Imagenes/images.png"))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.currentTextChanged.connect(self.cargarImagen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tercer punto"))
        self.label.setText(_translate("MainWindow", "Número de articulaciones y sus tipos"))
        self.label_4.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_5.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_6.setText(_translate("MainWindow", "Sergio Andres Lopez"))
        self.label_9.setText(_translate("MainWindow", "Steven Santana"))
        self.comboBox.addItem("Selecciona un robot")
        self.comboBox.addItem("Cartesiano")
        self.comboBox.addItem("Esférico")
        self.comboBox.addItem("Cilindrico")
        
    def cargarImagen(self, seleccion):
        # Define las rutas de las imágenes según la opción seleccionada
        if seleccion == "Cartesiano":
            print("Cartesiano")
            imagen_path = "../Robotica/Laboratorio_2/Imagenes/Cartesiano.jpeg"
            self.label.setText("tiene 3 articulaciones tipo Prismaticas")

        elif seleccion == "Esférico":
            imagen_path = "../Robotica/Laboratorio_2/Imagenes/Esferico.jpeg"
            self.label.setText("tiene 3 articulaciones una Prismaticas y dos rotacionales")
            
        elif seleccion == "Cilindrico":
            print("Cilindrico")
            imagen_path = "../Robotica/Laboratorio_2/Imagenes/Cilindrico.jpeg"
            self.label.setText("tiene 3 articulaciones dos Prismaticas y una rotacional")

        else:
            self.label.setText("¡No has seleccionado ningún robot!")
            self.label.setStyleSheet("color: red")

        # Crea un QLabel para mostrar la imagen
        pixmap = QtGui.QPixmap(imagen_path)
        self.label_imagen.setPixmap(pixmap)
        self.label_imagen.setScaledContents(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

