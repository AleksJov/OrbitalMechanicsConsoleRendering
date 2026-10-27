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
        pass

    def getGravity(self) -> float:
        pass

    def getRadius(self) -> float:
        pass

    def getMass(self) -> float:
        pass

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

    def escapeVelocity(self):
        pass

class Earth(Planet):

    def __init__(self):
        mass = 5.9722 * math.pow(10, 24)
        super().__init__("Earth", 9.81, 6371, mass)

    def d(self):
        pass

