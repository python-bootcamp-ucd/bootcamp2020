## Homework for Day 2

Here is a csv file with a list of US States, and the latitudes and longitudes of the state's centers, as well as the temperature data from the last 100+ years. 
[StateYlyTempAndLocData.csv](http://python-bootcamp-ucd.github.io/bootcamp2020/StateYlyTempAndLocData.csv) 

Instructions:
  1. Download the csv file from the link above. 
  2. Open up a Jupyter notebook. (To use a new notebook, you can again go to [here](https://jupyter.org/try), click "Try Classic Notebook", wait for page to load, then go to "File", "New Notebook", "Python 3".  You may however use the same notebook from the day 1 homework, as you will be doing similar plotting, but with some added data).
  3. In your empty notebook, go to "File", then "Open". This will take you to a new page with a directory of all files in your Binder. Select the "Upload" button in the right corner.
  4. Upload the csv file. It is now in your directory, and you can import data from it. 
  5. Here's the actual homework! 
  
  - Open the csv file and examine what's in it. What variable types are in here? Strings, floats, or integers? How is it different than the file you were working with yesterday?  Do all the rows have the same number of data?
  - In your empty Jupyter notebook, write a script that imports the data from the file.  Note that the longitudes in the file are all postive, but they should be negative, so you'll need to adjust for that.
  - Parse the data so that you have the temperature data for all of your states separated out.  You may have to make some allowances for any states that have fewer columns than others.
  - For each state, you should find the mean of the first 10 years of data, and the last 10 years of data, then find the difference between the 2.
  - Make a scatter plot of the data with x and y as the lat and lon coordinates, but color the points so that they represent the differnce in temperature from the earliest data you have to the most recent data.  Add a colorbar to your figure so to make it clear what you're plotting. It should look exactly like the plot from the previous assignment, but the dots will all be colored.
  - Your scatter plot should look vaguely like the outline of the US. Make sure Alaska is in the right place! If it's not, make sure you are plotting the correct x and y values.
  - That's it! Congratulations, you finished your second Python assignment! 


[Answer is here.](python-bootcamp-ucd.github.io/bootcamp2020/HomeworkDay2.ipynb)
