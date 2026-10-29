from RK4 import RK4
import ConsoleRenderDemo as CR
import math
import time
import numpy as np
import sys


def main():
    mass = 1.9884e30  # Sun, kg
    G = 6.67430e-11  # m^3 / (kg s^2)
    r_0 = 1.496e11  # 1 AU, metres
    theta_0 = 0
    v_r_0 = 0
    v_theta_0 = math.sqrt(G * mass / r_0 ** 3)  # radians per second

    state = [r_0, theta_0, v_r_0, v_theta_0]

    seconds_per_day = 24 * 60 * 60
    t, states = RK4(
        0, state,
        365 * seconds_per_day,  # one year, seconds
        seconds_per_day,  # one day per step
        mass, G
    )

    r = states[:, 0]
    theta = states[:, 1]
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    CR.ConsoleRender.animate(t, x, y, speed = 1)

if __name__ == '__main__':
    main()