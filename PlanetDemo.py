import math
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


class Sun(Planet):

    def __init__(self):
        self.__name = "Sun"
        self.__gravity = 274
        self.__radius = 695700
        self.__mass = 1.9884 * math.pow(10, 30)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Mercury(Planet):

    def __init__(self):
        self.__name = "Mercury"
        self.__gravity = 3.70
        self.__radius = 2440
        self.__mass = 3.30 * math.pow(10, 23)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Venus(Planet):

    def __init__(self):
        self.__name = "Venus"
        self.__gravity = 8.87
        self.__radius = 6052
        self.__mass = 4.87 * math.pow(10, 24)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


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


class Mars(Planet):

    def __init__(self):
        self.__name = "Mars"
        self.__gravity = 3.71
        self.__radius = 3390
        self.__mass = 6.24 * math.pow(10, 23)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Jupiter(Planet):

    def __init__(self):
        self.__name = "Jupiter"
        self.__gravity = 23.1
        self.__radius = 69911
        self.__mass = 1.90 * math.pow(10, 27)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Saturn(Planet):

    def __init__(self):
        self.__name = "Saturn"
        self.__gravity = 9.0
        self.__radius = 58232
        self.__mass = 5.68 * math.pow(10, 26)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Uranus(Planet):

    def __init__(self):
        self.__name = "Uranus"
        self.__gravity = 8.7
        self.__radius = 25559
        self.__mass = 8.68 * math.pow(10, 25)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Neptune(Planet):

    def __init__(self):
        self.__name = "Neptune"
        self.__gravity = 11.0
        self.__radius = 24764
        self.__mass = 1.02 * math.pow(10, 26)
        super().__init__(self.__name, self.__gravity, self.__radius, self.__mass)


class Pluto(Planet):

    def __init__(self):
        self.__name = "Pluto"
        self.__gravity = 0.62
        self.__radius = 1188
        self.__mass = 1.30 * math.pow(10, 22)
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
