#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:05:06 2020

@author: sljohansen793
"""

"""
Bad Code Examples (with Answers)
    -Each example below is a snippet of code that is somehow wrong. 
    -Go through and try to fix each problem so that the code gives you the correct output. 
    -Also try to figure out the goal of each code snippet 
    -Remember that in Spyder, you can comment/uncomment with "ctr1+1"
    -Print statements are your friend! Use them to figure out what is going on in each example. 
"""
import numpy as np
import matplotlib.pyplot as plt


"""
Example 1
"""
#a = 5
#b = 5.6
#c = "the number 5" 
#
#print(float(a))
#print(str(b))
#print(int(c))

#If a string contains words, it cannot be converted into integers or floats, which are numbers only.

"""
Example 2
"""

#a_list = (1,2,3,4,5)

#b_list = (3,4,5,6,7)

#ab_list=[]

#ab_list.append(a_list[0])
#ab_list.append(b_list[1:3])
#

#print(ab_list)
#
#You can change the contents of a list. You can't change the contents of a tuple. The append function can't do anything here.

"""
Example 3
"""
#Print out the last 4 values of the list

#c_list = [7,6,5,4,3,2]
#
##Indexing, like the range function, needs the final value to be one higher than the index you want. 
#d_list = [c_list[3:7]]
#
#print(d_list)

#This one doesn't give you an error, but it's still not doing what you want it to.
#In d_list, I wanted the last four values; indices 3, 4, 5, and 6. However, I'm only getting 3 values. 
#This is because Python starts counting at zero. The index should be c_list[2:6]. 

#Indexing, like the range function, needs the final value to be one higher than the index you want. 

"""
Example 4
"""

#eq = ((3+4)/5)*(6+7)+2*9)
#
#print(eq)

#The parentheses are not closed.
#This one is easy to fix if you look at the error code, but is a common mistake when you're using complicated equations.


"""
Example 5
"""

#e = 13
#f = 14
#
#eplusf = e + f
#etothef = e**f
#
#g = eplusf*etotef 
#
#h = g//e 
#
#print(h)

"""
Example 6
"""

#array = np.arange(10,50,2)
##arange makes an array from 10 to 50 in intervals of 2
#
#array.append(52)
#
#print(array)

#this is an array, not a list. You can only append to a list. 

""" 
Example 7
"""

#i_list = [2,4,6,8,10]
#
#for i in i_list
#    j = i*2
#    j_list.append(j)
#    print(j)

#Two things are missing here. There is no colon after the first line of the for loop, and j_list=[] is missing before the loop.

"""
Example 8
"""
#The goal of this example is to make a list that looks like:
#[4,2,6,8,4,12,12,6,18]

#k_list = [4, 2, 6]
#
#
#for i in range(1,4):
#    l_list = []
#    for k in k_list:
#        l = k*i
#        l_list.append(l)
#print(l_list)

#Empty l_list is declared within the first for loop, so it gets reset to 0 each loop instead of maintaining
#all the values from before. Use print statements to see exactly what's going on here. 

"""
Example 9
"""
#This function takes one value (New) and adds another value to it (Placeholder) and then replaces New with the sum.
#This is repeated for Set_Range number of times. 

#def some_function(Placeholder, New, Set_Range):
#    for j in range(Set_Range):
#        New+= placeholder
#    print(New)
#    return New

#some_function(1,1,10)

#Capitalization matters! Placeholder and placeholder are two different variables.

"""
Example 10
"""
#make two separate plots, not two lines on the same plot

#x = np.arange(0,30,2)
#y = np.arange(0,60,4)
#
#plt.plot(x,y)
#
#
#x2 = np.arange(0,10,1)
#y2 = np.arange(0,5,0.5)
#
#plt.plot(x2,y2)

#add plt.figure() in front of each plt.plot()   
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
