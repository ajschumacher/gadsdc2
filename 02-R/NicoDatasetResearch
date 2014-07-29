
What are the structure and contents of your dataset? (Number of records, columns, missing values, etc.)

++50 records, 3 columns, no missing values, cross-sectional. The data give the speed of cars and the distances taken to stop. 

What is the history of your dataset (How was it created?)

++The data were recorded in the 1920s on cars.

Has your dataset been written about? What have others used it for?

++Yes, here are two sources:
++Ezekiel, M. (1930) Methods of Correlation Analysis. Wiley.
++McNeil, D. R. (1977) Interactive Data Analysis. Wiley.
++The following program which generates a plot and performs a polynomial regression uses this data:

	require(stats); require(graphics)
	plot(cars, xlab = "Speed (mph)", ylab = "Stopping distance (ft)",
  	   las = 1)
	lines(lowess(cars$speed, cars$dist, f = 2/3, iter = 3), col = "red")
	title(main = "cars data")
	plot(cars, xlab = "Speed (mph)", ylab = "Stopping distance (ft)",
 	    las = 1, log = "xy")
	title(main = "cars data (logarithmic scales)")
	lines(lowess(cars$speed, cars$dist, f = 2/3, iter = 3), col = "red")
	summary(fm1 <- lm(log(dist) ~ log(speed), data = cars))
	opar <- par(mfrow = c(2, 2), oma = c(0, 0, 1.1, 0),
     	       mar = c(4.1, 4.1, 2.1, 1.1))
	plot(fm1)
	par(opar)

	## An example of polynomial regression
	plot(cars, xlab = "Speed (mph)", ylab = "Stopping distance (ft)",
	    las = 1, xlim = c(0, 25))
	d <- seq(0, 25, length.out = 200)
	for(degree in 1:4) {
	  fm <- lm(dist ~ poly(speed, degree), data = cars)
	  assign(paste("cars", degree, sep = "."), fm)
	  lines(d, predict(fm, data.frame(speed = d)), col = degree)
	}
	anova(cars.1, cars.2, cars.3, cars.4)


How do you acquire and load the dataset into R? (Include code.)

++Simply type "cars" to see the data.

What are some simple statistics describing the dataset?

++summary(cars) gives:

    	   speed           dist       
 	Min.   : 4.0   Min.   :  2.00  
 	1st Qu.:12.0   1st Qu.: 26.00  
 	Median :15.0   Median : 36.00  
	Mean   :15.4   Mean   : 42.98  
 	3rd Qu.:19.0   3rd Qu.: 56.00  
 	Max.   :25.0   Max.   :120.00  


For datasets already available in R, don't neglect to check the included documentation! (?dataset_name)
