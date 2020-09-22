# -*- coding: utf-8 -*-

"""

Python Workshop 9/22/20

The Basics
"""

"""
Part 1
    -Variable Types: Integers, Floats, Strings
    -Print Statements
"""

a = 10
b = 10.1
c = 'ten'

#a is an integer, b is a float, c is a string
print('integer:',a)
print('float:',b)
print('string:',c)
print(a,b,c)
print('The answers are:',a,b,c)

"""You can also make an integer a float or vice versa."""

print(float(a))
print(int(b))
#note that this rounds to 10

"""
Part 2
    -Lists
"""

#let's assign a, b, and c to a list

varlist = [a,b,c]
#"list" is now a variable that contains a list of other variables. 
#Note that list= [10, 10.1, 'ten'] is functionally the same. 

print('list:',varlist)

#appending to a list let's you add more items on the end
d = 100
varlist.append(d)
print('letters with d:',varlist)

# if you only need one item in a list, you can index it

print('first thing in list=', varlist[0])
#python starts counting at 0!


"""
Part 3
    -mathematical operations
"""
e=9.5
f=6.1

eplus = e+f
print('e+f = ',eplus)

eminus = e-f
print('e-f = ',eminus)

emult = e*f
print('e*f = ',emult)

fdiv = f/2.0
print('f/2.0 =', fdiv)

esquare = e**2
print('e squared = ', esquare)

fsqrt = f**0.5
print('sqrt of f = ',fsqrt)

fmod0 = e % f
print('e modulus f = ',fmod0)

emod1 = e % 3
print('e modulus 3 = ',emod1)

fmod2 = 43 % f
print('43 modulus f = ', fmod2)

#
##these operations work on integers and floats
##combine an integer with a float and it becomes a float

list2=[e,f]
#you can multiply a list by an integer to make it repeat itself
mult=list2*4
print('multiplied list:',mult)
#

"""
Part 4
    -for loops
"""


buildlist=[]
#This list is empty, but we are going to use the append command to add values to it. 

#We could do this...
a=1**2
buildlist.append(a)

b=2**2
buildlist.append(b)

c=3**2
buildlist.append(c)

d=4**2
buildlist.append(d)

print(buildlist)

#But this takes a long time to type out, and we've only added 4 values to the list.

#We can do exactly the same thing with a for loop- it is much more efficient! 

startlist=[1,2,3,4,5,6,7,8,9]
finallist=[]
for i in startlist:
    #during the first loop, i = 1, then i = 2, until the end of startlist. 
    n = i**2
    #during the first loop, n = 1, then n = 4, then n = 9, etc. 
    print(n)
    #always start with a lot of print statements when you make a loop
    #this way, you know exactly what is happening in the loop
    finallist.append(n)
    #Add value "n" to a list
    print(finallist)
    #print the list during each loop to make sure it gets longer each time.
    
    
    
m=0
mlist=[]
#In this loop, let's add 0+1+2+3+4+5+...+20   
for j in range(1,21):
    #this will loop over values of j=1 to j=20
    m=+j
    #this is equivalent to m=m+j
    print(m)
    #this will show m increasing during each loop. 
    mlist.append(m)
    #let's also add each increasing value of m to a list, and print that too.
    print(mlist)
    


"""
Part 5
    -functions
"""
#functions allow you to use the same set of code over and over again, but with different variables. 


#we can turn a for loop from the last section into a function. 



def squarelist(list):
    #"list" is a placeholder that can be replaced by any list when the function is called
    newlist=[]
    for i in list:
        n = i**2
        newlist.append(n)
    return newlist
    #this ends the function, and means that the output is this "newlist"     

#now call the function
    
listfunc = [7,6,5,4,3,2,1]
listfunc2 = [3,4,5,6]
listfunc3 = [55,31,9]

print(squarelist(listfunc))
#this will print newlist, when listfunc is the function input.

print(squarelist(listfunc2))

print(squarelist(listfunc3))

#adding a print statement into the function will cause the output to print whenever the function is called

def squarelist2(list):
    #"list" is a placeholder that can be replaced by any list when the function is called
    newlist=[]
    for i in list:
        n = i**2
        newlist.append(n)
    print(newlist)
    return newlist

squarelist2(listfunc3)


#It is possible to use a function inside of a different function. 

#Let's take the output list of the squarelist function, and subtract each value in that list from a value in a different list.  

def subtract_lists(list1,list2):
    difference_list=[]
    squares=squarelist(list1)
    for i in range(len(list2)):
        #i will now go from 0 to the length of list2 (which should be the same as list 1)
        diffs=squares[i]-list2[i]
        difference_list.append(diffs)
    return difference_list

p=[3,4,5,6]
q=[4,3,2,1]
print(subtract_lists(p,q))



"""
Part 6
    -NumPy
"""
import numpy as np

#NumPy is a python library that has a ton of useful functions. Many are for math but the uses are broad. 
#Here are just a couple of useful NumPy functions. 

#an array can often be used like a list, but it can be multi-dimensional like a matrix

#make an array of zeros
arr1 = np.zeros((3,3))
print('zero array:',arr1)

#make an array of random numbers
#note the parentheses!
arr2 = np.random.rand(3,3)
print('random array:',arr2)

#make an array from 0 to 50 with 5 evenly spaced values
arr3 = np.linspace(0,50,5)
print('linspace:',arr3)

#make an array from 0 to 50 in intervals of 5
arr4 = np.arange(0,50,5)
print('arange:',arr4)


#arrays are great for math, you can do an operation on the whole array at once
multarr3 = arr4*10
print(multarr3)


"""
Part 7
    -simple plotting
"""
import matplotlib.pyplot as plt

x=np.arange(0,100,5)
y=np.arange(0,20,1)

#plt.plot(x,y)
#plt.title("Scatter Plot Example")
#plt.xlabel("x axis")
#plt.ylabel("y axis")
#plt.show()
#
#plt.scatter(x,y)
#plt.title("Scatter Plot Example")
#plt.xlabel("x axis")
#plt.ylabel("y axis")
#plt.savefig("Example.png")

"""
Part 8
    -import data from text or csv file
"""


x_list=[]
y_list=[]
#start with two empty lists, these are where we will put the data from our text file

#open your file externally first and make sure your know what is in it! 

#this file contains the amplitude and frequency values from the microwave spectrum of the cis-beta-cyanovinyl

with open("survey1775.txt","r") as filename:
#this file contains the amplitude and frequency values from the microwave spectrum of the cis-beta-cyanovinyl
#this opens the survey1775.txt file and assigns its contents to the variable "filename"
#the "r" means read, because we just want to read the context. "w" is write, but we don't want to change the file. 
#we can now manipulate this "file" variable

    junk=filename.readline()
    print(junk)
    #The first line of my file is not data, just words. 
    #I don't want it in my lists of data so I'm just assigning it to a junk variable
    #now when I use the "file" variable, it won't include this first line

    for line in filename:
        #this loops through every line in the file
        x,y = line.split()
        #this takes each line and splits it into two separate variables
        #this only works if there are separated values on each line
        #if the values are comma separated add "," inside the parentheses
        x_list.append(float(x))
        y_list.append(float(y))
 #Now I have lists of my frequency values (x) and amplitudes (y)    

print(x_list)
print(y_list)
