# Newtonian Mechanics Console Render

## About
This project is a simulation of the orbits of planets
in the solar system. The simulation uses Newtonian Gravity
and polar coordinates to determine the equations of 
motion of each planet. The program then renders the orbit
to the console, plotting the sun and the orbiting planet.
For the physicists, the orbits are not Keplerian. Programming
this would be excessive for an Introduction to Programming course.
As a result, the orbits are circular.

## How to run
The simulation is run via _main.py_. The user **MUST** run it in
the local terminal and not in an IDE terminal as IDE
terminals cause issues with the render. The user is asked
whether they would like to create a planet or use an existing
one. Upon then, they are able to specify details or simply
begin the simulation. It does not matter whether the user
is in fullscreen or windowed mode as the program will render
based on the size of the terminal. One thing to avoid is switching
between fullscreen and windowed during the simulation as this 
causes line wrapping. After each render, there is some time
provided for the user to observe the orbit, before the next
render takes place. There is an option for using either 
Earth's time or the chosen planet's time. Experiment with
it and observe the changes.

## Required files
Since this is run on the local terminal and not in an IDE,
the user **MUST** have _python3_ installed. Not only this,
but the user must also have the following two installed:

- Numpy
- Matplotlib

as the program uses both.

## Main
This is the main file. Here is where the simulation occurs.
The user is asked whether they would like to create a planet
or use an existing one, then the program renders to the console.
The first render is the planets own orbit on a fixed screen size.
The second render is the planets orbit relative to either the
asteroid belt or 50AU (slightly further than Pluto). This way 
the user is able to see the original and a comparison to 
something of relative size.

# DISCLAIMER
Since the simulation compares to either the asteroid belt or Pluto,
the speed at which some planets orbit may look funky. This is noticeable
when choosing something like Jupiter and having the second render occur.
It shows Jupiter orbiting very slowly compared to Pluto's second render.
This is physically not accurate however is a limitation due to terminal 
window sizes. This becomes more apparent when the user selects Earth's time.

## PlanetDemo
The program has an abstract _Planet_ class from which the 
planets, the sun, and the moon, are created from. These child
classes inherit the methods from the parent class. All these
planets have the following values (even if they are not used):

- Name
- Gravity
- Radius
- Mass
- Distance from the sun (r_0)
- Sidereal period (see https://en.wikipedia.org/wiki/Sidereal_time
for more info)

## RungeKuttaDemo
This is the Runge Kutta algorithm for any butcher tableau.
This algorithm was written in 2020, so the file 
might look messy. With this, the user is able to use any 
butcher tableau and Runge Kutta method for approximations.
One need only modify the code to accept vectors and objects.

## RK4
This is the Runge Kutta 4 method derived from RungeKuttaDemo.
This was the original algorithm I wrote before making a more 
generic Runge Kutta algorithm. I modified this to accept a vector
and an object for the calculation.

## ConsoleRenderDemo
This is where the magic happens. This is the console render 
script written by ChatGPT and modified by me. If I had the time, I would
have written it from scratch myself. The console render renders in the terminal
regardless of window size. It determines the maximum size of the 
window and if the user is fullscreen or not. It then creates a 
grid to which it draws the sun, the planet, and a marker for
the orbit.

## Statement about AI usage
All the files were written by me except for _ConsoleRenderDemo.py_;
this one was originally written by ChatGPT then modified by me
to suit my needs. This is because I lacked the time to learn how to do this.
This is a huge project that took place over the semester,
yet I _wisely_ decided to start it one week out from the due date.