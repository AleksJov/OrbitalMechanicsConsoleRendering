import math
import numpy as np
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod

class Planet(ABC):

    __G = 6.67e-11
    __AU = 1.496e11

    def __init__(self, name: str, gravity: float, radius: float, mass: float, r_0: float, sidereal_period: float):
        self._name = name
        self._gravity = gravity
        self._radius = radius
        self._mass = mass
        self.__r_0 = r_0
        self.__sidereal_period = sidereal_period

    ## Getters
    def getName(self) -> str:
        return self._name

    def getGravity(self) -> float:
        return self._gravity

    def getRadius(self) -> float:
        return self._radius

    def getMass(self) -> float:
        return self._mass

    def getr_0(self) -> float:
        return self.__r_0

    def getSiderealPeriod(self) -> float:
        return self.__sidereal_period

    @classmethod
    def getUniversalGravitationalConstant(cls) -> float:
        return cls.__G

    @classmethod
    def getAU(cls):
        return cls.__AU

    ## Setters
    def setName(self, name: str):
        self._name = name

    def setGravity(self, gravity: float):
        self._gravity = gravity

    def setRadius(self, radius: float):
        self._radius = radius

    def setMass(self, mass: float):
        self._mass = mass

    def escapeVelocity(self) -> float:

        G = self.getUniversalGravitationalConstant()
        mass = self.getMass()
        radius = self.getRadius()
        velocity = math.sqrt( (2 * G * mass) / radius )

        return velocity


    def centralAngularVelocity(self, r_0: float) -> float:
        """
        This is the method for the angular velocity.
        The value G is obtained from the class.
        The mass is obtained from the planet that will be in the centre.
        The value r_0 is the distance from the central planet in AU.

        :param r_0: The distance from planet x to this central planet.
        :return: Initial angular velocity
        """

        G = self.getUniversalGravitationalConstant()
        central_mass = self.getMass()

        v_theta_0 = math.sqrt(G * central_mass / (r_0 ** 3))

        return v_theta_0


    def centralRadialAcceleration(self, r: float, v_theta: float) -> float:
        """
        This defines the radial acceleration imposed by the central planet.
        Angular velocity is obtained using the centralInitialAngularVelocity method.
        The value of G is obtained from the class.
        The mass is the central mass, i.e. the planet in the centre that produces this force.
        The value r is the distance of planet x to this central planet.

        :param r: Distance from the central planet
        :param v_theta: The angular velocity of the orbiting planet
        :return radial_acc: Radial angular velocity
        """

        G = self.getUniversalGravitationalConstant()
        central_mass = self.getMass()
        angular_velocity = v_theta

        radial_acc = r * (angular_velocity ** 2) - (G * central_mass / (r ** 2))

        return radial_acc


    def centralAngularAcceleration(self, r: float, v_r: float, v_theta: float) -> float:
        """
        This defines the angular acceleration produced by the central planet.
        The value r is the distance from the central planet.
        The value v_r is the radial velocity of planet x.
        Example, an r of 1.5 means 1.5 AU = 1.5 * 1.496e11.

        :param r: The distance of planet x to the central planet
        :param v_r: The radial velocity of the orbiting planet
        :param v_theta: The angular velocity of the orbiting planet
        :return:
        """

        radial_velocity = v_r
        angular_velocity = v_theta

        angular_acc = -2 * radial_velocity * angular_velocity / r

        return angular_acc


class Sun(Planet):

    def __init__(self):
        self.__name = "Sun"
        self.__gravity = 274
        self.__radius = 695700
        self.__mass = 1.9884e30
        self.__r_0 = 0
        self.__sidereal_period = 0
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Mercury(Planet):

    def __init__(self):
        self.__name = "Mercury"
        self.__gravity = 3.70
        self.__radius = 2440
        self.__mass = 3.30e23
        self.__r_0 = 0.387
        self.__sidereal_period = 0.240846
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Venus(Planet):

    def __init__(self):
        self.__name = "Venus"
        self.__gravity = 8.87
        self.__radius = 6052
        self.__mass = 4.87e24
        self.__r_0 = 0.723
        self.__sidereal_period = 0.615
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Earth(Planet):

    def __init__(self):
        self.__name = "Earth"
        self.__gravity = 9.81
        self.__radius = 6371
        self.__mass = 5.9722e24
        self.__r_0 = 1
        self.__sidereal_period = 1
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Moon(Planet):
    """
    The moon is not a planet. Only use the moon to orbit the earth, otherwise the
    simulation will fail.
    """
    def __init__(self):
        self.__name = "Moon"
        self.__gravity = 1.624
        self.__radius = 1737.5
        self.__mass = 7.384e22
        self.__r_0 = 0.00257 ## This is the distance to the earth not the sun
        self.__sidereal_period = 0.0748
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Mars(Planet):

    def __init__(self):
        self.__name = "Mars"
        self.__gravity = 3.71
        self.__radius = 3390
        self.__mass = 6.24e23
        self.__r_0 = 1.524
        self.__sidereal_period = 1.881
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Jupiter(Planet):

    def __init__(self):
        self.__name = "Jupiter"
        self.__gravity = 23.1
        self.__radius = 69911
        self.__mass = 1.90e27
        self.__r_0 = 5.203
        self.__sidereal_period = 11.86
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Saturn(Planet):

    def __init__(self):
        self.__name = "Saturn"
        self.__gravity = 9.0
        self.__radius = 58232
        self.__mass = 5.68e26
        self.__r_0 = 9.555
        self.__sidereal_period = 29.46
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Uranus(Planet):

    def __init__(self):
        self.__name = "Uranus"
        self.__gravity = 8.7
        self.__radius = 25559
        self.__mass = 8.68e25
        self.__r_0 = 19.218
        self.__sidereal_period = 84.01
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Neptune(Planet):

    def __init__(self):
        self.__name = "Neptune"
        self.__gravity = 11.0
        self.__radius = 24764
        self.__mass = 1.02e26
        self.__r_0 = 30.110
        self.__sidereal_period = 164.8
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


class Pluto(Planet):

    def __init__(self):
        self.__name = "Pluto"
        self.__gravity = 0.62
        self.__radius = 1188
        self.__mass = 1.30e22
        self.__r_0 = 39.482
        self.__sidereal_period = 248.1
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass, self.__r_0, self.__sidereal_period)


def main():
    pass

if __name__ == '__main__':
    main()
