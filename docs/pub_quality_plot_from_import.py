#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:41:27 2020

@author: sljohansen793
"""

import numpy as np
import matplotlib.pyplot as plt

#this is only needed in jupyter
"""
The goal of this script is to take data from my research and make a publication quality line plot with it. 
It is a lot more complicated than just plotting x and y values, 
but I figured out how to do all of this by just googling what I wanted to do. 
"""

plt.close("all")
#this prevents your script from plotting over an old plot each time it runs

x_list=[]
y_list=[]
#start with two empty lists, these are where we will put the data from our text file

#open your file externally first and make sure your know what is in it! 

filename="survey1775.txt"
#this file contains the amplitude and frequency values from the microwave spectrum of an unknown molecule


file=open(str(filename),"r")
#this opens the survey1775.txt file and assigns its contents to the variable "file"
#we can now manipulate this variable

junk=file.readline()
#print(junk)
#The first line of my file is not data, just words. 
#I don't want it in my lists of data so I'm just assigning it to a junk variable
#now when I use the "file" variable, it won't include this first line

for line in file:
#this loops through every line in the file
    x,y = line.split()
#this takes each line and splits it into two separate variables
#this only works if there are separated values on each line
#if the values are comma separated add "," inside the parentheses
    x_list.append(float(x))
    y_list.append(float(y))
#Now I have lists of my frequency values (x) and amplitudes (y)    

#print(x_list)
#print(y_list)

#Instead of just using plt.plot, I want to use features only available in the subplots function,
#even though I am only plotting on one set of axes. This is using matplotlib's object oriented API.

fig,ax=plt.subplots(figsize=(7.5,2.1))
#I am now making a figure for my plots that is 7.5 by 2.1 inches. 

ax.plot(x_list,y_list,color="k", linewidth=0.8)
#This command plots my x and y values, sets the line color to black,
#and sets the linewidth to smaller than the default. 

plt.title("$cis$-beta-cyanovinyl radical $1_{01}-0_{00}$", fontsize=16)
#The $$ indicate LaTeX math mode. Very useful for formatting. 
#This sets the title for the whole figure. 
#If I had more than one plot, I could use ax.set_title to title each plot on the figure. 

ax.set_xlabel("Frequency (MHz)", fontsize=14)
#My amplitude values are arbitrary units, and the y axis is usually not included in microwave spectra.
#If you want to include a y lable, use ax.set_ylabel.

ax.set_ylim(min(y_list),max(y_list))
ax.set_xlim(min(x_list),max(x_list))
#This commands set the x and y limits on my data. The min and max functions are very useful. 

ax.set_xticks(np.arange(10194.0,10201.0,1))
#This sets the x ticks to appear every 1 MHz from 10194.0 and 10200.0 MHz.
#Note that the upper limit has to be 1 above where you want the last tick- here, the last one appears at 10200.0 MHz. 

ax.set_yticks([])
#This sets the y ticks to be nothing. [] is an empty list. 

ax.get_xaxis().get_major_formatter().set_useOffset(False) 
#This weird command is SO useful and important. 
#Matplotlib's default is to make large numbers appear as an offset on the axis, and the tick labels to show +1, 0, -1
#etc from the offset number. It is usually unwanted and clunky. 
#This command makes the labels read the actual full numbers. 

for b in ["top","right","left"]:
    ax.spines[b].set_visible(False)
#This removes the frame from the specified parts of the plot. If you want a y axis to appear, delete "left"   

plt.tight_layout() 
#This is not necessary, but forces matplotlib to be more effecient about its use of space on the figure. 
#Sometimes axis labels get cut off, and this command usually fixes that. 

plt.savefig("survey1775.png", dpi=800)
#Save the figure in whatever format you want- can be .jpg, .pdf, etc. 
#Also set the resolution- I find 800 is good for publications and presentation, but a minimum of 300 is usually okay.

