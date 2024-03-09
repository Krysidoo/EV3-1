#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import math

# Initialiser la brique EV3, les moteurs et le capteur de toucher
ev3 = EV3Brick()
mot_gau = Motor(Port.C)
mot_dro = Motor(Port.B)
capteur_toucher = TouchSensor(Port.S1)

# Définir les caractéristiques du robot
diam = 54.9  # diamètre des roues en mm
largeur = 105  # distance entre les roues en mm
robot = DriveBase(mot_gau, mot_dro, diam, largeur)
robot.settings(500, 50, 100, 20)  # vitesse, accélération, vitesse de rotation, accélération de rotation

# Avancer vers le mur
robot.straight(2000 - 2 * math.pi * 200)  # avancer jusqu'à 20 cm avant le mur

# Tracer un cercle complet de rayon 20 cm dans le sens anti-horaire
robot.drive_time(160, -45, 11000)

# Continuer à avancer jusqu'à ce que le capteur de toucher soit actionné
while not capteur_toucher.pressed():
    robot.straight(200)

# Arrêter les moteurs
robot.stop()

# Attendre exactement cinq secondes
wait(5000)

# Reculer sur lui-même, tourner de 90 degrés dans le sens anti-horaire
robot.straight(-200)  # reculer de 20 cm
robot.drive_time(0, -50, 3500)  # tourner de 90 degrés dans le sens anti-horaire
