oneNN <- function(data){
	
	training<-sample(1:150,50,replace=FALSE)
	test<-setdiff(1:150,training)
	training<-data[training,]
	test<-data[test,]
	
	correct = 0
	incorrect = 0
	for (i in 1:100){
		distMat = numeric()
		for (j in 1:50){
			x <- test[i,1:4]
			y <- training[j,1:4]
			distMat<-c(distMat,dist(rbind(x,y)))	
		}
		
		guess<-training[which.min(distMat),5]
		if (guess == test[i,5]) correct<-correct+1
		else incorrect<-incorrect+1
	}
	cat("Correct Predictions:",correct,"\n")
	cat("Incorrect Predictions:",incorrect,"\n")
}

