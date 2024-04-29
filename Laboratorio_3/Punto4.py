from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2  # Importar OpenCV
import numpy as np
from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 21, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 21, 25))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QWidget(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 140, 551, 371))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Articulación 1"))
        self.label_4.setText(_translate("MainWindow", "Articulación 2"))

        self.loadImage()
        
    
    
    def loadImage(self):
       
        # Leer la imagen con OpenCV
        img = cv2.imread('../Robotica/Laboratorio_3/Imagenes/Chevrolet.jpg')

        # Obtener las dimensiones de la imagen original
        # alto_original, ancho_original = img.shape[:2]

        # # Definir el nuevo tamaño deseado de la imagen
        # nuevo_ancho = 14  # Nuevo ancho de la imagen
        # nuevo_alto = int(alto_original * (nuevo_ancho / ancho_original))  # Mantener la proporción

        # # Redimensionar la imagen
        # img_redimensionada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     
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
        #self.label.setPixmap(pixmap)

        self.robot(coordenadas_x, coordenadas_y)
    
    def robot(self, coordenadas_x, coordenadas_y):

        l1 = 10
        l2 = 10

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
        Robot = DHRobot(R, name='Bender')

        for x, y in zip(coordenadas_x, coordenadas_y):
            # Cinemática inversa
            Px = x*0.3/10
            Py = y*0.3/10
            print(f"Px {Px}, PY {Py}")
            #sleep(2)

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
            self.label_6.setText(str(np.rad2deg(q1)))
            self.label_5.setText(str(np.rad2deg(q2)))

            self.plot_robot(Robot, q1, q2)

            # print(Robot)

            # Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

            # #zlim([-15,30]);

            # MTH = Robot.fkine([q1,q2])
            # print(MTH)
            # #print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')

    def plot_robot(self, robot, q1, q2):
        fig = Figure()
        
        ax = fig.add_subplot(111, projection='3d')
        robot.plot([q1, q2], backend='pyplot', limits=[-20, 20, -20, 20, -20, 20])
        ax.set_xlim([-20, 20])
        ax.set_ylim([-20, 20])
        ax.set_zlim([-20, 20])
        
        canvas = FigureCanvas(fig)
        layout = QtWidgets.QVBoxLayout(self.label_7)
        layout.addWidget(canvas)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

