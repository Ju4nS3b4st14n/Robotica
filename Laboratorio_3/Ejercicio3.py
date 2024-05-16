from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
from roboticstoolbox import *
import numpy as np
import cv2  # Importar OpenCV
import math
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
#import RPi.GPIO as GPIO
from time import sleep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 40, 104, 25))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 70, 104, 25))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 21, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 21, 25))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QWidget(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 100, 551, 371))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(396, 40, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(396, 70, 101, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 70, 67, 17))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 40, 67, 17))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 510, 160, 25))
        self.label_8.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 600, 160, 25))
        self.label_9.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 630, 160, 25))
        self.label_10.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 540, 160, 25))
        self.label_11.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 570, 160, 25))
        self.label_12.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(500, 510, 221, 151))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../Robotica/Laboratorio_3/Imagenes/images.png"))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 118, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 500, 191, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 550, 191, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.fig = Figure()
        self.fig1 = self.fig.add_subplot(projection='3d')
        self.fig1.set_xlabel('X')
        self.fig1.set_ylabel('Y')
        self.fig1.set_zlabel('Z')
        self.fig1.set_xlim(-10, 10)
        self.fig1.set_ylim(0, 10)
        self.fig1.set_zlim(0, 10)

        self.canvas = FigureCanvas(self.fig)
        layout = QtWidgets.QVBoxLayout(self.label_7)
        layout.addWidget(self.canvas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Punto 2"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Articulación 1"))
        self.label_4.setText(_translate("MainWindow", "Articulación 2"))
        self.label_8.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_9.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_10.setText(_translate("MainWindow", "Sergio Andres Lopez"))
        self.label_11.setText(_translate("MainWindow", "Steven Santana"))
        self.label_12.setText(_translate("MainWindow", "Karen Mancilla"))
        self.pushButton.setText(_translate("MainWindow", "Iniciar"))
        self.comboBox.addItem("Selecciona un logo")
        self.comboBox.addItem("Chevrolet")
        self.comboBox.addItem("Renault")
        self.comboBox.addItem("Mercedes")
        self.comboBox.addItem("Kia")
        self.comboBox_2.addItem("Selecciona un nombre")
        self.comboBox_2.addItem("SERGIO")
        self.comboBox_2.addItem("JUAN")
        self.comboBox_2.addItem("CAMILO")
        self.comboBox_2.addItem("KAREN")
        self.comboBox_2.addItem("STEVEN")
        

        self.pushButton.clicked.connect(self.robot)
        self.comboBox.currentTextChanged.connect(self.cars)
        self.comboBox_2.currentTextChanged.connect(self.Names)

    def robot(self):

        l1 = 6
        l2 = 8

        n = 181
        d = np.zeros((3,n))

        # Cinemática inversa
        x = self.textEdit.toPlainText()
        y = self.textEdit_2.toPlainText()

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

        Robot = DHRobot(R, name='Bender')

        if x == '' or y == '':

            for i in range(0, n, 20):
                q1 = np.deg2rad(0)
                q2 = np.deg2rad(i)

                MTH = Robot.fkine([q1,q2])
                d[:,i] =  MTH.t 
                self.move_robot(q1, q2)
                self.plot_path(d, i)
                self.plot_robot(Robot, q1, q2)
                sleep(0.05)
            
            for i in range(n, 0, -20):
                q1 = np.deg2rad(0)
                q2 = np.deg2rad(i)

                self.move_robot(q1, q2)
                self.plot_robot(Robot, q1, q2)
                sleep(0.05)

            for i in range(0, n, 20):
                q1 = np.deg2rad(i)
                q2 = np.deg2rad(0)
                
                MTH = Robot.fkine([q1,q2])
                d[:,i] =  MTH.t 
                self.move_robot(q1, q2)
                self.plot_path(d, i)
                self.plot_robot(Robot, q1, q2)
                sleep(0.05)

            for i in range(0, n, 20):
                q1 = np.deg2rad(180)
                q2 = np.deg2rad(i)

                MTH = Robot.fkine([q1,q2])
                d[:,i] =  MTH.t 
                self.move_robot(q1, q2)
                self.plot_path(d, i)
                self.plot_robot(Robot, q1, q2)
                sleep(0.05)

        if x != '' and y != '':

            Px = int(x)
            Py = int(y)

            b = math.sqrt(Px**2+Py**2)
            # Theta 2
            cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
            sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
            theta2 = math.atan2(sen_theta2, cos_theta2)
            # Theta 1
            alpha = math.atan2(Py,Px)
            phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
            theta1 = alpha - phi

            if theta1 <= -np.pi:
                theta1 = (2*np.pi)+theta1        

            q1 = theta1
            q2 = theta2

            if q2 <= -np.pi:
                q2 = (2*np.pi)+q2
                
            if np.isnan(q1) or np.isnan(q2):
                q1 = 0
                q2 = 0

            self.move_robot(q1, q2)
            self.plot_path1(Px, Py)
            self.plot_robot(Robot, q1, q2)  

    def cars(self, seleccion):

        # Define las rutas de las imágenes según la opción seleccionada
        if seleccion == "Chevrolet":
            # Leer la imagen con OpenCV
            img = cv2.imread('../Robotica/Laboratorio_3/Imagenes/Chevrolet.jpg')
        elif seleccion == "Renault":
            img = cv2.imread('../Robotica/Laboratorio_3/Imagenes/Renault.png')
        elif seleccion == "Mercedes":
            img = cv2.imread('../Robotica/Laboratorio_3/Imagenes/Mercedes.png')
        elif seleccion == "Kia":
            img = cv2.imread('../Robotica/Laboratorio_3/Imagenes/Kia2.jpg')

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     

        # Obtener contornos
        _, binaria = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        coordenadas_x = []
        coordenadas_y = []
        
        # Imprimir las coordenadas de los contornos
        for contour in contornos:
            for punto in contour:
                x, y = punto[0]
                coordenadas_x.append(x)
                coordenadas_y.append(y)

        self.robot_cars(coordenadas_x, coordenadas_y, seleccion)

    def robot_cars(self, coordenadas_x, coordenadas_y, seleccion):
        # Restringir el número de coordenadas a procesar
        if seleccion == "Chevrolet":
            coordenadas_x = coordenadas_x[:94]
            coordenadas_y = coordenadas_y[:94]

        elif seleccion == "Renault":
            coordenadas_x = coordenadas_x[:710]
            coordenadas_y = coordenadas_y[:710]

        elif seleccion == "Mercedes":
            coordenadas_x = coordenadas_x[:820]
            coordenadas_y = coordenadas_y[:820]

        elif seleccion == "Kia":
            coordenadas_x = coordenadas_x[:446]
            coordenadas_y = coordenadas_y[:446]

        l1 = 6
        l2 = 8

        d = np.zeros((3, len(coordenadas_x)))

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
        Robot = DHRobot(R, name='Bender')

        for i in range(len(coordenadas_x)):
            x, y = coordenadas_x[i], coordenadas_y[i]
            # Cinemática inversa
            if seleccion == "Chevrolet":
                Px = x/70-5
                Py = y/70+6
            elif seleccion == "Renault":
                Px = x/50-2
                Py = y/50+6
            elif seleccion == "Mercedes":
                Px = x/60-2
                Py = y/60+6
            elif seleccion == "Kia":
                Px = x/70-4
                Py = y/70+6

            b = math.sqrt(Px**2+Py**2)
            # Theta 2
            cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
            sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
            theta2 = math.atan2(sen_theta2, cos_theta2)
        
            # Theta 1
            alpha = math.atan2(Py,Px)
            phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
            theta1 = alpha - phi
        
            if theta1 <= -np.pi:
                theta1 = (2*np.pi)+theta1 

            q1 = theta1
            q2 = theta2

            if q2 <= -np.pi:
                q2 = (2*np.pi)+q2

            MTH = Robot.fkine([q1,q2])
            d[:, i] =  MTH.t 

            self.plot_path4(d, i)
            #self.move_robot(self, q1, q2)
            #self.plot_robot(Robot, q1, q2)

    def Names(self, palabra):
        
        coordenadas_letras = {
        # Definir los puntos para cada letra
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
        'Q': [[0, 0], [0, 5], [2, 5], [2, 0], [0, 0], [2, 0],[1,2.5],[2,0]],
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

        nombre = palabra
        print(nombre)

        coordenadas_x = []
        coordenadas_y = []
        espacio_entre_letras = 3  # Espacio entre letras
        current_x = 0

        for letra in palabra:
            if letra.upper() in coordenadas_letras:
                coordenadas = coordenadas_letras[letra.upper()]
                for i in range(len(coordenadas)):
                    x, y = coordenadas[i]
                    coordenadas_x.append(x + current_x)
                    coordenadas_y.append(y)
                current_x += max([x for x, _ in coordenadas]) + espacio_entre_letras

        self.plot_names(coordenadas_x, coordenadas_y)

    def plot_names(self, coordenadas_x, coordenadas_y):

        l1 = 6
        l2 = 8

        d = np.zeros((3, len(coordenadas_x)))

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
        Robot = DHRobot(R, name='Bender')

        for i in range(len(coordenadas_x)):
            x, y = coordenadas_x[i], coordenadas_y[i]
    
            Px = x/2-8
            Py = y/2+4

            b = math.sqrt(Px**2+Py**2)
            # Theta 2
            cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
            sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
            theta2 = math.atan2(sen_theta2, cos_theta2)
        
            # Theta 1
            alpha = math.atan2(Py,Px)
            phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
            theta1 = alpha - phi
        
            if theta1 <= -np.pi:
                theta1 = (2*np.pi)+theta1 

            q1 = theta1
            q2 = theta2

            if q2 <= -np.pi:
                q2 = (2*np.pi)+q2

            MTH = Robot.fkine([q1,q2])
            d[:, i] =  MTH.t 

            self.plot_path4(d, i)
            #self.move_robot(self, q1, q2)
            #self.plot_robot(Robot, q1, q2)


    def plot_robot(self, robot, q1, q2):
        
        self.label_5.setText(str(np.rad2deg(q2)))
        self.label_6.setText(str(np.rad2deg(q1)))
        robot.plot([q1, q2], backend='pyplot', limits=[-20, 20, -20, 20, -20, 20])

    def plot_path(self, d, i):

        self.fig1.plot(d[0,i],d[1,i],d[2,i],'.b')
        self.canvas.draw()

    def plot_path1(self, x, y):

        self.fig1.plot(x, y, 0,'.b')
        self.canvas.draw()

    def plot_path4(self, d, i):

        if i > 0:
            self.fig1.plot([d[0, i-1], d[0, i]], [d[1, i-1], d[1, i]], [d[2, i-1], d[2, i]], color='blue')
        self.canvas.draw()
        
    def move_robot(self, q1, q2):
        
        q1s = int(np.rad2deg(q1))
        q2s = int(np.rad2deg(q2))

    #     GPIO.setmode(GPIO.BOARD)
    #     GPIO.setup(33, GPIO.OUT)
    #     pulso_q1 = GPIO.PWM(33, 50)
    #     pulso_q1.start(1.5)
    #     grados_q1 = ((1.0/18.0) * q1s) + 2.5
    #     pulso_q1.ChangeDutyCycle(grados_q1)
    #     sleep(0.1)
    #     pulso_q1.stop()
        
    #     GPIO.setup(35, GPIO.OUT)
    #     pulso_q2 = GPIO.PWM(35, 50)
    #     pulso_q2.start(1.5)
    #     grados_q2 = ((1.0/18.0) * q2s) + 2.5
    #     pulso_q2.ChangeDutyCycle(grados_q2)
    #     sleep(0.1)
    #     pulso_q2.stop()
    #     GPIO.cleanup()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

