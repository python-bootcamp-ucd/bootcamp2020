#!/usr/bin/env 
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:17:09 2020

@author: dangruber, sljohansen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so
#we want to use a fitting function from scipy.optimize

plt.close("all")
#This helps avoid making a plot on top of an old one. By default, I put it at the top of all my scripts that include plotting.

state_list=[]
lat_list=[]
long_list=[]
temp_list = []
#we are going to put the state names, latitudes, longitudes, and temperatures in these lists

#LOOK AT THE DATA FILE BEFORE YOU START. MAKE SURE YOU KNOW WHAT'S IN THERE.

with open("StateYlyTempAndLocData.csv","r") as csv_file:
    #this opens the desired file and assigns the file contents to the variable "csv_file"
    #the "r" indicates that we are just reading this file, "w" would let us write to it
    headers=csv_file.readline()
    #We actually will use these headers again, we are trying to fit a line to the plot of the temps (y) over the years (x)

    
    for line in csv_file:
        #this loops through every line in the file
        state_data = line.split(",")
        #we could assign all the lists here, but the instead lets turn each line into its own list, so we can clean that list up in the next step.


        for i in range(len(state_data)):
            state_data[i] = state_data[i].strip()
        # This line just strips out any unwanted spaces and characters from each element of state_data.

        
        state_list.append(str(state_data[0]))
        #First column contains state names
        
        lat_list.append(float(state_data[1]))
        #second column contains latitudes
        
        long_list.append(float(state_data[2])*(-1))
        #third column contains longitudes which we have to make negative
        
        #fourth column on contains temperatures, but we need to account for Alaska's missing data
        temps = []
        for i in state_data[3:]:
            if i != '':
            #this conditional statement says "if i (the temperature value) does not equal an empty space (''), add it to the temps list    
                temps.append(float(i))
                #The numbers in the file are in '', so they are strings. Numbers should be processed as floats or integers, so we have to change them.
                #At any given time, temps contains only one state's data.
        temp_list.append(temps)
        #temp_list is the list of all temp lists for all states
        

        
#print(state_list)
#print(lat_list)
#print(long_list)
#print(temp_list)
#print out your lists to make sure they contain the correct data before continuing. 


def fit_eq(x, m, b):
    #The curve_fit function requires that x, the independent variable, be the first one declared in the function.
    return (m*x)+b
#We want to fit a trend line to each set of temperatures. This is the equation that will be called later in the curve_fit function.




years = headers.split(',')
#This takes the headers of all the columns and turns it into a list. 

for i in range(len(years)):
    years[i] = years[i].strip()
#again, this removes unwanted formatting from the list

years = years[3:]
#this pulls out just the actual years, not state, latitude, longitude

plot_year = []
# Turn all the years into floats so we can use them as numbers
for year in years:
    plot_year.append(float(year))
# This turns all the years into floats so we can use them as numbers
   
curve_list = []
#This list is where the slopes of the trendlines for each state will go. 
    
#The for loop below makes the temp and years lists the same length for each state, then uses those lists as the x and y values in the curve_fit function    
for i in temp_list:
    #this will loop through the list of temps for each state
    fit_years = plot_year[0:len(i)]
    #this makes sure the years and temps are the same length, so Alaska won't be a problem

    fit_years.reverse()
    i.reverse()
    #Reversing the lists makes the data go from the past to the present, which makes more intuitive sense for this type of climate data. 
    
    popt,pcov = so.curve_fit(fit_eq,fit_years,i)
    #This one line is doing a lot of work! 
    #This uses a non-linear least-squares fit on each state's temperature data to determine the best fit trend line for the data. 
    #popt contains the output we care about- the best fit slope and intercept for each state.
    
    curve_list.append(popt[0])
    #The slope is the first value in popt, and that's what we want to include in our plot. 
    

plt.scatter(long_list,lat_list,c=curve_list,cmap='seismic',vmin=-0.03,vmax=0.03)   
#vmin and vmax should be equidistant from zero in order to make sure the white on the colorbar indicates a zero slope.    
plt.colorbar()  
plt.title("Locations of the Centers of US States")
plt.xlabel("Longitudes")
plt.ylabel("Latitudes")
plt.savefig("Day_3_HW_Answer")
