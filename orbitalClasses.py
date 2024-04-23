import math
import random
import operator
import matplotlib.pyplot as plt
import numpy as np

class celestialBody: 
    def __init__(self, name, G, m, xPos, yPos, velX, velY, ax, ay):

        self.name = name
        self.G = G
        self.m = m
        self.mu = G*m
        self.posX = [xPos]
        self.posY = [yPos]
        self.velX = [velX]
        self.velY = [velY]
        self.ax = [ax]
        self.ay = [ay]

class celestialBodyElemental: 
    def __init__(self, name, a, e, ta, m):

        ta = ta*math.pi/180
        muSun = 132712*10**6
        r = a*(1-e**2)/(1+e*math.cos(ta))
        eps = -muSun/(2*a)
        vel = math.sqrt(2*(muSun/r + eps))

        self.name = name
        self.m = m
        self.G = 6.673*10**(-11)
        self.mu = self.G*m
        self.posX = [r*math.cos(ta)]
        self.posY = [r*math.sin(ta)]
        self.velX = [-vel*math.sin(ta)]
        self.velY = [vel*math.cos(ta)]
        self.ax = [0]
        self.ay = [0]

class spacecraft: 
    def __init__(self, name, a, e, ta, m, body):
        ta = ta*math.pi/180
        r = a*(1-e**2)/(1+e*math.cos(ta))
        eps = -body.mu/(2*a)
        vel = math.sqrt(2*(body.mu/r + eps))

        self.name = name
        self.m = m
        self.posX = [body.posX[-1] + r*math.cos(ta)]
        self.posY = [body.posY[-1] + r*math.sin(ta)]
        self.velX = [body.velX[-1] + vel*math.sin(ta)]
        self.velY = [body.velY[-1] + vel*math.cos(ta)]
        self.ax = [0]
        self.ay = [0]