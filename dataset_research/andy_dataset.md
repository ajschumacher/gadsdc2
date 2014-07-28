####Dataset Research Assignment from Class 2 (23 July)

I am using the 2013 DC Crime Dataset from the List of suggested datasets (DC Data Catalog: http://data.dc.gov/)

#####(1) What are the structure and contents of your dataset? (Number of records, columns, missing values, etc.)

Comma-separated values, 20 fields, 35,880 records ("observations"). 601 missing values found (using sum(is.na(dataset))).

#####(2) What is the history of your dataset (How was it created?)

Crime data statistics are a legally mandated collection requirement for the Metropolitan Police Department. MPD provides annual crime data statistics to the FBI to support the Uniform Crime Reporting (UCR) program. Data was generated from crime reporting by police, then screened as part of monthly reviews.

#####(3) Has your dataset been written about? What have others used it for?

Yes -- Officially, the MPD has released summary reports and other analysis on the dataset, and the FBI has subsumed it as part of the UCR dataset allowing for comparative analyses with other metro areas, states, etc. Unofficially, the dataset was summarized in a Washington Post article ("D.C. homicide rate is up, but violent crime continues to decrease," January 2, 2014), and various other articles compare 2014 crime rates to 12-month-prior data.  Other, more specific analysis has been performed regarding the effectiveness of certain technologies (cameras, ShotSpotter acoustic sensors) on localized crime. Urban and regional-interest blogs have also cited the dataset regarding crime comparisons within and between neighborhoods.

#####(4) How do you acquire and load the dataset into R? (Include code.)

Data was acquired as a CSV file from the DC Data Catalog (http://data.dc.gov). Loading the dataset was performed through the following command:

crime_incidents_2013_CSV <- read.csv("~/Desktop/class2/crime_incidents_2013_CSV.csv")

(I can't take credit for this, I used the menus.  But the function and the variable naming all make perfect sense.)

#####(5) What are some simple statistics describing the dataset?

* 38,880 crimes committed in 2013;
* Most common crime was "THEFT/OTHER" (12,894 incidents)
* Least common crime was "ARSON" (35 incidents)
* Ward with most crimes committed was Ward 2 (5,953 incidents)
* ANC with most crimes committed was 1A (2,121 incidents)
* Most crimes were committed during the evening shift (15,158 incidents - 42.2%)

