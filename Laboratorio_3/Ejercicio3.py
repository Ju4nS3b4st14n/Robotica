from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt

# Longitudes de los eslabones
l1 = 6
l2 = 8

# Definición de las coordenadas de cada letra
coordenadas_letras = {
    # Definir los puntos para cada letra
    'J': [(0, 5), (2, 5), (2, 0), (1, 0)],
    'A': [[0, 0], [0, 5], [2, 5], [2, 0], [2, 2.5],[0, 2.5]],
    'B': [[0, 0], [0, 5], [2, 5], [2, 2.5], [0, 2.5],[2, 2.5],[2,0],[0,0]],
    'C': [[2, 0], [0, 0], [0, 5], [2, 5]],
    'D': [[0, 0], [0, 5], [2, 5], [2, 0], [0, 0]],
    'E': [[2, 0], [0, 0], [0, 2.5], [1, 2.5],[0,2.5],[0,5],[2,5]],
    'F': [[0, 0], [0, 2.5], [1, 2.5],[0,2.5],[0,5],[2,5]],
    'G': [[1, 2.5], [2, 2.5], [2, 0], [0, 0],[0,5],[2,5]],
    'H': [[0, 0], [0, 5], [0, 2.5], [2, 2.5],[2,5],[2,0]],
    'I': [[0, 0], [2, 0], [1, 0], [1, 5],[0,5],[2,5]],
    'J': [[0, 2.5], [0, 0], [1, 0], [1, 5],[0,5],[2,5]],
    'K': [[0, 0], [0, 5], [0, 2.5], [2, 5],[0,2.5],[2,0]],
    'L': [[0, 5], [0, 0], [2, 0]],
    'M': [[0, 0], [0, 5], [1, 2.5], [2, 5],[2,5],[2,0]],
    'N': [[0, 0], [0, 5], [2, 0], [2, 5]],
    'O': [[0, 0], [0, 5], [2, 5], [2, 0], [0, 0]],
    'P': [[0, 0], [0, 5], [2, 5], [2, 2.5], [0, 2.5]],
    'Q': [[0, 0], [0, 5], [2, 5], [2, 0], [0, 0], [2, 0],[1,2.5],[2,0]],#arreglar
    'R': [[0, 0], [0, 5], [2, 5], [2, 2.5], [0, 2.5], [2, 0]],
    'S': [[0,0],[2, 0], [2, 2.5], [0, 2.5], [0, 5], [2, 5]],
    'T': [[1, 0], [1, 5], [0, 5], [2, 5]],
    'U': [[0, 5], [0, 0], [2, 0], [2, 5]],
    'V': [[0, 5], [1, 0], [2, 5]],
    'W': [[0, 5], [0, 0], [1, 2.5], [2, 0], [2, 5]],
    'X': [[0, 0], [2, 5], [1, 2.5], [0, 5], [2, 0]],
    'Y': [[0, 5], [1, 2.5], [2, 5], [1, 2.5], [1, 0]],
    'Z': [[2, 0], [0, 0], [2, 5], [0, 5]]
}

# Función para calcular los ángulos 
def calcular_angulos(x, y):
    b = np.sqrt(x**2 + y**2)
    cos_theta2 = (b**2 - l1**2 - l2**2) / (2 * l1 * l2)
    sen_theta2 = np.sqrt(1 - cos_theta2**2)
    theta2 = np.arctan2(sen_theta2, cos_theta2)
    alpha = np.arctan2(y, x)
    phi = np.arctan2(l2 * sen_theta2, l1 + l2 * cos_theta2)
    theta1 = alpha - phi
    return theta1, theta2

# Función para trazar una palabra (cinemática inversa)
def trazar_palabra(palabra):
    plt.figure(figsize=(8, 6))
    for letra in palabra:
        if letra.upper() in coordenadas_letras:
            coordenadas = coordenadas_letras[letra.upper()]
            for i in range(len(coordenadas) - 1):
                x0, y0 = coordenadas[i]
                x1, y1 = coordenadas[i + 1]
                dx = x1 - x0
                dy = y1 - y0
                theta1, theta2 = calcular_angulos(dx, dy)
                plt.plot([x0, x1], [y0, y1], 'k-')
                plt.plot(x0, y0, 'bo')
                plt.plot(x1, y1, 'ro')
                print(f'Angulos para ({x1}, {y1}): theta1={np.degrees(theta1):.2f}, theta2={np.degrees(theta2):.2f}')
                # Enviar los ángulos al robot 
        else:
            print(f'La letra "{letra}" no está definida.')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Trazado del nombre "{palabra}"')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    plt.savefig('temp.png')
    #plt.close()
    

# Definición de la clase de la ventana principal de la aplicación
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(587, 500)
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(210, 0, 171, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../Taller 2 - Qt Designer/logoECCI.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 500, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 101, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.imprimir = QtWidgets.QPushButton(self.centralwidget)
        self.imprimir.setGeometry(QtCore.QRect(430, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imprimir.setFont(font)
        self.imprimir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 69, 201);")
        self.imprimir.setObjectName("imprimir")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 160, 291, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.grafico = QtWidgets.QGraphicsView(self.centralwidget)
        self.grafico.setGeometry(QtCore.QRect(10, 220, 561, 241))
        self.grafico.setObjectName("grafico")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #Imprime nombre de la lista
        self.imprimir.clicked.connect(self.trazar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TALLER III - EJERCICIO 4"))
        self.comboBox.setItemText(0, _translate("MainWindow", "KAREN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "CAMILO"))
        self.comboBox.setItemText(2, _translate("MainWindow", "JUAN"))
        self.comboBox.setItemText(3, _translate("MainWindow", "STEVEN"))
        self.comboBox.setItemText(4, _translate("MainWindow", "SERGIO"))
        self.comboBox.setItemText(5, _translate("MainWindow", "OTRO"))
        self.imprimir.setText(_translate("MainWindow", "IMPRIMIR"))
        self.label_2.setText(_translate("MainWindow", "NOMBRES:"))
        self.label_7.setText(_translate("MainWindow", "INGRESE UN NUEVO NOMBRE:"))
        

    def trazar(self):
        palabra = self.comboBox.currentText()
        if palabra == "OTRO":
            nombreX = self.textEdit.toPlainText()
            pass
        else:
            trazar_palabra(palabra)      
        scene = QtWidgets.QGraphicsScene()  # Crear una nueva escena
        pixmap = QtGui.QPixmap('temp.png')
        scene.addPixmap(pixmap)  # Agregar la imagen a la escena
        self.grafico.setScene(scene)  # Asignar la escena al QGraphicsView

# Ejecución de la aplicación
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
