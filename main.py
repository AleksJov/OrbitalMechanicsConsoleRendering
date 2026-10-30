from RK4 import RK4
import ConsoleRenderDemo as CR
import math
import time
import numpy as np
from PlanetDemo import *

planet_classes = {
    "mercury": Mercury,
    "venus": Venus,
    "earth": Earth,
    "moon": Moon,
    "mars": Mars,
    "jupiter": Jupiter,
    "saturn": Saturn,
    "uranus": Uranus,
    "neptune": Neptune,
    "pluto": Pluto
}

def create_planet():
    while True:
        user_input = input("Choose a planet to orbit the sun (Earth, Jupiter, Neptune) or \'q\' to quit: ").strip().lower()

        if user_input.strip().lower() == "q":
            print("Exiting simulation. Have a nice day.")
            exit()

        planet_class = planet_classes.get(user_input)
        if planet_class is not None:
            return planet_class()

def createUserPlanet():
    pass

def main():

    sun = Sun()
    planet = create_planet()
    planet_r_0 = planet.getr_0() * planet.getAU()
    sun_v_theta = sun.centralAngularVelocity(planet_r_0)
    theta_0 = 0
    v_r_0 = 0

    state = [planet_r_0, theta_0, v_r_0, sun_v_theta]

    SECONDS_PER_DAY = 24 * 60 * 60
    SECONDS_PER_YEAR = 365 * SECONDS_PER_DAY
    sidereal_period = planet.getSiderealPeriod()
    t, states = RK4(0, state, SECONDS_PER_YEAR * sidereal_period, SECONDS_PER_DAY * sidereal_period, sun)

    r = states[:, 0]
    theta = states[:, 1]
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    CR.ConsoleRender.animate(t, x, y)

if __name__ == '__main__':
    main()