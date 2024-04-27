from PyQt5 import QtCore, QtGui, QtWidgets
from roboticstoolbox import *
import numpy as np
import cv2


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

        # Llamar a la función para procesar la imagen y obtener las coordenadas
        coordenadas_x, coordenadas_y = self.obtener_coordenadas_imagen()
        self.robot(coordenadas_x, coordenadas_y)

    def robot(self, coordenadas_x, coordenadas_y):
        l1 = 6
        l2 = 8

        # Iterar sobre las coordenadas X e Y
        for x, y in zip(coordenadas_x, coordenadas_y):
            # Realizar el cálculo de la cinemática inversa para las coordenadas x, y
            Px = x
            Py = y

            b = np.sqrt(Px ** 2 + Py ** 2)
            # Theta 2
            cos_theta2 = (b ** 2 - l2 ** 2 - l1 ** 2) / (2 * l1 * l2)
            sen_theta2 = np.sqrt(1 - (cos_theta2) ** 2)
            theta2 = np.arctan2(sen_theta2, cos_theta2)

            # Theta 1
            alpha = np.arctan2(Py, Px)
            phi = np.arctan2(l2 * sen_theta2, l1 + l2 * cos_theta2)
            theta1 = alpha - phi

            q1 = theta1
            q2 = theta2

            R = []
            R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
            R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

            Robot = DHRobot(R, name='Bender')

            # Llamar a la función plot_robot con las coordenadas calculadas
            #self.plot_robot(Robot, q1, q2)

            print(Robot)

            Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

            #zlim([-15,30]);

            MTH = Robot.fkine([q1,q2])
            print(MTH)
            #print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, "deg", "zyx")}')
            

    def plot_robot(self, robot, q1, q2):
        # Tu código para plotear el robot
        print(Robot)

        Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

        #zlim([-15,30]);

        MTH = Robot.fkine([q1,q2])
        print(MTH)
        #print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, "deg", "zyx")}')

    # Función para procesar la imagen y obtener las coordenadas
    def obtener_coordenadas_imagen(self):
        img = cv2.imread('../Robotica/Laboratorio_3/Imagenes/Mercedes.jpg')

        # Obtener las coordenadas de los contornos u otras características de la imagen
        # Por ejemplo, aquí se obtienen las coordenadas de los contornos
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        _, binaria = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        coordenadas_x = []
        coordenadas_y = []

        for contour in contornos:
            for punto in contour:
                x, y = punto[0]
                coordenadas_x.append(x)
                coordenadas_y.append(y)

        return coordenadas_x, coordenadas_y


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
