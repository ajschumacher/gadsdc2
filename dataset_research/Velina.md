# Effects of Vitamin C Levels on Tooth Growth

[The ToothGrowth Experiment](http://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html) measures the length of teeth in each of 10 guinea pigs at each of three dose levels of Vitamin C (0.5, 1, and 2 mg) with each of two delivery methods (orange juice or ascorbic acid). 

### Contents

* Columns: 3
* Rows: 60
* No missing values
* There are 20 observations at each doze level


### History

Except for the # Source (C. I. Bliss (1952) The Statistics of Bioassay. Academic Press) and # Reference (McNeil, D. R. (1977) Interactive Data Analysis. New York: Wiley) for this dataset, I wasn't able to find any other use, except in one-off mentions. 

### How I loaded the data in R and some of the code I wrote 

Downloading data from Runkeeper is fairly straightfoward. Simply follow [these instructions](http://support.runkeeper.com/hc/en-us/articles/201109886-How-to-Export-your-RunKeeper-data).

Loading the data into R was accomplished with the following steps:

* Install the package containing the ToothGrowth dataset
* Create a variable containing the dataset
* Run various statistics on the variable

```
install.packages("datasets")
my.data<-ToothGrowth
str(my.data)
names(my.data)
table(my.data$dose)
min(my.data$len)
max(my.data$len)
plot(my.data)
sum(is.na(my.data))
```

### Simple Stats

* Longest length measured: 33.9 mm
* Shortest length measured: 4.2 mm
* Mean/Median close in value, 18.81 and 19.25 respectively
* Looking at the quick plot, a higher doze of vitamin C maybe correlated to higher tooth growth
