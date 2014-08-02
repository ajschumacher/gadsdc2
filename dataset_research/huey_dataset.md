#Dataset Research - Huey

[NYC Open data - School District Breakdowns](https://data.cityofnewyork.us/Education/School-District-Breakdowns/g3vh-kbnw)

I chose a basic data set that breaks down demographic statistics by school district in the NY . I actually chose this after playing around extensively with different data sets that piqued my interest. I explored a bunch listed on [this page](http://bagrow.com/dsv/datasets.html). Ultimately, the data sets that I was interested were either too big, or I didn't know how to load them in R. For the sake of getting through the basics, I chose a simple data set with a topic that is relevant to my interests. 

### Structure/Contents

__Records__: 32
__Columns__: 45
__Missing values__: It seems that the author of the data set was unable to get data for 5 schools. Instead of entering in these values as N/A, he entered them in as 0. As this would cause problems with any statistics summary, I scrubbed these 5 rows from the csv file. I'm not entirely sure if there's a better approach on how to handle this. (*will Google!!*)
__Other notes__: Values still seem incomplete - for some schools, only 2 are listed as participants, which cannot obviously be the case. 

### History

Data set was created by a user named Albert Webber on July 27, 2011 and updated on March 19, 2013. It has been downloaded 655 times as of August 2, 2014

### Other uses?

This isn't a "famous" data set so haven't been able to find any attributes for it (simple Google Search). 

### Acquiring and loading into R

1. [NYC Open data - School District Breakdowns](https://data.cityofnewyork.us/Education/School-District-Breakdowns/g3vh-kbnw)
2. Export --> Download as --> csv
3. In R: 
  * MyData = read.csv(file="School_District_Breakdowns.csv", header=TRUE)
  * Having a lot of errors with loading read.table. 

### Simple statistics 

*These statistics probably do not reflect the __true__ demographics break down of NYC school districts, as there are missing and/or inaccurate data in this data set. *

2103 = Count of all students in data set
59.6% = AVG % of females in a school 
40.4% = AVG % of males in a school 
27.6 = AVG % of black non-hispanic population in a school 
100% = AVG % of students on public assistance 
