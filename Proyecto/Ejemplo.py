from PyQt5 import QtCore, QtGui, QtWidgets
import time   
from adafruit_servokit import ServoKit 
import sys
import board
import busio
from adafruit_pca9685 import PCA9685
import math
import numpy
from sympy import *
from InverseKinematics3R import *
from ForwardKinematics3R import *
import matplotlib.pyplot as plt
from gpiozero import *
   
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalSlider_motor1 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_motor1.setGeometry(QtCore.QRect(100, 80, 201, 20))
                self.horizontalSlider_motor1.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_motor1.setObjectName("horizontalSlider_motor1")
                self.horizontalSlider_motor1.setRange(1, 179)
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(30, 80, 58, 18))
                self.label.setObjectName("label")
                self.horizontalSlider_motor2 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_motor2.setGeometry(QtCore.QRect(100, 110, 201, 20))
                self.horizontalSlider_motor2.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_motor2.setObjectName("horizontalSlider_motor2")
                self.horizontalSlider_motor2.setRange(1, 179)
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(30, 110, 58, 18))
                self.label_2.setObjectName("label_2")
                self.horizontalSlider_motor3 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_motor3.setGeometry(QtCore.QRect(100, 140, 201, 20))
                self.horizontalSlider_motor3.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_motor3.setObjectName("horizontalSlider_motor3")
                self.horizontalSlider_motor3.setRange(1, 179)
                initial_value = int((180 - 0) / 2)  # Valor inicial en la mitad
                self.horizontalSlider_motor3.setValue(initial_value)
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(30, 140, 58, 18))
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(150, 10, 291, 20))
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(160, 170, 58, 18))
                self.label_5.setObjectName("label_5")
                self.pushButton_pick = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_pick.setGeometry(QtCore.QRect(40, 200, 88, 34))
                self.pushButton_pick.setObjectName("pushButton_pick")
                self.pushButton_PLACE = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_PLACE.setGeometry(QtCore.QRect(230, 200, 88, 34))
                self.pushButton_PLACE.setObjectName("pushButton_PLACE")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(120, 50, 131, 18))
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(420, 50, 211, 20))
                self.label_7.setObjectName("label_7")
                self.pos_x = QtWidgets.QLineEdit(self.centralwidget)
                self.pos_x.setGeometry(QtCore.QRect(470, 80, 121, 31))
                self.pos_x.setObjectName("pos_x")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(420, 90, 58, 18))
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(420, 130, 58, 18))
                self.label_9.setObjectName("label_9")
                self.pos_y = QtWidgets.QLineEdit(self.centralwidget)
                self.pos_y.setGeometry(QtCore.QRect(470, 120, 121, 31))
                self.pos_y.setObjectName("pos_y")
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(420, 170, 58, 18))
                self.label_10.setObjectName("label_10")
                self.pos_z = QtWidgets.QLineEdit(self.centralwidget)
                self.pos_z.setGeometry(QtCore.QRect(470, 160, 121, 31))
                self.pos_z.setObjectName("pos_z")
                self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_go.setGeometry(QtCore.QRect(480, 210, 88, 34))
                self.pushButton_go.setObjectName("pushButton_go")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(120, 280, 161, 18))
                self.label_11.setObjectName("label_11")
                self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_start.setGeometry(QtCore.QRect(150, 320, 88, 34))
                self.pushButton_start.setObjectName("pushButton_start")
                self.label_12 = QtWidgets.QLabel(self.centralwidget)
                self.label_12.setGeometry(QtCore.QRect(270, 400, 200, 200))
                self.label_12.setText("")
                self.label_12.setPixmap(QtGui.QPixmap("/home/luis/Documentos/logo-universidad-ecci (1).png"))
                self.label_12.setObjectName("label_12")
                self.label_13 = QtWidgets.QLabel(self.centralwidget)
                self.label_13.setGeometry(QtCore.QRect(10, 407, 241, 31))
                self.label_13.setObjectName("label_13")
                self.label_14 = QtWidgets.QLabel(self.centralwidget)
                self.label_14.setGeometry(QtCore.QRect(10, 440, 181, 18))
                self.label_14.setObjectName("label_14")
                self.label_15 = QtWidgets.QLabel(self.centralwidget)
                self.label_15.setGeometry(QtCore.QRect(10, 470, 191, 18))
                self.label_15.setObjectName("label_15")
                self.label_16 = QtWidgets.QLabel(self.centralwidget)
                self.label_16.setGeometry(QtCore.QRect(10, 530, 121, 20))
                self.label_16.setObjectName("label_16")
                self.label_17 = QtWidgets.QLabel(self.centralwidget)
                self.label_17.setGeometry(QtCore.QRect(10, 500, 121, 20))
                self.label_17.setObjectName("label_17")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
        
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.i2c=busio.I2C(board.SCL,board.SDA)
                self.pca=PCA9685(self.i2c)
                self.kit = ServoKit(channels=16)
                self.pca.frequency=60
                self.horizontalSlider_motor1.valueChanged.connect(self.manual)
                self.horizontalSlider_motor2.valueChanged.connect(self.manual)
                self.horizontalSlider_motor3.valueChanged.connect(self.manual)
                self.pushButton_go.clicked.connect(self.semi_auto)
                self.pushButton_pick.clicked.connect(self.gripperPick)
                self.pushButton_PLACE.clicked.connect(self.gripperPlace)
                self.pushButton_start.clicked.connect(self.auto)

                #self.sensor = DistanceSensor(echo=14, trigger=4)
                #self.sensor2 = DistanceSensor(echo=17, trigger=18)
                self.sensor3 = DistanceSensor(echo=14, trigger=4)

                self.plot_robot_figure()
        
       
        def manual(self):
                
                theta1=self.horizontalSlider_motor1.value()
                theta2=self.horizontalSlider_motor2.value()
                theta3=self.horizontalSlider_motor3.value()
                
                self.mover_servos_manual(theta1,theta2,theta3)
                #self.plot_robot(q1, q2, q3)
       
        def semi_auto(self):
            
                l1 = 4
                l2 = 8
                l3 = 18
                
                n = 90
                
                x = self.pos_x.text()
                y = self.pos_y.text()
                z = self.pos_z.text()

                if x == '' or y == '' or z == '' or x == '-' or y == '-' or z == '-' :

                    x = 26
                    y = 0
                    z = 4

                if x == 0 and y == 0 and z == 0 :

                    x = 26
                    y = 0
                    z = 4
                
                # Cinemática inversa
                # Punto 1
                P1x = 26
                P1y = 0
                P1z = 4

                [theta1_P1, theta2_P1, theta3_P1] = InverseKinematics3R(l1,l2,l3,P1x,P1y,P1z)
                
                # Punto 2
                P2x = int(x)
                P2y = int(y)
                P2z = int(z)

                [theta1_P2, theta2_P2, theta3_P2] = InverseKinematics3R(l1,l2,l3,P2x,P2y,P2z)

                theta1_P1toP2 = numpy.linspace(theta1_P1, theta1_P2, n)
                theta2_P1toP2 = numpy.linspace(theta2_P1, theta2_P2, n)
                theta3_P1toP2 = numpy.linspace(theta3_P1, theta3_P2, n)

                for i in range (0,n):
                    print(i)
                    [q1, q2, q3] = (theta1_P1toP2[i],theta2_P1toP2[i],theta3_P1toP2[i])
                    print(q1, q2, q3)
                    self.mover_servos_semi(q1,q2,q3)
                    
                #self.plot_robot(q1, q2, q3)
                
        def auto(self):

            l1 = 4
            l2 = 8
            l3 = 18
            n = 100
            self.gripperPlace(0)

            # Cinemática inversa
            # Punto 1
            P1x = 26
            P1y = 0
            P1z = 4

            [theta1_P1, theta2_P1, theta3_P1] = InverseKinematics3R(l1,l2,l3,P1x,P1y,P1z)

            # Punto 2
            P2x = 18
            P2y = 0
            P2z = 12

            [theta1_P2, theta2_P2, theta3_P2] = InverseKinematics3R(l1,l2,l3,P2x,P2y,P2z)
            
            theta1_P1toP2 = numpy.linspace(theta1_P1, theta1_P2, n)
            theta2_P1toP2 = numpy.linspace(theta2_P1, theta2_P2, n)
            theta3_P1toP2 = numpy.linspace(theta3_P1, theta3_P2, n)

            for i in range (0,n):
                print(i)
                [q1, q2, q3] = (theta1_P1toP2[i],theta2_P1toP2[i],theta3_P1toP2[i])
                print(q1, q2, q3)
                self.mover_servos_semi(q1,q2,q3)
            
            self.gripperPick()
            time.sleep(2)

            # Punto 3
            P3x = 14
            P3y = 4
            P3z = 0

            [theta1_P3, theta2_P3, theta3_P3] = InverseKinematics3R(l1,l2,l3,P3x,P3y,P3z)
            
            theta1_P1toP3 = numpy.linspace(theta1_P2, theta1_P3, n)
            theta2_P1toP3 = numpy.linspace(theta2_P2, theta2_P3, n)
            theta3_P1toP3 = numpy.linspace(theta3_P2, theta3_P3, n)

            for i in range (0,n):
                print(i)
                [q1, q2, q3] = (theta1_P1toP3[i],theta2_P1toP3[i],theta3_P1toP3[i])
                print(q1, q2, q3)
                self.mover_servos_semi(q1,q2,q3)
                
            self.gripperPlace(30)
            time.sleep(2)
            
            # Punto 4
            P4x = 18
            P4y = 0
            P4z = 12

            [theta1_P4, theta2_P4, theta3_P4] = InverseKinematics3R(l1,l2,l3,P4x,P4y,P4z)

            theta1_P1toP4 = numpy.linspace(theta1_P3, theta1_P4, n)
            theta2_P1toP4 = numpy.linspace(theta2_P3, theta2_P4, n)
            theta3_P1toP4 = numpy.linspace(theta3_P3, theta3_P4, n)

            for i in range (0,n):
                print(i)
                [q1, q2, q3] = (theta1_P1toP4[i],theta2_P1toP4[i],theta3_P1toP4[i])
                print(q1, q2, q3)
                self.mover_servos_semi(q1,q2,q3)
                
            # Punto 5
            P5x = 0
            P5y = 18
            P5z = 12

            [theta1_P5, theta2_P5, theta3_P5] = InverseKinematics3R(l1,l2,l3,P5x,P5y,P5z)

            theta1_P1toP5 = numpy.linspace(theta1_P4, theta1_P5, n)
            theta2_P1toP5 = numpy.linspace(theta2_P4, theta2_P5, n)
            theta3_P1toP5 = numpy.linspace(theta3_P4, theta3_P5, n)

            for i in range (0,n):
                print(i)
                [q1, q2, q3] = (theta1_P1toP5[i],theta2_P1toP5[i],theta3_P1toP5[i])
                print(q1, q2, q3)
                self.mover_servos_semi(q1,q2,q3)
                
            # Punto 6
            P6x = 0
            P6y = 14
            P6z = 0

            [theta1_P6, theta2_P6, theta3_P6] = InverseKinematics3R(l1,l2,l3,P6x,P6y,P6z)

            theta1_P1toP6 = numpy.linspace(theta1_P5, theta1_P6, n)
            theta2_P1toP6 = numpy.linspace(theta2_P5, theta2_P6, n)
            theta3_P1toP6 = numpy.linspace(theta3_P5, theta3_P6, n)

            for i in range (0,n):
                print(i)
                [q1, q2, q3] = (theta1_P1toP6[i],theta2_P1toP6[i],theta3_P1toP6[i])
                print(q1, q2, q3)
                self.mover_servos_semi(q1,q2,q3)
                
            self.gripperPick()
            
            # Punto 6
            P7x = 0
            P7y = 18
            P7z = 12

            [theta1_P7, theta2_P7, theta3_P7] = InverseKinematics3R(l1,l2,l3,P7x,P7y,P7z)

            theta1_P1toP7 = numpy.linspace(theta1_P6, theta1_P7, n)
            theta2_P1toP7 = numpy.linspace(theta2_P6, theta2_P7, n)
            theta3_P1toP7 = numpy.linspace(theta3_P6, theta3_P7, n)

            for i in range (0,n):
                print(i)
                [q1, q2, q3] = (theta1_P1toP7[i],theta2_P1toP7[i],theta3_P1toP7[i])
                print(q1, q2, q3)
                self.mover_servos_semi(q1,q2,q3)
                
        def ajustar_angulo(self, angle):
                while angle < 0:
                    angle += numpy.pi
                while angle > numpy.pi:
                    angle -= numpy.pi
                return angle

        def mover_servos_manual(self, q1s,q2s,q3s):
            
#                 distancia = self.sensor.distance
#                 distancia2 = self.sensor2.distance
                #distancia3 = self.sensor3.distance
                
                q3s = 180 - q3s
                
                if q1s == 0:
                    q1s = 5
                    
                elif  q1s == 180:
                    q1s = 175
                
                if q2s == 0:
                    q2s = 5
                    
                elif  q2s == 180:
                    q2s = 175
                    
                if q3s == 0:
                    q3s = 5
                    
                elif  q3s == 180:
                    q3s = 175
        
#                 if distancia3 < 0.10:
#                     print(distancia3)
#                     
#                     pulso = int((q1s/24) * (1970-980) + 980)
#                     self.pca.channels[4].duty_cycle = pulso
#                 
#                     pulso2 = int((q2s/21) * (1970-980) + 980)
#                     self.pca.channels[15].duty_cycle = pulso2
#               
#                     pulso3 = int((q3s/27) * (1970-980) + 980)
#                     self.pca.channels[2].duty_cycle = pulso3
#                     
#                     time.sleep(0.5)
#                 
#                 
#                 if distancia < 0.26 or distancia2 < 0.26 :
#                     pulso = int((q1s/24) * (1970-980) + 980)
#                     self.pca.channels[4].duty_cycle = 0
#                 
#                     pulso2 = int((q2s/21) * (1970-980) + 980)
#                     self.pca.channels[15].duty_cycle = 0
#               
#                     pulso3 = int((q3s/27) * (1970-980) + 980)
#                     self.pca.channels[2].duty_cycle = 0
           
                
                pulso = int((q1s/24) * (1970-980) + 980)
                self.pca.channels[4].duty_cycle = pulso
                
                pulso2 = int((q2s/21) * (1970-980) + 980)
                self.pca.channels[15].duty_cycle = pulso2
              
                pulso3 = int((q3s/27) * (1970-980) + 980)
                self.pca.channels[2].duty_cycle = pulso3
                
        def mover_servos_semi(self, q1s, q2s, q3s):
            
#                 distancia = self.sensor.distance
#                 distancia2 = self.sensor2.distance
                #distancia3 = self.sensor3.distance
                #print(distancia3)
                
                q3s = 180 - q3s
                
                if q1s == 0:
                    q1s = 5
                    
                elif  q1s == 180:
                    q1s = 175
                
                if q2s == 0:
                    q2s = 5
                    
                elif  q2s == 180:
                    q2s = 175
                    
                if q3s == 0:
                    q3s = 5
                    
                elif  q3s == 180:
                    q3s = 175
                    
#                 if distancia3 < 0.10:
#                     
#                     pulso = int((q1s/24) * (1970-980) + 980)
#                     self.pca.channels[4].duty_cycle = pulso
#                 
#                     pulso2 = int((q2s/21) * (1970-980) + 980)
#                     self.pca.channels[15].duty_cycle = pulso2
#               
#                     pulso3 = int((q3s/27) * (1970-980) + 980)
#                     self.pca.channels[2].duty_cycle = pulso3
#                     
#                     time.sleep(0.5)
#                 
#                 
#                 if distancia < 0.26 or distancia2 < 0.26 :
#                     
#                     pulso = int((q1s/24) * (1970-980) + 980)
#                     self.pca.channels[4].duty_cycle = 0
#                 
#                     pulso2 = int((q2s/21) * (1970-980) + 980)
#                     self.pca.channels[15].duty_cycle = 0
#               
#                     pulso3 = int((q3s/27) * (1970-980) + 980)
#                     self.pca.channels[2].duty_cycle = 0
                    
                    
                pulso = int((q1s/24) * (1970-980) + 980)
                self.pca.channels[4].duty_cycle = pulso
                
                pulso2 = int((q2s/21) * (1970-980) + 980)
                self.pca.channels[15].duty_cycle = pulso2
              
                pulso3 = int((q3s/27) * (1970-980) + 980)
                self.pca.channels[2].duty_cycle = pulso3
                    
                time.sleep(0.09)
              

        def gripperPick(self):
              
            self.kit.servo[3].angle=90

        def gripperPlace(self, q):
              
            self.kit.servo[3].angle=q

        def plot_robot_figure(self):

            l1 = 4
            l2 = 8
            l3 = 18

            R = []
            R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
            R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
            R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=0))

            self.Robot = DHRobot(R, name='Bender')

        def plot_robot(self, q1, q2, q3):

            self.Robot.plot([q1, q2, q3], backend='pyplot', limits=[-30, 30, -30, 30, -30, 30])
        
        
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">MOTOR-1</span></p></body></html>"))
                self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">MOTOR-2</span></p></body></html>"))
                self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">MOTOR-3</span></p></body></html>"))
                self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#aa0000;\">CELDA ROBOTIZADA-ROBOT DE 3DOF</span></p></body></html>"))
                self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Gripper</span></p></body></html>"))
                self.pushButton_pick.setText(_translate("MainWindow", "PICK"))
                self.pushButton_PLACE.setText(_translate("MainWindow", "PLACE"))
                self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">MODO: MANUAL</span></p></body></html>"))
                self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">MODO: SEMI-AUTOMATICO</span></p></body></html>"))
                self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aaff;\">POS X:</span></p></body></html>"))
                self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aaff;\">POS Y:</span></p></body></html>"))
                self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aaff;\">POS Z:</span></p></body></html>"))
                self.pushButton_go.setText(_translate("MainWindow", "GO!"))
                self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#aa557f;\">MODO:AUTOMATICO</span></p></body></html>"))
                self.pushButton_start.setText(_translate("MainWindow", "¡START!"))
                self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Juan Sebastian Torres</span></p></body></html>"))
                self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Steven Santana</span></p></body></html>"))
                self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Juan Alberto Celemin</span></p></body></html>"))
                self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Sergio Lopez</span></p></body></html>"))
                self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Karen Mantilla</p></body></html>"))
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

