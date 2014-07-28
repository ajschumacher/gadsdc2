downloaded data from https://github.com/hadley/nycflights13/tree/master/data

library(dplyr)
library(ggplot2)
library(maps)
library(doBy)
load("/Users/lpetting/Desktop/downloads/planes.rda")
load("/Users/lpetting/Desktop/downloads/flights.rda")
load("/Users/lpetting/Desktop/downloads/weather.rda")
load("/Users/lpetting/Desktop/downloads/airports.rda")
load("/Users/lpetting/Desktop/downloads/airlines.rda")

summary(flights)
summary(weather)
## flights uses 0-24 hours, weather uses 0-23. Fix:
flights$hour[flights$hour==24]<-0 
##merge!
flights1 <- merge(flights, airlines, by=c("carrier"))
names(planes)
names(planes)[names(planes)=="year"] <- "year_built"
flights2 <-merge(flights1, planes, by=c("tailnum"))
flights3 <-merge(flights2, weather, by=c("origin", "year", "month", "day", "hour"))
flights<-flights3
names(airports)[names(airports)=="faa"] <- "dest"
flights4 <-merge(flights, airports, by=c("dest"))
flights<-flights4

##now play!
##new variable for age of plane 
flights$age <- flights$year - flights$year_built
#dummy for delays of any length
flights$delaydum= ifelse (flights$dep_delay>0,1,0)
##new variable for minutes lost per delay
flights$timelost <- flights$seats*flights$dep_delay

attach(flights)
flights$delaycat[dep_delay<16] <- "<15 mins"
flights$delaycat[dep_delay>15&dep_delay<31] <- "15-30 mins"
flights$delaycat[dep_delay>30&dep_delay<46] <- "30-45 mins"
flights$delaycat[dep_delay>45] <- ">45 mins"
detach(flights) 

##USE- when are delays more likely during day
ggplot(flights, aes(hour, fill = delaycat))+
  geom_density(position = "stack", aes(y = ..count..))+
  ylab("Number of delays")+
  xlab("Time of Day")+
  ggtitle("When do most delays occur?")

#create a delay to flight ratio
flightsby_carrier<-summaryBy(count~carrier, data=flights, FUN=c(sum))
delaysby_carrier<-summaryBy(delaydum~carrier, data=flights, FUN=c(sum))
flights<-(merge(flights, flightsby_carrier, by=c("carrier")))
flights<-merge(flights,delaysby_carrier,by=c("carrier"))

#delay-to-flight ratio, by carrier
collapse1<- summaryBy(delaydum.sum+count.sum.y~ name+carrier, FUN=c(mean), data=flights)
collapse1$ratio<-(collapse1$delaydum.sum.mean/collapse1$count.sum.y.mean)*100

#USE
#reorder for plot
collapse1 <- transform(collapse1, 
                          carrier = reorder(carrier, ratio))

ggplot(data=collapse1, aes(x=carrier, y=ratio, fill=carrier)) +
  geom_bar(colour="black", stat="identity") +
  guides(fill=FALSE)+
  xlab("Airline")+
  ylab("Ratio")+
  ggtitle("Percentage of Delayed Flights by Airline")

#USE
#delays through the year
ggplot(flights, aes(month, fill = delaycat))+
  geom_density(position = "stack", aes(y = ..count..))+ 
  geom_vline(xintercept = 1, colour="grey")+
  geom_vline(xintercept = 2, colour="grey")+
  geom_vline(xintercept = 3, colour="grey")+
  geom_vline(xintercept = 4, colour="grey")+
  geom_vline(xintercept = 5, colour="grey")+
  geom_vline(xintercept = 6, colour="grey")+
  geom_vline(xintercept = 7, colour="grey")+
  geom_vline(xintercept = 8, colour="grey")+
  geom_vline(xintercept = 9, colour="grey")+
  geom_vline(xintercept = 10, colour="grey")+
  geom_vline(xintercept = 11, colour="grey")+
  geom_vline(xintercept = 12, colour="grey")+
  xlab("Month")+
  ylab("Delays")+
  ggtitle("Distribution of Delays by Month")


#USE
#mean length of delay by time of day
ggplot(flights, aes(hour, dep_delay))+
  stat_summary(fun.y = mean, geom = "bar")+
  xlab("Time of day")+
  ylab("Length of delay, mins")+
  ggtitle("Mean delay time by hour")

#not used
#mean age by carrier
ggplot(flights, aes(carrier, age))+
  stat_summary(fun.y = mean, geom = "bar")

#to sum total flights below, need to sum something (i think)
flights$count= 1

#Make a map!
#to calculate mean delay time and total flights by airport, merge them
library(doBy)
dep<-summaryBy(dep_delay~dest, data=flights, FUN=c(mean))
flights <-merge(flights, dep, by=c("dest"))
total_flights<-summaryBy(count~dest, data=flights, FUN=c(sum))
flights <-merge(flights, total_flights, by=c("dest"))

#load US map data
all_states <- map_data("state")

#r will try to render each data point of 110000+ points, need to collapse data set
collapse2 <- summaryBy(lon+lat+dep_delay~ dest, FUN=c(mean), data=flights)
#drop HI and AK- makes map too small
collapse2<-subset(collapse2, name.y!="Honolulu Intl"&name.y!="Ted Stevens Anchorage Intl")

#finally, the map
p <- ggplot()
p <- p + geom_polygon( data=all_states, aes(x=long, y=lat, group = group),color="white" )
p <- p + geom_jitter( data=collapse2, position=position_jitter(width=0.5, height=0.5), aes(x=lon.mean, y=lat.mean, size = dep_delay.mean.x.mean), color="coral1") + scale_size(name="Minutes")
#to add label p <- p + geom_text( data=collapse2, hjust=0.5, vjust=-0.5, aes(x=lon.mean, y=lat.mean, label=name.y), color="gold2", size=1 )
p<-p+ ggtitle("Average Delay from Newark")
p

save(flights,file="flights.Rda")
