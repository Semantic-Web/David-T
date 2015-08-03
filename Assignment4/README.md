Assignment 4:
-----------
Essentially DCAT will allow us to find all related data across multiple data.gov/ federal data sites. 
Try to find related data across databases (see data.gov)  to answer  slightly complicated questions. 
For example, you will have to use census data to find ethnic backgrounds and ages in various US regions and data from HealthData.gov on mortality and morbidity rates, 
or data on educational institutions (via data.gov) . 
Then, pose some question such as: Is health or education coverage worse in some regions and relate it to data from the US Census Bureau. 
This is just a suggestion. The idea is to use DCAT front-end to access data from two government data sets, as per your passion and background, 
and relate them using simple data analytics. A simple data analytic is to find the average for the entire US and define arbitrarily half that of that as the threshold  to define under-coverage, 
or one--and-a-half that value as the threshold to define over-coverage. 
The primary goal here is to integrate data across two data sets, using the DCAT interface. 
Any simple type of data analytics is fine. Do screen captures, and upload the code, screen captures, and a short paper to Github.

Experiment:
-----------
Comparing 2 Datasets
- 1st Dataset from Data.gov includes "Estimates of the population by age, sex, race, and Hispanic origin for the nation, states, and counties" ;
http://catalog.data.gov/dataset/population-estimates
- 2nd Dataset from HealthCare.gov includes "Mortality Rate By Region" ;
http://catalog.data.gov/dataset/infant-mortality-by-race-ethnicity-2004-2013

My goal was to combine these two datasets and compare the infant mortality rate between the different races (White, Black, American Indian, Asian, Hispanic, Pacific Islander, And Two or More Races).
one dataset showed the total deaths there were for all infants across the different races. The second dataset showed the population estimate across the united states for all ages and races. 
I provided a method to narrow the population estimate to show only the infants in the united states so I could see the total number of infants in the US for each race.
This number was essentially the "Total Number of Births" in the US for each race.

Data Analysis Performed:
-------------------------
To find the infant mortality rate for each race, I had to first find the infant population for each race across the US to use as a base denominator. 
Secondly, I had to find the number of total infant deaths for each race. The number of total deaths divided by the total number of births(infant population)
returned the mortality rate for each race.   



Results:
-----------
After Parsing the two RDF files within python and combining the 2 datasets, I have discovered that in 2013 the rates for infant mortalities for each race were as follows:

![alt tag](https://raw.githubusercontent.com/Semantic-Web/David-T/master/Assignment4/Screenshots/2013%20Rates.png)


  
![alt tag](https://raw.githubusercontent.com/Semantic-Web/David-T/master/Assignment4/Screenshots/Infant%20Mortality%20Rate%20Graph.png)
  
Conclusion:
-----------
Infants with two or more races had the highest rate of mortalities with a rate of 11.9 deaths for every 1000 births.
Black infants came in second with a rate of 10.6 deaths for every 1000 births.
Asian infants had the lowest mortality rate at 2.5 deaths for every 1000 births. 
