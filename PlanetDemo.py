import math
import numpy as np
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod

class Planet(ABC):

    __G = 6.67 * math.pow(10, -11)

    def __init__(self, name: str, gravity: float, radius: float, mass: float):
        self._name = name
        self._gravity = gravity
        self._radius = radius
        self._mass = mass

    ## Getters
    def getName(self) -> str:
        return self._name

    def getGravity(self) -> float:
        return self._gravity

    def getRadius(self) -> float:
        return self._radius

    def getMass(self) -> float:
        return self._mass

    @classmethod
    def getUniversalGravitationalConstant(cls) -> float:
        return cls.__G

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

    @staticmethod
    def gravitationalForce(planet_1: object, planet_2: object) -> tuple[float, float]:

        """
        This is currently a static method of the abstract class.
        To do this properly, define this as an abstract method.
        This will mean that all child classes will need to implement
        this method. With this, all planets will be able to
        experience a force on themselves. This will also include
        polymorphism and inheritance. This is much better than returning
        both forces acting on each other and then getting confused
        which acted on which. This was also, if we have a planet static,
        i.e. not moving, we can simply set its velocity to zero. Makes it
        easier to do in the subclasses itself than in the abstract class.
        """

        mass_1 = getattr(planet_1, "getMass")
        mass_2 = getattr(planet_2, "getMass")

        radius_1 = getattr(planet_1, "getRadius")
        radius_2 = getattr(planet_2, "getRadius")

        G = Planet.getUniversalGravitationalConstant()

        force_12 = (G * mass_1() * mass_2()) / radius_1()
        force_21 = (G * mass_1() * mass_2()) / radius_2()

        return force_12, force_21


class Earth(Planet):

    def __init__(self):
        self.__name = "Earth"
        self.__gravity = 9.81
        self.__radius = 6371
        self.__mass = 5.9722 * math.pow(10, 24)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Moon(Planet):

    def __init__(self):
        self.__name = "Moon"
        self.__gravity = 1.624
        self.__radius = 1737.5
        self.__mass = 7.384 * math.pow(10, 22)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


def main():

    earth = Earth()
    moon = Moon()

    Planet.gravitationalForce(earth, moon)

    print(earth.escapeVelocity())
    print(moon.escapeVelocity())

    force_earth_moon, force_moon_earth = Planet.gravitationalForce(earth, moon)

    print(f"Force of earth on the moon is: {force_moon_earth}")
    print(f"Force of the moon on earth is: {force_earth_moon}")


if __name__ == '__main__':
    main()
