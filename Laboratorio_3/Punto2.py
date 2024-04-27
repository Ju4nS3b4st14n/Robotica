from PyQt5 import QtCore, QtGui, QtWidgets
from roboticstoolbox import *
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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

        self.robot()

    def robot(self):
        l1 = 6
        l2 = 8

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

        Robot = DHRobot(R, name='Bender')

        for i in range(0, 181, 10):
            q1 = np.deg2rad(0)
            self.label_6.setText(str(np.rad2deg(q1)))
            q2 = np.deg2rad(i)
            self.label_5.setText(str(np.rad2deg(q2)))

            self.plot_robot(Robot, q1, q2)

            sleep(0.1)

        for i in range(0, 181, 10):
            q1 = np.deg2rad(i)
            self.label_6.setText(str(np.rad2deg(q1)))
            q2 = np.deg2rad(0)
            self.label_5.setText(str(np.rad2deg(q2)))

            self.plot_robot(Robot, q1, q2)

            sleep(0.1)

        for i in range(0, 181, 10):
            q1 = np.deg2rad(180)
            self.label_6.setText(str(np.rad2deg(q1)))
            q2 = np.deg2rad(i)
            self.label_5.setText(str(np.rad2deg(q2)))

            self.plot_robot(Robot, q1, q2)
            sleep(0.1)

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


