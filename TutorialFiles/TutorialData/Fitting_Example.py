#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:40:27 2020

@author: dangruber
"""

# Import the needed libraries.
# We'll need this for the fitting.
import scipy.optimize as so
# We'll need this for plotting it later.
import matplotlib.pyplot as plt
# We'll need this for doing some math.
import numpy as np

# This makes sure that any previous plot windows are closed.
plt.close('all')

# Declare some empty lists that will be filled with time and height data.
time_list=[]
height_list=[]

# Now we'll open the data file, which has been saved in .csv format.
with open('RocketHeights.csv','r') as rocket_obs:
    # This opens the desired file and assigns the file contents to the variable
    # "rocket_obs". The "r" indicates that we are just reading this file, "w"
    # would let us write to it.
    
    # We need to get rid of a junk line because there are headers in this data.
    junk=rocket_obs.readline()
    
    # Now we loop through the rocket_obs file and split each line, then place
    # then place the contents into the preassigned lists from above.
    for line in rocket_obs:
        # This loops through every line in the file.
        times,heights = line.split(',')
        # Remember, this only works if the values on each line are delimited
        # with commas. If the values are separated by a space, the parentheses
        # can be left empty.
        time_list.append(float(times))
        height_list.append(float(heights))
        # Remember, the numbers in the file are in '', so they are strings.
        # Numbers should be processed as floats or integers, so we have to
        # change them into that using the float() function.
        
# Check the data. Always check the data!!!
print('Times:')
print(time_list)
print('Heights:')
print(height_list)
# Plot the observations as blue dots.
plt.plot(time_list,height_list,'b.',label='Observed heights')
plt.xlabel('time (seconds)')
plt.ylabel('height (meters)')

# Define the equation to be fit. Since this is a fit equation for acceleration,
# we'll use the classic y = (1/2)*a*t^2, where the variables are t for tim,
# and a for acceleration.
def fit_eqn(t,a):
    return 0.5*a*(t**2)

# The fit function computes the optimal values for the fit parameters (popt)
# and the covariance matrix for the popt fit parameters (pcov). The covariance
# matrix is needed for calculating the standard deviation errors of the fit
# parameters.
# The actual execution of this function only takes one line, once the
# appropriate equation has been defined (as above), and the library has been
# imported (line 11). The function requires a fit equation (line 57), a list of
# x values (time_list), and a list of y values (height_list) as inputs.
popt,pcov = so.curve_fit(fit_eqn,time_list,height_list)
# Print the result.
print('Best fit acceleration (m/s^2):')
print(popt[0])

# Now let's compute the standard deviation error of the fit parameter. If there
# are more than one output fit parameters, popt, then pcov will be a matrix and
# the errors will be the square roots of the diagonal elements of pcov.
perr = np.sqrt(np.diag(pcov))
# Print the result.
print('Standard deviation of the estimate of the acceleration (m/s^2):')
print(perr[0])

# Finally, let's plot the fit over the observations. To do this we'll make an
# array of x and y values spanning the observation times.
fit_times = np.linspace(0,10,50)    # Make an array of 50 numbers from 0 to 10
fit_heights = fit_eqn(fit_times,popt) # Make an array of heights
plt.plot(fit_times,fit_heights,'r--',label='Fit curve')
# Plotted the curve as a red dashed line.
plt.title('Observed rocket heights with best fit curve')
plt.legend()