# Marc's dataset research - Car data

I chose to work with the Cars dataset, which is a simple dataset that is already included in R Studio.
The dataset contains 50 entries, measuring the relationship between automobile speed and braking distance. The dataset consists of 2 columns and no missing entries.
The dataset was originally recorded in 1920 by Dr. Mordecai Ezekiel in New York City, and I was originally drawn to the data set for three reasons:
	1. Ezekiel demonstrates strong, simple and easy to visualize correlation between the speed and stopping distance (shocking!)
	2. He only measured two variables, which allows a novice R user like myself to practice R syntax with an accessible data.frame
	3. He published this file in the crude, early days of American automotive manufacturing and his work influenced public policy. (and I would love my data science work to someday affect business or government decision making!)
	
This dataset has been written about extensively, but it is primarily used by online R tutorials and university Statisticians as a case study to help beginners get started in the Language. For this reason, I thought it was kind of a rite of passage (a la "FizzBuzz").

**Some simple statistics:**
> apply(cars, 2, sd)
    		speed      dist 
 		  5.2876 mph   25.769377 feet
> apply(cars, 2, var)
    		speed      		  dist 
		 27.95918 mph		664.06082 feet
> apply(cars, 2, mean)
			speed  			dist 
			15.40 mph		42.98 feet
			
In addition to applying discrete statistical functions to the *Cars* dataset (as done above), I ran the summary() function and printed the following statistics:
> summary(cars)
     speed           dist       
 Min.   : 4.0   Min.   :  2.00  
 1st Qu.:12.0   1st Qu.: 26.00  
 Median :15.0   Median : 36.00  
 Mean   :15.4   Mean   : 42.98  
 3rd Qu.:19.0   3rd Qu.: 56.00  
 Max.   :25.0   Max.   :120.00  


I also ran an example plot function by searching the *Cars* documentation page. It is as follows:

> plot(cars, xlab = "Speed (mph)", ylab = "Stopping distance (ft)",
+      las = 1, xlim = c(0, 25))
> d <- seq(0, 25, length.out = 200)
> for(degree in 1:4) {
+     fm <- lm(dist ~ poly(speed, degree), data = cars)
+     assign(paste("cars", degree, sep = "."), fm)
+     lines(d, predict(fm, data.frame(speed = d)), col = degree)
+ }
> anova(cars.1, cars.2, cars.3, cars.4)
Analysis of Variance Table

Model 1: dist ~ poly(speed, degree)
Model 2: dist ~ poly(speed, degree)
Model 3: dist ~ poly(speed, degree)
Model 4: dist ~ poly(speed, degree)
  Res.Df   RSS Df Sum of Sq      F Pr(>F)
1     48 11354                           
2     47 10825  1    528.81 2.3108 0.1355
3     46 10634  1    190.35 0.8318 0.3666
4     45 10298  1    336.55 1.4707 0.2316