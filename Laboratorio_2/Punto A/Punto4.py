import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tercer putno")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(270, 20, 261, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 1000)  # Modificar el rango del slider
        self.horizontalSlider.valueChanged.connect(self.on_slider_valueChanged)  # Conectar la señal valueChanged
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(270, 50, 261, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setRange(0, 10000)  # Modificar el rango del slider
        self.horizontalSlider_2.valueChanged.connect(self.on_slider_valueChanged)  # Conectar la señal valueChanged
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(270, 80, 261, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setRange(0, 120)  # Modificar el rango del slider
        self.horizontalSlider_3.valueChanged.connect(self.on_slider_valueChanged)  # Conectar la señal valueChanged
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 150, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 150, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 80, 150, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 20, 200, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 50, 200, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 80, 200, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 530, 160, 25))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 570, 160, 25))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 610, 160, 25))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 650, 160, 25))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(530, 520, 221, 151))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../Robotica/Laboratorio_2/Imagenes/images.png"))
        self.label_10.setObjectName("label_10")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 120, 721, 390))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cuart punto"))
        self.label.setText(_translate("MainWindow", "Resistencia"))
        self.label_2.setText(_translate("MainWindow", "Capacitancia"))
        self.label_3.setText(_translate("MainWindow", "Voltaje"))
        self.label_4.setText(_translate("MainWindow", "(Ω): 0"))
        self.label_5.setText(_translate("MainWindow", "(f): 0"))
        self.label_6.setText(_translate("MainWindow", "(v): 0"))
        self.label_7.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_8.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_9.setText(_translate("MainWindow", "Sergio Andres Lopez"))
        self.label_11.setText(_translate("MainWindow", "Steven Santana"))

        # Inicializar un lienzo de figuras vacío
        self.canvas = FigureCanvas(plt.figure())

        # Agregar el lienzo al widget
        layout = QtWidgets.QVBoxLayout(self.widget)
        layout.addWidget(self.canvas)


    def on_slider_valueChanged(self, value):
        
        resistencia = self.horizontalSlider.value()  # Valor de la resistencia (Ω)
        capacitancia = self.horizontalSlider_2.value() / 1e6  # Valor de la capacitancia (F), asumiendo que el slider da valor en μF
        voltaje = self.horizontalSlider_3.value()  # Valor del voltaje (V)

        tau = resistencia * capacitancia  # Constante de tiempo τ = RC
        t_carga = np.linspace(0, 5 * tau, 500)  # Tiempo para la curva de carga
        t_descarga = np.linspace(0, 5 * tau, 500)  # Tiempo para la curva de descarga después de la carga

        carga = voltaje * (1 - np.exp(-t_carga / tau))  # Ecuación de carga
        descarga = voltaje * np.exp(-t_descarga / tau)  # Ecuación de descarga

        # Obtener la figura y los ejes actuales
        fig = self.canvas.figure
        ax = fig.gca()

        ax.clear()

        # Graficar carga y descarga
        ax.plot(t_carga, carga, label='Carga')
        ax.plot(t_descarga + 5 * tau, descarga, label='Descarga')  # Asumiendo la descarga comienza después de la carga

        # Agregar etiquetas y título
        ax.set_xlabel('Tiempo (s)')
        ax.set_ylabel('Voltaje (V)')
        ax.set_title('Carga y Descarga en un Circuito RC')

        # Mostrar leyenda
        ax.legend()

        # Actualizar el lienzo
        self.canvas.draw()

        # Actualizar etiquetas
        self.label_4.setText("(Ω): {}".format(resistencia))
        self.label_5.setText("(F): {}".format(capacitancia))
        self.label_6.setText("(V): {}".format(voltaje))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
