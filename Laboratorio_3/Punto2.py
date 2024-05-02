from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from roboticstoolbox import *
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import RPi.GPIO as GPIO
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        QTimer.singleShot(100, self.robot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Punto 2"))
        # # 
        self.label_8.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_9.setText(_translate("MainWindow", "Juan Camilo Alberto"))
        self.label_10.setText(_translate("MainWindow", "Sergio Andres Lopez"))
        self.label_11.setText(_translate("MainWindow", "Steven Santana"))
        self.label_12.setText(_translate("MainWindow", "Karen Mancilla"))

        #self.robot()

    def robot(self):
        l1 = 6
        l2 = 8

        n = 181
        d = np.zeros((3,n))

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

        Robot = DHRobot(R, name='Bender')
        fig1 = self.plot_fig()

        for i in range(0, n, 20):
            q1 = np.deg2rad(0)
            # self.label_6.setText(str(np.rad2deg(q1)))
            q2 = np.deg2rad(i)
            # self.label_5.setText(str(np.rad2deg(q2)))

            MTH = Robot.fkine([q1,q2])
            d[:,i] =  MTH.t 
            self.move_robot(q1, q2)
            self.plot_path(fig1, d, i)
            self.plot_robot(Robot, q1, q2)
            sleep(0.05)
            
        for i in range(n, 0, -20):
            q1 = np.deg2rad(0)
            # self.label_6.setText(str(np.rad2deg(q1)))
            q2 = np.deg2rad(i)
            # self.label_5.setText(str(np.rad2deg(q2)))

            self.move_robot(q1, q2)
            self.plot_robot(Robot, q1, q2)
            sleep(0.05)

        for i in range(0, n, 20):
            q1 = np.deg2rad(i)
            # self.label_6.setText(str(np.rad2deg(q1)))
            q2 = np.deg2rad(0)
            # self.label_5.setText(str(np.rad2deg(q2)))

            MTH = Robot.fkine([q1,q2])
            d[:,i] =  MTH.t 
            self.move_robot(q1, q2)
            self.plot_path(fig1, d, i)
            self.plot_robot(Robot, q1, q2)
            sleep(0.05)

        for i in range(0, n, 20):
            q1 = np.deg2rad(180)
            # self.label_6.setText(str(np.rad2deg(q1)))
            q2 = np.deg2rad(i)
            # self.label_5.setText(str(np.rad2deg(q2)))

            MTH = Robot.fkine([q1,q2])
            d[:,i] =  MTH.t 
            self.move_robot(q1, q2)
            self.plot_path(fig1, d, i)
            self.plot_robot(Robot, q1, q2)
            sleep(0.05)

    def plot_robot(self, robot, q1, q2):

        robot.plot([q1, q2], backend='pyplot', limits=[-20, 20, -20, 20, -20, 20])

    def plot_path(self, fig1, d, i):
        fig1.plot(d[0,i],d[1,i],d[2,i],'.b')
        self.canvas.draw()

    def plot_fig(self):

        fig = Figure()
        fig1 = fig.add_subplot(projection='3d')
        fig1.set_xlabel('X')
        fig1.set_ylabel('Y')
        fig1.set_zlabel('Z')
        fig1.set_xlim(-30, 30)
        fig1.set_ylim(-30, 30)
        fig1.set_zlim(-30, 30)

        self.canvas = FigureCanvas(fig)
        layout = QtWidgets.QVBoxLayout(self.label_7)
        layout.addWidget(self.canvas)
        
        return fig1
        
    def move_robot(self, q1, q2):
        
        q1s = int(np.rad2deg(q1))
        q2s = int(np.rad2deg(q2))

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(33, GPIO.OUT)
        pulso_q1 = GPIO.PWM(33, 50)
        pulso_q1.start(1.5)
        grados_q1 = ((1.0/18.0) * q1s) + 2.5
        pulso_q1.ChangeDutyCycle(grados_q1)
        sleep(0.1)
        pulso_q1.stop()
        
        GPIO.setup(35, GPIO.OUT)
        pulso_q2 = GPIO.PWM(35, 50)
        pulso_q2.start(1.5)
        grados_q2 = ((1.0/18.0) * q2s) + 2.5
        pulso_q2.ChangeDutyCycle(grados_q2)
        sleep(0.1)
        pulso_q2.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

