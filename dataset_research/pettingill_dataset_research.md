# Exploring NYC Flight Data

### Intro 
For my dataset research I decided to take a look at the [NYC flight data](https://github.com/hadley/nycflights13/tree/ master/data) recently made available by [Hadley Wickham](https://github.com/hadley). There are 5 files available for download- flights, planes, airlines, weather, and airports. Each of these files can be merged into the flights file, to do some basic analyses on flights, delays, airlines, etc.

###File Structure 
The base file is the flights file, which has 336,776 observations and 16 variables. Each observation represents an outgoing flight in the year 2013. The planes file has 3322 observations and 4 variables. Each observation is a tail number ID. Airlines has 16 obs with 2 variables, and weather 8719 observations with 14 variables. I used the flights file as my master, and then merged the other files to this. I lost no observations in the merge of airline names into the flights file- this merely gave a proper name to the 2-digit code in the flights file. In the second merge (planes), I lost a number of observations, because R drops observations that do not merge- from both dataset. So, everytime I had a missing observation for the merge variable (tailnum), I lost an observation. This brings me to 284,170 obs. The next merge was with the weather data. The base file (flights) was for all NYC airports, but the weather data was truncated heavily in the favor of Newark (though Wickham suggested that data were available for each airport, this is not the case. I went to his git to get the code to download the raw data from the online source he provided but there was an error which I could not resolve. So I stuck with the file he made available). My final was down to 112,167, and 110,631 when I merged in the name of the arrival airport. (I wanted this for mapping later.)

The variables in my final dataset are many, ranging from weather to type of plane, engine and year of build. I do a lot of descriptive statistics and am generally familiar with R so wanted to work on plotting and mapping. I played around a bunch, mainly to see if I could find anything interesting. 

I settled on 3 plots to share, which I think capture some stories of the dataset.

1. [When do most delays occur?](https://drive.google.com/file/d/0BwxUT8SYM0VBX181dmVwSGpMblk/edit?usp=sharing) A barplot of the total number of delays
by time of day. Majorities of delays are early and for less than 15
minutes. But 2nd most prevalent delays are longer than 45 mins.

2. [Percentage of delayed flights by airline](https://drive.google.com/file/d/0BwxUT8SYM0VBUEhrTXdfWWVRME0/edit?usp=sharing). For this I summed up delayed flights (by creating a dummy for any delay and then calculating the percentage of total flights these comprised per airline. There is some variation by airline (which could be cool to explore later- does flight time to next airport matter? Age of plane? What about previous leg?

3. [Average delay from Newark](https://drive.google.com/file/d/0BwxUT8SYM0VBdnIwbDdMV3Z3N2c/edit?usp=sharing). For this I plotted airports on a map, with size scaled by the average delay to these airports. (This was pretty fun to make!)

My R code is a bit long but I have included it with this assignment. 


