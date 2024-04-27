from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2  # Importar OpenCV
import numpy as np
from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 140, 591, 361))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 70, 151, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.loadImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quinto punto"))
        self.pushButton.setText(_translate("MainWindow", "Cargar imagen"))
        self.label_7.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_8.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_9.setText(_translate("MainWindow", "Sergio Andres Lopez"))
        self.label_11.setText(_translate("MainWindow", "Steven Santana"))

        #coordenadas_x, coordenadas_y = loadImage()
        
    
    
    def loadImage(self):
       
        # Leer la imagen con OpenCV
        img = cv2.imread('../Robotica/Laboratorio_3/Imagenes/Mercedes.jpg')

        # Obtener las dimensiones de la imagen original
        alto_original, ancho_original = img.shape[:2]

        # Definir el nuevo tamaño deseado de la imagen
        nuevo_ancho = 14  # Nuevo ancho de la imagen
        nuevo_alto = int(alto_original * (nuevo_ancho / ancho_original))  # Mantener la proporción

        # Redimensionar la imagen
        img_redimensionada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(img_redimensionada, cv2.COLOR_BGR2GRAY)     
        edges = cv2.Canny(gray, 100, 200)

        # Encontrar contornos
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
        # Dibujar contornos en la imagen original
        cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

        # Obtener contornos
        _, binaria = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        coordenadas_x = []
        coordenadas_y = []
        
        # Imprimir las coordenadas de los contornos
        print(f"\n\nCoordenadas Logo\n\n")
        for contour in contornos:
            for punto in contour:
                x, y = punto[0]
                coordenadas_x.append(x)
                coordenadas_y.append(y)
                print(f"Coordenada: X={x}, Y={y}")

            
        # Convertir la imagen de vuelta a formato Qt
        height, width, channels = img.shape
        bytesPerLine = channels * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            
        pixmap = QPixmap.fromImage(qImg)
        self.label.setPixmap(pixmap)

        self.cinematica(coordenadas_x, coordenadas_y)
        #return coordenadas_x, 
    #coordenadas_x, coordenadas_y = loadImage()
    
    def cinematica(self, coordenadas_x, coordenadas_y):

        l1 = 10
        l2 = 10

        for x, y in zip(coordenadas_x, coordenadas_y):
            # Cinemática inversa
            Px = x
            Py = y
            print(x,y)

            b = math.sqrt(Px**2+Py**2)
            # Theta 2
            cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
            sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
            theta2 = math.atan2(sen_theta2, cos_theta2)
            print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
            # Theta 1
            alpha = math.atan2(Py,Px)
            phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
            theta1 = alpha - phi
            print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
            #-------------

            q1 = theta1
            q2 = theta2

            R = []
            R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
            R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

            Robot = DHRobot(R, name='Bender')
            print(Robot)

            Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

            #zlim([-15,30]);

            MTH = Robot.fkine([q1,q2])
            print(MTH)
            #print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

