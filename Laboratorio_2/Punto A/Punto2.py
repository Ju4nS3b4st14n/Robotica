import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 540, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 500, 191, 25))
        self.comboBox.setObjectName("comboBox")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 10, 641, 391))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 460, 191, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 430, 191, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 400, 230, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: red")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 430, 61, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 460, 61, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Segundo punto"))
        self.pushButton.setText(_translate("MainWindow", "Gráficar"))
        self.label.setText(_translate("MainWindow", "Valor máximo de la función"))
        self.label_2.setText(_translate("MainWindow", "Valor minimo de la función"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.pushButton.clicked.connect(self.Grafica)
        self.label_4.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_5.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_6.setText(_translate("MainWindow", "Sergio Andres Lopez"))
        self.label_9.setText(_translate("MainWindow", "Steven Santana"))
        self.comboBox.addItem("Selecciona una función")
        self.comboBox.addItem("Seno")
        self.comboBox.addItem("Coseno")
        self.comboBox.addItem("Tangente")
        self.comboBox.addItem("Cotangente")
        self.comboBox.addItem("Secante")
        self.comboBox.addItem("Cosecante")

        # Inicializar un lienzo de figuras vacío
        self.canvas = FigureCanvas(plt.figure())

        # Agregar el lienzo al widget
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)

    def Seno(self):
        min = self.lineEdit.text()
        maxi = self.lineEdit_2.text()
        if min == "" or maxi == "":
            self.label_3.setText("No has ingresado valores")
        else:
            self.label_3.setText("")

        x = np.linspace(float(min), float(maxi), 100)

        y = np.sin(x)

        # Obtener la figura y los ejes actuales
        fig = self.canvas.figure
        ax = fig.gca()

        ax.clear()

        # Crear el gráfico
        ax.plot(x, y)

        # Agregar etiquetas y título
        ax.set_xlabel('x')
        ax.set_ylabel('sin(x)')
        ax.set_title('Gráfico de la función seno')

        # Actualizar el lienzo
        self.canvas.draw()
        ax.clear()

    def Coseno(self):
        min = self.lineEdit.text()
        maxi = self.lineEdit_2.text()
        if min == "0":
            min = "1"
        if maxi == "360":
            maxi = "359"
        if maxi == "0":
            maxi = "1"
        if min == "360":
            min = "359"
        if min == "" or maxi == "":
            self.label_3.setText("No has ingresado valores")
        else:
            self.label_3.setText("")

        x = np.linspace(float(min), float(maxi), 100)

        y = np.cos(x)

        # Obtener la figura y los ejes actuales
        fig = self.canvas.figure
        ax = fig.gca()

        ax.clear()

        # Crear el gráfico
        ax.plot(x, y)

        # Agregar etiquetas y título
        ax.set_xlabel('x')
        ax.set_ylabel('cos(x)')
        ax.set_title('Gráfico de la función coseno')

        # Actualizar el lienzo
        self.canvas.draw()

    def Tangente(self):
        min = self.lineEdit.text()
        maxi = self.lineEdit_2.text()
        if min == "0":
            min = "1"
        if maxi == "360":
            maxi = "359"
        if maxi == "0":
            maxi = "1"
        if min == "360":
            min = "359"
        if min == "" or maxi == "":
            self.label_3.setText("No has ingresado valores")
        else:
            self.label_3.setText("")

        x = np.linspace(float(min), float(maxi), 100)

        y = np.tan(x)

        # Obtener la figura y los ejes actuales
        fig = self.canvas.figure
        ax = fig.gca()

        ax.clear()

        # Crear el gráfico
        ax.plot(x, y)

        # Agregar etiquetas y título
        ax.set_xlabel('x')
        ax.set_ylabel('tan(x)')
        ax.set_title('Gráfico de la función tangente')

        # Actualizar el lienzo
        self.canvas.draw()

    def Cotangente(self):
        min2 = self.lineEdit.text()
        maxi2 = self.lineEdit_2.text()
        if min2 == "0":
            min2 = "1"
        if maxi2 == "360":
            maxi2 = "359"
        if maxi2 == "0":
            maxi2 = "1"
        if min2 == "360":
            min2 = "359"
        if min2 == "" or maxi2 == "":
            self.label_3.setText("No has ingresado valores")
        else:
            self.label_3.setText("")

        x = np.linspace(float(min2), float(maxi2), 100)
        x_radians = np.deg2rad(x)

        y = 1 / np.tan(x_radians)

        # Obtener la figura y los ejes actuales
        fig = self.canvas.figure
        ax = fig.gca()

        ax.clear()

        # Crear el gráfico
        ax.plot(x, y)

        # Agregar etiquetas y título
        ax.set_xlabel('x')
        ax.set_ylabel('1/tan(x)')
        ax.set_title('Gráfico de la función cotangente')

        # Actualizar el lienzo
        self.canvas.draw()

    def Secante(self):
        min2 = self.lineEdit.text()
        maxi2 = self.lineEdit_2.text()
        if min2 == "0":
            min2 = "1"
        if maxi2 == "360":
            maxi2 = "359"
        if maxi2 == "0":
            maxi2 = "1"
        if min2 == "360":
            min2 = "359"
        if min2 == "" or maxi2 == "":
            self.label_3.setText("No has ingresado valores")
        else:
            self.label_3.setText("")

        x = np.linspace(float(min2), float(maxi2), 100)
        x_radians = np.deg2rad(x)

        y = 1 / np.cos(x_radians)

        # Obtener la figura y los ejes actuales
        fig = self.canvas.figure
        ax = fig.gca()

        ax.clear()

        # Crear el gráfico
        ax.plot(x, y)

        # Agregar etiquetas y título
        ax.set_xlabel('x')
        ax.set_ylabel('1/cos(x)')
        ax.set_title('Gráfico de la función secante')

        # Actualizar el lienzo
        self.canvas.draw()

    def Cosecante(self):
        min2 = self.lineEdit.text()
        maxi2 = self.lineEdit_2.text()
        if min2 == "0":
            min2 = "1"
        if maxi2 == "360":
            maxi2 = "359"
        if maxi2 == "0":
            maxi2 = "1"
        if min2 == "360":
            min2 = "359"
        if min2 == "" or maxi2 == "":
            self.label_3.setText("No has ingresado valores")
        else:
            self.label_3.setText("")

        x = np.linspace(float(min2), float(maxi2), 100)
        x_radians = np.deg2rad(x)

        y = 1 / np.sin(x_radians)

        # Obtener la figura y los ejes actuales
        fig = self.canvas.figure
        ax = fig.gca()

        ax.clear()

        # Crear el gráfico
        ax.plot(x, y)

        # Agregar etiquetas y título
        ax.set_xlabel('x')
        ax.set_ylabel('1/sin(x)')
        ax.set_title('Gráfico de la función cosecante')

        # Actualizar el lienzo
        self.canvas.draw()

    def Grafica(self):
        seleccion = self.comboBox.currentText()

        if seleccion == "Seno":
            self.Seno()
        if seleccion == "Coseno":
            self.Coseno()
        if seleccion == "Tangente":
            self.Tangente()
        if seleccion == "Cotangente":
            self.Cotangente()
        if seleccion == "Secante":
            self.Secante()
        if seleccion == "Cosecante":
            self.Cosecante()
        else:
            self.label_3.setText("¡No has seleccionado una función!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
