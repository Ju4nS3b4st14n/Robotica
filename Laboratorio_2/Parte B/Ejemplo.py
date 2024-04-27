from roboticstoolbox import *
from spatialmath.base import *
import math
from scipy import integrate, randn
import numpy as np


h1 = 0
h2 = 0
l1 = 4
l2 = 4

q1 = 0
q2 = 0

R = []
R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

Robot = DHRobot(R, name='Bender')
#print(Robot)

Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2])
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, "deg", "zyx")}')

