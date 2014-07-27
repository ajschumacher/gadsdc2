# Analyizing Runkeeper Data 

[Runkeeper](http://www.runkeeper.com/) is a personal fitness tracking service. Using a smartphone app, a user is able to record position, speed, route data and more.

### Structure and Contents

* Dates range: 2013-06-01 to 2014-07-26
* Number of records: 591
* Columns: 12
** Observations include type of activity, such as cycling or running, average speed, distance and more.
* Discreptancies: 
** At least one column, route name, has almost all NA values.
** Some values appear inaccurate, such as an activity duration being listed as -43 minutes

### History

This data represents just over a year of personal tracking of my own activities, mainly cycling. As a bike communter living in DC, a typical week will include trips to and from work, as well as longer weekend rides.

We can assume no one as written about my data, as it's private and only accesible via my Runkeeper account.

### Acquision

Downloading data from Runkeeper is fairly straightfoward. Simply follow [these instructions](http://support.runkeeper.com/hc/en-us/articles/201109886-How-to-Export-your-RunKeeper-data).

Loading the data into R was accomplished with the following steps:

* Ensure R is working in the same directory as our data
* Load the data into a variable
* Validate data was imported correctly

```
getwd()
my.data <- read.csv('runkeeper-data/cardioActivities.csv')
names(my.data)
str(my.data)
head(my.data, n=10)
```

### Simple Stats

* Furthest distance traversed: 22.41 miles
* Fastest average speed: 21.7 mph
* Slowest average speed: -0.67 _suspicious!_
* Just under 60% of activites were bike rides
* Exactly one activiy was recorded as snowboarding
