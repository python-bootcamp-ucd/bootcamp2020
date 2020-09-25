## HW 3

This assignment will use the same csv file as HW 2. 
[StateYlyTempAndLocData.csv](http://python-bootcamp-ucd.github.io/bootcamp2020/StateYlyTempAndLocData.csv) 

Instructions:
  1. Download the csv file from the link above. 
  2. Open up a Jupyter notebook. (To use a new notebook, you can again go [here](https://jupyter.org/try), click "Try Classic Notebook", wait for page to load, then go to "File", "New Notebook", "Python 3".  You may however use the same notebook from the day 1 homework, as you will be doing similar plotting, but with some added data).
  3. In your empty notebook, go to "File", then "Open". This will take you to a new page with a directory of all files in your Binder. Select the "Upload" button in the right corner.
  4. Upload the csv file. It is now in your directory, and you can import data from it. 
  5. Here's the actual homework. Ideally, you'll have already completed HW 2 before doing this one. 

- The goal of this assignment is to fit a trend line to the temperature data for the last 100 years for each state in the US (except Hawaii, because we don't have that data).
The color of each state's dot will be determined by the slope of this trend line. The final plot will look similar to the plot for HW 2, but there you plotted the difference in average temperature from the last ten years and the first ten years of data. 
You're attempting to answer a similar question- how much has the average temperature changed in the last century? - but you're using a different method. 
- Besides importing matplot.pyplot and numpy, you also need to import scipy.optimize (as so, or as sciop, is fine)
- Like in homework 2, make a list of state names, latitudes, longitudes, and temperatures. The temperature list is actually a list of lists. 
  - The data has some extra formatting stuff in there. You can remove it by using the strip function. Try looking up how this works. 
  - Make sure to not import the empty data for Alaska. Here's an if statement that will help (don't forget to check the Day 1 if/else video!) but you'll have to use the appropriate variables from your code. "!=" means "does not equal". 
  
```
for i in state_data[3:]:
      if i != '':
          temps.append(float(i))
    temp_list.append(temps)
```
- Define this function for the slope of a line. It's important in this case that the variables are in this order. 


```
def fit_eq(x, m, b):
  return (m*x)+b
```
- Next, make lists of the y values (temperatures) and x values (years) for each state. Think of these as individual scatter plots that you want to fit a trend line to. You don't have to plot them, but it might help visualize what you're doing. 
  - You can use the years from the headers (you might have assigned this line to the junk variable at the beginning). Make sure that these lists are the same length for each state! Again, Alaska is the tricky one here. 
- In order to see how the trends are changing, you want your lists to start with the earliest years. The "reverse" function will help you do that. 
- Now comes the most important part! You want to fit each state's data using the scipy.optimize.curve_fit function. Look up the documentation for this function. 
- This function outputs two arrays. Print them both out. Which one contains the parameter that is important for the scatter plot of the US? The documentation will help you figure this out. Ask questions if you're not sure! 
- Now all that's left is to make a scatter plot, just like the one you made for homework 2. Except now, the color of each dot is determined by the line that you fit. Once you have the plot, compare it to the one for HW 2. What are the similarities and differences? 
- That's it! Congratulations, you've finished the final project of Python Bootcamp! 

## Answer
[Script](http://python-bootcamp-ucd.github.io/bootcamp2020/HW3.py)

[Plot](http://python-bootcamp-ucd.github.io/bootcamp2020/Day_3_HW_Answer.png)
