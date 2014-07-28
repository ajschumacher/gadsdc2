Infochimps UFO Dataset
=========
Infochimps.com is a clearinghouse for user-submitted data. They host and distribute any dataset under free/open terms. 

And among those datasets is one that contains more than 60,000 accounts of UFO sightings, including detailed eye-witness descriptions, location, dates reported and sighted, duration and shape. The data comes from the National UFO Reporting Center. The sightings span from 1995 to 2009.

61,865 observations, however, is a bit cumbersome, so I'm thinking that I may only deal with those sightings from 1997. An arbitrary year.

Installation
--------------
1. Download .bzip file from http://www.infochimps.com/datasets/60000-documented-ufo-sightings-with-text-descriptions-and-metada
2. Unzip the .bzip file.
3. Run the following code in the directory in which the file was unzipped:

```sh
ufo <- read.table("C:/infochimps/ufo/ufo_awesome.tsv", sep="\t", fill=TRUE)
names(ufo) <- c("sighted_at","reported_at", "location", "shape", "duration", "description")
ufo <- cbind(ufo, substring(as.character(ufo$reported_at),1,4))
colnames(ufo)[7] <- "year"
ufo97 <- subset(ufo, year == 1997) # creates a subset of those UFO sightings reported in 1997
states <- substr(as.character(ufo97$location), nchar(as.character(ufo97$location))-2+1, nchar(as.character(ufo97$location)))
ufo97 <- cbind(ufo97, states)
```
Statistics
---------
In 1997 there were.
  - 719 sightings
  - Most sightings occurred in the West
    - California (83)
    - Arizona (56)
    - Washington (54)
    - Missouri (44)
    - Texas (39)

And you can see this for yourself by running the following code in R:

```sh
install.packages("plyr")
library(plyr)
x <- count(ufo97$states)
x[order(x$freq, decreasing=TRUE),]
```
Mentions of Dataset online
--------------------------
Here are a smattering of the mentions of the dataset online:
* Aliens Revealed in InfoChimps' UFO Sightings Dataset : http://www.programmableweb.com/news/aliens-revealed-infochimps-ufo-sightings-dataset/2011/04/22
* Video of how to use the dataset : http://www.datameer.com/documentation/display/DAS21/UFO+Sightings
* Where the Aliens are Flying Their UFO's : http://flowingdata.com/2011/07/07/where-the-aliens-are-flying-their-ufos/
