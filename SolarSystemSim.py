import math
import random
import operator
import matplotlib.pyplot as plt
import numpy as np
import orbitalClasses 
import orbitalFunctions

muSun = 132712*10**6
Rs2e = 149.6*10**9 #m
earthYVInit = math.sqrt(muSun/Rs2e)
G = 6.673*10**(-11)

Mercury = orbitalClasses.celestialBodyElemental("Mercury", 57.9*10**6, 0.206, 0, 0.33*10**24)
Venus = orbitalClasses.celestialBodyElemental("Venus", 108.2*10**6, 0.007, 0, 4.87*10**24)
Earth = orbitalClasses.celestialBodyElemental("Earth", 150*10**6, 0.1, 0, 5.976*10**24)
Mars = orbitalClasses.celestialBodyElemental("Mars", 228*10**6, .094, 0, 0.642*10**24)
Jupiter = orbitalClasses.celestialBodyElemental("Jupiter", 778.5*10**6, 0.049, 0, 1898*10**24)
Saturn = orbitalClasses.celestialBodyElemental("Saturn", 1432*10**6, 0.052, 0, 568*10**24)
Uranus = orbitalClasses.celestialBodyElemental("Uranus", 2867*10**6, 0.047, 0, 86.8*10**24)
Neptune = orbitalClasses.celestialBodyElemental("Neptune", 4514*10**6, 0.010, 0, 102*10**24)
Pluto = orbitalClasses.celestialBodyElemental("Pluto", 5906.4*10**6, 0.244, 0, 0.0130*10**24)

yearS = 31536000
propTime = 248*yearS
dt = .01*yearS
bodyList = [Mercury,Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]
orbitalFunctions.runOrbitSim("Sun", bodyList, dt, 0, propTime)

for body in bodyList:
    plt.plot(body.posX, body.posY)
    
plt.show()


