#Daniel's dataset research-Abalone data


I have chosen the abalone data to use for my dataset research project. The source of my dataset comes from UC Irvine's Machine Learning Repository [website](http://archive.ics.uci.edu/ml/datasets/Abalone?pagewanted=all).
The dataset and documentation can be found in the following links:
* [Data](http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data)
* [Documentation](http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.names)


##### 1. What are the structure and contents of your dataset? (Number of records, columns, missing values, etc.)

The Abalone data contains various measurements collected on a sample of 4,177 abalone. From the documentation, we see that there are nine variables. The names of the variables along with other relevant information are summarized below:

|Variable name|Data type|Units|Description|
|:------------|:--------|:----|:----------|
|Sex|nominal|n/a|M, F, and I (infant)|
|Length|continuous|mm|Longest shell measurement|
|Diameter|continuous|mm|Widest shell measurement|
|Height|continuous|mm|Thickness with meat in shell|
|Whole weight|continuous|g|Weight of whole abalone|
|Shucked weight|continuous|g|Weight of meat|
|Viscera weight|continuous|g|Weight of gut (after bleeding)|
|Shell weight|continuous|g|Weight of shell after being dried|
|Rings|integer|n/a|Rings +1.5 gives the age in years|  

Note that the continuous variables (i.e., all but sex and rings) have been scaled by dividing them by 200.

##### 2. What is the history of your dataset (How was it created?)

According to the documentation, the database was first owned by *the Department of Primary Industry and Fisheries, Tasmania*. In particular, *the Marine Resources Division* of *the Marine Reserach Laboratories - Taroona*. And it was donated to UC Irvine's Machine Learning Repository by Sam Waugh who was associated with *the Department of Computer Science* at *the University of Tasmania* in December 1995.

It appears that the data was originally created for the following study:
* Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994) "The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H._ _rubra_) from the North Coast and Islands of Bass Strait", Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288).


##### 3. Has your dataset been written about? What have others used it for?

Referring again to the documentation, at least a couple of academic papers have been written using this dataset:
* Sam Waugh (1995) "Extending and benchmarking Cascade-Correlation", PhD thesis, Computer Science Department, University of Tasmania.
* David Clark, Zoltan Schreter, Anthony Adams "A Quantitative Comparison of Dystal and Backpropagation", submitted to the Australian Conference on Neural Networks (ACNN '96).

Furthermore, the dataset has been used by many different individuals and organizations for exploring data science/data analysis concepts. The *Statistical Consulting Group* at the *San Diego State University* has written a [post](http://scg.sdsu.edu/linear-regression-in-r-abalone-dataset/) on performing linear regressions in R using this dataset.


##### 4. How do you acquire and load the dataset into R? (Include code.)

Although the code for loading the dataset and performing simple statistics can be found in the file `Daniel-code.R`, here is the code snippet that I used to load the dataset into R:

```R
# Pull in abalone data
abalone.data <- read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data", header=F)
```

Because the column names are not provided in the raw source data, I decided to create a vector of the column names. I used the vector to name the columns:

```R
# Define column names
abalone.columns <- c("Sex","Length","Diameter","Height",
                     "Weight.Whole","Weight.Shucked",
                     "Weight.Viscera","Weight.Shell","Rings")

# Rename variables
colnames(abalone.data) <- c(abalone.columns)
```


##### 5. What are some simple statistics describing the dataset?

The results of running the `summary()` function are summarized below. As noted above, the continuous variables (i.e., all but sex and rings) have been scaled by dividing them by 200.

* Categorical variables:

|Sex|Count|
|:---|---:|
|Female|1,307|
|Infant|1,342|
|Male|1,528|
|Total|4177|

* Numerical variables:

|Column|Minimum|Maxium|Mean|Median|
|:-----|------:|-----:|---:|-----:|
|Length|0.075|0.815|0.524|0.545|
|Diameter|0.0550|0.6500|0.4079|0.425|
|Height|0.0000|1.1300|0.1395|0.1400|
|Weight.Whole|0.0020|2.8255|0.8287|0.7995|
|Weight.Shucked|0.0010|1.4880|0.3594|0.3360|
|Weight.Viscera|0.0005|0.7600|0.1806|0.1710|
|Weight.Shell|0.0015|1.0050|0.2388|0.2340|
|Rings|1.000|29.000|9.934|9.000|


