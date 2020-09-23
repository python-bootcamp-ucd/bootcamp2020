#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:57:06 2020

@author: sljohansen793
"""

import matplotlib.pyplot as plt
plt.close("all")
#this prevents python from plotting over an old plot, but isn't necessary in Jupyter

state_list=[]
lat_list=[]
long_list=[]
#we are going to put the state names and latitudes and longitudes in these lists

#LOOK AT THE DATA FILE BEFORE YOU START. MAKE SURE YOU KNOW WHAT'S IN THERE.

with open("StateAndLocDataDay1.csv","r") as csv_file:
    #this opens the desired file and assigns the file contents to the variable "csv_file"
    #the "r" indicates that we are just reading this file, "w" would let us write to it

    junk=csv_file.readline()
    #The first line of the file includes the headers, not the data. We're assigning that to the variable "junk"
    #It won't be used again
    print(junk) #this makes sure that the right line is junk

    for line in csv_file:
        #this loops through every line in the file
        states,lats,longs = line.split(",")
        #this takes each line and splits it into three separate variables
        #this only works if there are separated values on each line
        #if the values are separated by a space, the parentheses can be empty
        state_list.append(states)
        lat_list.append(float(lats))
        long_list.append(float(longs)*(-1))
        #The numbers in the file are in '', so they are strings. Numbers should be processed as floats or integers, so we have to change them. 
        #You can also make these lists by being clever about indexing instead of using line.split(). Day 2 will cover this.

print(state_list)
print(lat_list)
print(long_list)
#print out your lists to make sure they contain the correct data before continuing. 

plt.scatter(long_list,lat_list)        
plt.title("Locations of the Centers of US States")
plt.xlabel("Longitudes")
plt.ylabel("Latitudes")
plt.savefig("Day_1_HW_Answer.png")
#Does this look like the US? If it doesn't, it's because the signs are wrong somewhere, or the x and y are inverted. 
