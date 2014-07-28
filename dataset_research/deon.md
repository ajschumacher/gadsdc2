#Markdown Live Editor#
# Interesting Dataset

[NYC Jobs][1]

##Description
This dataset contains current job postings available on the City of New York’s official jobs site ([http://www.nyc.gov/html/careers/html/search/search.shtml][2]). Internal postings available to city employees and external postings available to the general public are included. This data is updated weekly.

##Prior usage or write-ups
I cannot find any evidence of anyone else doing analysis on this dataset or writing about it.

##Data acquisition
I exported this file in CSV format from the [NYC Open Data][1] website to my laptop ...

 - Export
 - Download as ... CSV

... and then loaded it using the following code:

    nyc.data<-read.csv('/Users/richardgriessel/Downloads/NYC_Jobs.csv')

The R function read.csv reads a file in table format and creates a data frame from it, with cases corresponding to lines and variables to fields in the file.

##Basic Stats
Records: 1807
Columns: 26

    > summary(nyc.data$X..Of.Positions)
       Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      1.000   1.000   1.000   4.564   1.000 999.000 
    
----------

    > summary(nyc.data$Salary.Range.From)
       Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
          0   43350   54080   51060   61850  205200
    
----------

    > summary(nyc.data$Salary.Range.To)
       Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
          9   53790   79900   80110  100000  212600 

##Column names:
Job ID,Agency,Posting Type,# Of Positions,Business Title,Civil Service Title,Title Code No,Level,Salary Range From,Salary Range To,Salary Frequency,Work Location,Division/Work Unit,Job Description,Minimum Qual Requirements,Preferred Skills,Additional Information,To Apply,Hours/Shift,Work Location 1,Recruitment Contact,Residency Requirement,Posting Date,Post Until,Posting Updated,Process Date


  [1]: https://data.cityofnewyork.us/Business/NYC-Jobs/kpav-sd4t
  [2]: http://www.nyc.gov/html/careers/html/search/search.shtml

