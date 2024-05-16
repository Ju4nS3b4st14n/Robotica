from PyQt5 import QtCore, QtGui, QtWidgets
import math
import numpy
from sympy import *
from InverseKinematics3R import *
from ForwardKinematics3R import *
import matplotlib.pyplot as plt
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 520)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 581, 501))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.m2_semiautomatico = QtWidgets.QFrame(self.frame_2)
        self.m2_semiautomatico.setGeometry(QtCore.QRect(280, 40, 291, 231))
        self.m2_semiautomatico.setStyleSheet("border-color: rgb(0, 0, 0);\n""gridline-color: rgb(0, 0, 0);")
        self.m2_semiautomatico.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m2_semiautomatico.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m2_semiautomatico.setObjectName("m2_semiautomatico")
        self.label_5 = QtWidgets.QLabel(self.m2_semiautomatico)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 280, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.m2_semiautomatico)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.m2_semiautomatico)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.m2_semiautomatico)
        self.label_8.setGeometry(QtCore.QRect(40, 120, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.go_semiauto = QtWidgets.QPushButton(self.m2_semiautomatico)
        self.go_semiauto.setGeometry(QtCore.QRect(130, 186, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.go_semiauto.setFont(font)
        self.go_semiauto.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.go_semiauto.setObjectName("go_semiauto")
        self.pos_x = QtWidgets.QLineEdit(self.m2_semiautomatico)
        self.pos_x.setGeometry(QtCore.QRect(130, 40, 101, 31))
        self.pos_x.setObjectName("pos_x")
        self.pos_y = QtWidgets.QLineEdit(self.m2_semiautomatico)
        self.pos_y.setGeometry(QtCore.QRect(130, 80, 101, 31))
        self.pos_y.setObjectName("pos_y")
        self.pos_z = QtWidgets.QLineEdit(self.m2_semiautomatico)
        self.pos_z.setGeometry(QtCore.QRect(130, 120, 101, 31))
        self.pos_z.setObjectName("pos_z")
        self.m1_manual = QtWidgets.QFrame(self.frame_2)
        self.m1_manual.setGeometry(QtCore.QRect(10, 40, 251, 231))
        self.m1_manual.setStyleSheet("border-color: rgb(0, 85, 255);")
        self.m1_manual.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m1_manual.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m1_manual.setObjectName("m1_manual")
        self.place = QtWidgets.QPushButton(self.m1_manual)
        self.place.setGeometry(QtCore.QRect(170, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.place.setFont(font)
        self.place.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.place.setObjectName("place")
        self.pick = QtWidgets.QPushButton(self.m1_manual)
        self.pick.setGeometry(QtCore.QRect(70, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pick.setFont(font)
        self.pick.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pick.setObjectName("pick")
        self.scroll_z = QtWidgets.QScrollBar(self.m1_manual)
        self.scroll_z.setGeometry(QtCore.QRect(10, 120, 211, 31))
        self.scroll_z.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.scroll_z.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_z.setObjectName("scroll_z")
        self.scroll_z.setRange(0, 180)
        self.label_2 = QtWidgets.QLabel(self.m1_manual)
        self.label_2.setGeometry(QtCore.QRect(0, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrolly = QtWidgets.QScrollBar(self.m1_manual)
        self.scrolly.setGeometry(QtCore.QRect(10, 80, 211, 31))
        self.scrolly.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.scrolly.setOrientation(QtCore.Qt.Horizontal)
        self.scrolly.setObjectName("scrolly")
        self.scrolly.setRange(0, 180)
        self.scroll_x = QtWidgets.QScrollBar(self.m1_manual)
        self.scroll_x.setGeometry(QtCore.QRect(10, 40, 211, 31))
        self.scroll_x.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.scroll_x.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_x.setObjectName("scroll_x")
        self.scroll_x.setRange(0, 180)
        self.label_4 = QtWidgets.QLabel(self.m1_manual)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.m1_manual)
        self.label_9.setGeometry(QtCore.QRect(140, 180, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.m3_automatico = QtWidgets.QFrame(self.frame_2)
        self.m3_automatico.setGeometry(QtCore.QRect(10, 280, 251, 101))
        self.m3_automatico.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m3_automatico.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m3_automatico.setObjectName("m3_automatico")
        self.goboton = QtWidgets.QPushButton(self.m3_automatico)
        self.goboton.setGeometry(QtCore.QRect(90, 56, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.goboton.setFont(font)
        self.goboton.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.goboton.setObjectName("goboton")
        self.label_6 = QtWidgets.QLabel(self.m3_automatico)
        self.label_6.setGeometry(QtCore.QRect(10, 15, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(30, 420, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 440, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.label_12.setFont(font)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../Taller 2 - Qt Designer/logoECCI.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 0, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.camara = QtWidgets.QGraphicsView(self.frame_2)
        self.camara.setGeometry(QtCore.QRect(270, 280, 301, 211))
        self.camara.setObjectName("camara")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(80, 390, 100, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.m3_automatico.raise_()
        self.m2_semiautomatico.raise_()
        self.m1_manual.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label.raise_()
        self.camara.raise_()
        self.label_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scroll_x.valueChanged.connect(self.manual)
        self.scrolly.valueChanged.connect(self.manual)
        self.scroll_z.valueChanged.connect(self.manual)

        self.go_semiauto.clicked.connect(self.semi_auto)

        self.plot_robot_figure()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "MODO SEMI-AUTOMATICO"))
        self.label_3.setText(_translate("MainWindow", "X:"))
        self.label_7.setText(_translate("MainWindow", "Y:"))
        self.label_8.setText(_translate("MainWindow", "Z:"))
        self.go_semiauto.setText(_translate("MainWindow", "GO"))
        self.place.setText(_translate("MainWindow", "PLACE"))
        self.pick.setText(_translate("MainWindow", "PICK"))
        self.label_2.setText(_translate("MainWindow", "GRIPER"))
        self.label_4.setText(_translate("MainWindow", "MODO MANUAL"))
        self.label_9.setText(_translate("MainWindow", "->"))
        self.goboton.setText(_translate("MainWindow", "GO"))
        self.label_6.setText(_translate("MainWindow", "MODO AUTOMATICO"))
        self.label_11.setText(_translate("MainWindow", "ELECTIVA DE ROBÓTICA"))
        self.label.setText(_translate("MainWindow", "PROTOTIPO CELDA ROBOTICA - ROBOT 3GDL"))
        self.label_10.setText(_translate("MainWindow", "ESTUDIANTES"))

    def manual(self):

        theta1 = self.scroll_x.value()
        theta2 = self.scrolly.value()
        theta3 = self.scroll_z.value()

        q1 = int(numpy.deg2rad(theta1))
        q2 = int(numpy.deg2rad(theta2))
        q3 = int(numpy.deg2rad(theta3))
        print(q1, q2, q3)

        #self.plot_robot(q1, q2, q3)

    def plot_robot(self, q1, q2, q3):

        self.Robot.plot([q1, q2, q3], backend='pyplot', limits=[-30, 30, -30, 30, -30, 30])

    def semi_auto(self):

        l1 = 4
        l2 = 8
        l3 = 18

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
        Px = int(x)
        Py = int(y)
        Pz = int(z)

        e = sqrt(Px**2+Py**2)
        c = Pz - l1
        b = sqrt(e**2+c**2)
        # Theta 1
        theta1 = float(atan2(Py,Px))
        print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
        # Theta 3
        cos_theta3 = (b**2-l2**2-l3**2)/(2*l2*l3)
        sen_theta3 = sqrt(1-(cos_theta3)**2)
        theta3 = float(atan2(sen_theta3, cos_theta3))
        print(f'theta 3 = {numpy.rad2deg(theta3):.4f}')
        # Theta 2
        alpha = math.atan2(c,e)
        phi = math.atan2(l3*sen_theta3, l2+l3*cos_theta3)
        theta2 = float(alpha - phi)
        if theta2 <= -numpy.pi:
            theta2 = (2*numpy.pi)+theta2

        print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
        #-------------
        q1 = theta1
        q2 = theta2
        q3 = theta3

        if numpy.isnan(q1) or numpy.isnan(q2) or numpy.isnan(q3):
            q1 = 0
            q2 = 0
            q3 = 0

        self.plot_robot(q1, q2, q3)


    # def open_grypper(self):

    # def close_grypper(self):

    def plot_robot_figure(self):

        l1 = 4
        l2 = 8
        l3 = 18

        R = []
        R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=0))

        self.Robot = DHRobot(R, name='Bender')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
