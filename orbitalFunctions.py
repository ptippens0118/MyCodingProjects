import math
import random
import operator
import matplotlib.pyplot as plt
import numpy as np

def runOrbitSim(centralBody, Bodies, dt, t, Tf):

    while t < Tf:

        for Body in Bodies:
            Fgx1, Fgy1 = gravForce(centralBody, Body)

            Fx1 = Fgx1
            Fy1 = Fgy1

            Body.ax.append(Fx1/Body.m)
            Body.ay.append(Fy1/Body.m)

            Body.velX.append(Body.velX[-1] + Body.ax[-1]*dt)
            Body.velY.append(Body.velY[-1] + Body.ay[-1]*dt)

            Body.posX.append(Body.posX[-1] + Body.velX[-1]*dt)
            Body.posY.append(Body.posY[-1] + Body.velY[-1]*dt)

        t = t+dt

    return Bodies

def gravForce(object1, object2):
    #Calculate force object 1 exerts on object 2
    if object1 == "Sun":
        posX1 = 0
        posY1 = 0
        mu1 = 132712*10**6
    else:
        posX1 = object1.posX[-1]
        posY1 = object1.posX[-1]
        mu1 = object1.mu

    posX2 = object2.posX[-1]
    posY2 = object2.posY[-1]

    dX = posX2 - posX1
    dY = posY2 - posY1

    r = math.sqrt(dX**2 + dY**2)

    Fg = (mu1*object2.m)/(r**2)
    theta = math.atan(dY/dX)

    if dX >= 0:
        Fgx = -abs(math.cos(theta)*Fg)
    else: 
        Fgx = abs(math.cos(theta)*Fg)

    if dY >= 0:
        Fgy = -abs(math.sin(theta)*Fg)
    else: 
        Fgy = abs(math.sin(theta)*Fg)

    return Fgx, Fgy