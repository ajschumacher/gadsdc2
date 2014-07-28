Infochimps UFO Dataset
=========

UFO data across more than 60,000 accounts of UFO sightings, including detailed eye-witness descriptions, location, date reported and sighted, duration and shape. The data comes from the National UFO Reporting Center.

  - 61,865 observations
  - 


Installation
--------------
1. Download .bzip file from http://www.infochimps.com/datasets/60000-documented-ufo-sightings-with-text-descriptions-and-metada
2. Unzip the .bzip file.
3. Run the following code in the directory in which the file was unzipped:

```sh
ufo <- read.table("ufo_awesome.tsv", sep="\t", fill=TRUE)
names(ufo) <- c("sighted_at","reported_at", "location", "shape", "duration", "description")
ufo2 <- cbind(ufo, substring(as.character(ufo$reported_at),1,4))
colnames(ufo2)[7] <- "year"
ufo97 <- subset(ufo2, year == 1997) # creates a subset of those UFO sightings reported in 1997
```

Mentions of Dataset online
--------------------------
Here are a smattering of the mentions of the dataset online:
* Aliens Revealed in InfoChimps' UFO Sightings Dataset : http://www.programmableweb.com/news/aliens-revealed-infochimps-ufo-sightings-dataset/2011/04/22
* Video of how to use the dataset : http://www.datameer.com/documentation/display/DAS21/UFO+Sightings
* Where the Aliens are Flying Their UFO's : http://flowingdata.com/2011/07/07/where-the-aliens-are-flying-their-ufos/
