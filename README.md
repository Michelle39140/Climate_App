# Climate_App

**Tasks**: 
1. Explore the climate database for Honolulu, Hawaii, run climate analyze and visulaze the results;
2. Create a Flask API that returns weather data from the database up on user queries.

**Data**: [Weather data in Sqlite file](Resources/hawaii.sqlite)

**Lanugage**: Python

**Libraries**: sqlalchemy, flask, matplotlib, pandas  

**Deployed on** Heroku

**Notebook**: [Jupyter Notebook](Climate Analysis.ipynb)

## Flask API is like here:
## Climate analysis results:
### Precipitation Analysis

* Plot the results using the DataFrame `plot` method.

  ![precipitation](Images/precipitation.png)

* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

### Temperature Analysis (Optional)

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).

    ![temperature](Images/temperature.png)

### Other Recommended Analysis (Optional)

* The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.

  * Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for min, avg, and max temperatures.

  * You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic tobs that match that date string.

  * Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

  * Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

  * Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

    ![daily-normals](Images/daily-normals.png)

- - -

#
#### Copyright
Data Boot Camp ©2018. All Rights Reserved.
