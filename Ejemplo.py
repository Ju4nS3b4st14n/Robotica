from PyQt5 import QtCore, QtGui, QtWidgets
from roboticstoolbox import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import RPi.GPIO as GPIO
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
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 40, 104, 25))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 70, 104, 25))
        self.textEdit_2.setObjectName("textEdit_2")
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

        self.textEdit.textChanged.connect(self.robot)
        self.textEdit_2.textChanged.connect(self.robot)

        self.selected_motor = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Articulación 1"))
        self.label_4.setText(_translate("MainWindow", "Articulación 2"))

    def robot(self):
        l1 = 6
        l2 = 8
        # Cinemática inversa
        x = self.textEdit.toPlainText()
        y = self.textEdit_2.toPlainText()
        Px = int(x)
        Py = int(y)

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
        self.label_6.setText(str(np.rad2deg(q1)))
        q2 = theta2
        self.label_5.setText(str(np.rad2deg(q2)))

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

        Robot = DHRobot(R, name='Bender')

        # self.selected_motor = 33
        # self.selected_motor = 35

        self.plot_robot(Robot, q1, q2)

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

        self.move_robot(q1, q2)

    def move_robot(self, q1, q2):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        pulso_q1 = GPIO.PWM(33, 50)
        pulso_q2 = GPIO.PWM(35, 50)
        pulso_q1.start(1.5)
        pulso_q2.start(1.5)

        grados_q1 = ((1.0/18.0) * q1) + 2.5 
        pulso_q1.ChangeDutyCycle(grados_q1)
        sleep(0.01)
        pulso_q1.stop()
        GPIO.cleanup()

        grados_q2 = ((1.0/18.0) * q2) + 2.5 
        pulso_q2.ChangeDutyCycle(grados_q2)
        sleep(0.01)
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


