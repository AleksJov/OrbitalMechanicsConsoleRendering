import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.typing import NDArray

def derivatives(t, state, central_planet: object) -> NDArray[float]:
    r, theta, v_r, v_theta = state

    radial_acc = getattr(central_planet, "centralRadialAcceleration")
    radial_acc = radial_acc(r, v_theta)

    angular_acc = getattr(central_planet, "centralAngularAcceleration")
    angular_acc = angular_acc(r, v_r, v_theta)

    return np.array([
        v_r,
        v_theta,
        radial_acc,
        angular_acc,
    ])


def RK4(t_0, state_0, T, h, central_planet):
    N = int(np.ceil((T - t_0) / h)) + 1

    t = np.zeros(N)
    states = np.zeros((N, len(state_0)))

    t[0] = t_0
    states[0] = state_0

    for i in range(N - 1):
        current_state = states[i]

        k_1 = derivatives(
            t[i], current_state, central_planet
        )
        k_2 = derivatives(
            t[i] + h / 2,
            current_state + (h / 2) * k_1,
            central_planet
        )
        k_3 = derivatives(
            t[i] + h / 2,
            current_state + (h / 2) * k_2,
            central_planet
        )
        k_4 = derivatives(
            t[i] + h,
            current_state + h * k_3,
            central_planet
        )

        states[i + 1] = current_state + (h / 6) * (
            k_1 + 2*k_2 + 2*k_3 + k_4
        )
        t[i + 1] = t[i] + h

    return t, states


def main():
    mass = 1.9884e30                  # Sun, kg
    G = 6.67430e-11                   # m^3 / (kg s^2)
    r_0 = 1.496e11                    # 1 AU, metres
    theta_0 = 0
    v_r_0 = 0
    v_theta_0 = math.sqrt(G * mass / r_0**3)  # radians per second

    state = [r_0, theta_0, v_r_0, v_theta_0]

    seconds_per_day = 24 * 60 * 60
    t, states = RK4(
        0, state,
        365 * seconds_per_day,  # one year, seconds
        seconds_per_day,        # one day per step
        mass, G
    )

    r = states[:, 0]
    theta = states[:, 1]
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Convert metres to millions of kilometres to make axis labels readable.
    scale = 1e9
    plt.plot(x / scale, y / scale, label="Orbiting planet")
    plt.scatter([0], [0], color="orange", label="Sun")

    plt.xlabel("x (million km)")
    plt.ylabel("y (million km)")
    plt.title("Planet orbiting a fixed Sun")
    plt.axis("equal")
    # plt.grid(True)
    # plt.legend()
    plt.show()


if __name__ == '__main__':
    main()