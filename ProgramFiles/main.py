from RK4 import RK4
import ConsoleRenderDemo as CR
import time
import numpy as np
from PlanetDemo import *

## Have a dict for the default planets and a separate one for the created planets.
## Currently, the moon is not available as it can only orbit around Earth. For this
## I would need to implement a way for the user to put Earth as the central planet.
## This is something that can be implemented later.
planet_classes = {
    "mercury": Mercury,
    "venus": Venus,
    "earth": Earth,
    # "moon": Moon,
    "mars": Mars,
    "jupiter": Jupiter,
    "saturn": Saturn,
    "uranus": Uranus,
    "neptune": Neptune,
    "pluto": Pluto
}

planets = {}

## These are all self-explanatory and can be easily followed.
## Better have them split up here instead of in the main like in my Civilisation program.
## This way, the main is kept short.
## The main for my civilisation is something like 300 lines and difficult to follow.
def createPlanet():
    while True:
        user_input = input("Choose a planet to orbit the sun (Earth, Jupiter, Neptune), "
                           "\'s\' to show registry, "
                           "or \'q\' to quit: ").strip().lower()

        if user_input.strip().lower() == "q":
            print("Exiting simulation...\n")
            time.sleep(1.5)
            exit()

        if user_input.strip().lower() == 's':
            print("Here is a list of all the planets.")
            for key in planet_classes.keys():
                print(key)
            for key in planets.keys():
                print(key)
            continue

        planet_class = planet_classes.get(user_input)
        user_planet = planets.get(user_input)
        if planet_class is not None:
            return planet_class()

        if user_planet is not None:
            return user_planet

        print(f"Planet \'{user_input}\' is not in our registry. Please try a different name or \'s\' to show registry.")


def getPositiveFloats(message: str, error_message: str) -> float:

    while True:
        try:
            value = float(input(message))

            if value <= 0:
                raise ValueError(error_message)
            return value
        except ValueError as e:
            print(f"Invalid value: {e}\n")


def getValidr_0(message: str, error_message: str) -> float:

    while True:
        try:
            value = float(input(message))

            ## The maximum screen size is 50AU. I chose this as it allows the user to create
            ## planets past Pluto, whilst still rendering Jupiter within the terminal limits.
            if value <= 0 or value > 50:
                raise ValueError(error_message)
            return value
        except ValueError as e:
            print(f"Invalid value: {e}\n")


def createUserPlanet() -> object:

    while True:
        name = input("What is your planets name: ").strip()

        if name.lower() == 'q' or name.lower() == 's':
            print("Invalid name for planet. Please try again.")
        else:
            break

    mass_message = "What is your planets mass, e.g. 4.536e24: "
    mass_error = "Mass cannot be less than or equal to zero."
    mass = getPositiveFloats(mass_message, mass_error)

    r_0_message = "What is your planets distance from the sun in AU units; max 50AU, e.g. Mars r_0 = 0.723: "
    r_0_error = "The distance from the sun cannot be less than or equal to zero or greater than 50."
    r_0 = getValidr_0(r_0_message, r_0_error)

    print("The following is information about the sidereal period.")
    print("The sidereal period is the ratio of time it takes for a planet to complete one orbit around "
          "the sun, respective to Earths one full year. For example, Venus is closer so has "
          "a sidereal period of 0.615, while Mars is further away and has a period of 1.881. "
          "Pluto is the furthest with a period of 248.1.")

    sp_message = "What is your planets sidereal: "
    sp_error = "The sidereal period must be greater than or equal to zero."
    sidereal_period = getPositiveFloats(sp_message, sp_error)

    return UserPlanet(name, mass, r_0, sidereal_period)


def planetToDict(planet: object):

    pn = getattr(planet, "getName")
    planet_name = pn()

    if planet_name.lower() in planet_classes or planet_name in planets:
        print(f"The planet \'{planet_name}\' already exists.")
    else:
        planets[planet_name.lower()] = planet
        print("Planet has been successfully created.")


def options() -> object | None:
    while True:

        user_input = input("Would you like to create a planet, use existing ones, "
                           "show planet registry, or quit [create, existing, show, q]? ").strip().lower()

        if user_input == 'q':
            print("Exiting simulation...\n")
            time.sleep(1.5)
            exit()

        if user_input.lower() == 'create':
            planet = createUserPlanet()
            planetToDict(planet)

        elif user_input.lower() == 'show':
            print("Here is a list of all the planets.")
            for key in planet_classes.keys():
                print(key)
            for key in planets.keys():
                print(key)

        elif user_input.lower() == 'existing':
            planet = createPlanet()
            return planet

        else:
            print("Invalid option. Please select from one of the following options.")


def chooseViewRadius(r_0_AU: float) -> tuple[float | int, bool]:

    if r_0_AU <= 3.2:
        return 3.5, True
    else:
        return 50, False


def markerChoice() -> str:
    while True:
        marker_input = input("Choose a marker for your planet or use the default [default] \'p\': ").strip().lower()

        if marker_input == 'default':
            return 'p'

        ## Two characters cause issues when rendering to the terminal
        ## however emojis are variable characters length. I wanted the
        ## user to be able to at least enter an emoji for the planet.
        try:
            if len(marker_input) > 2 or len(marker_input.strip()) == 0:
                raise ValueError("Marker cannot be greater than 2 characters long or be an empty string.")
            return marker_input
        except ValueError as e:
            print(f"Invalid input. {e}\n")


def main():

    while True:

        planet = options()
        marker = markerChoice()
        r_0_planet = planet.getr_0()
        planet_name = planet.getName()
        view_radius, in_belt = chooseViewRadius(r_0_planet)

        year_input_flag = input("By default, the simulation uses the planets year for the time. "
                                "Would you like to use Earth's year instead? [y/n]: ")

        earth_year_flag = False
        if year_input_flag.strip().lower() == 'y':
            earth_year_flag = True

        ## Create the sun and obtain planets initial starting values
        sun = Sun()
        planet_r_0 = planet.getr_0() * planet.getAU()
        sun_v_theta = sun.centralAngularVelocity(planet_r_0)
        theta_0 = 0
        v_r_0 = 0

        ## State vector
        state = [planet_r_0, theta_0, v_r_0, sun_v_theta]

        ## One full year in solar calendar time, i.e. one full Earth year
        SECONDS_PER_DAY = 24 * 60 * 60
        SECONDS_PER_YEAR = 365 * SECONDS_PER_DAY
        sidereal_period = planet.getSiderealPeriod()
        t, states = RK4(0, state, SECONDS_PER_YEAR * sidereal_period, SECONDS_PER_DAY * sidereal_period, sun)

        ## If they would like to use earth years as a comparison
        if earth_year_flag:
            t, states = RK4(0, state, SECONDS_PER_YEAR, SECONDS_PER_DAY, sun)

        ## This grabs the r and theta values then we can determine the x and y coords from those
        r = states[:, 0]
        theta = states[:, 1]
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        print("\nStarting simulation...")
        time.sleep(3)

        ## Running for fixed screen size
        print(f"\nThis is {planet_name.capitalize()}'s orbit with a fixed screen size.")
        time.sleep(5) ## Nicety to have to let them read before screen clears
        CR.ConsoleRender.animate(t, x, y, marker = marker) ## Simulation with fixed screen size
        time.sleep(5) ## They can observe the planets orbit for 5 sec

        ## Are we in the asteroid belt
        if in_belt:
            print(f"\n{planet_name.capitalize()} planet lies within the asteroid belt. "
                  "This is it's orbit relative to the asteroid belt.")
        else:
            print(f"\n{planet_name.capitalize()} lies outside the asteroid belt. "
              "This is it's orbit relative to pluto.")

        time.sleep(7) ## Let them be able to read the statements before clearing screen
        CR.ConsoleRender.animateVariable(t, x, y, view_radius, marker = marker) ## The simulation respective to either asteroid belt or pluto
        time.sleep(2) ## This one not so important as the screen doesn't get cleared until .animate is called

if __name__ == '__main__':
    main()