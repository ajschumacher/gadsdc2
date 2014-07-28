data<-scan(file="euler8.txt",what="character")
numbers<-as.numeric(unlist(strsplit(data[1:20],"")))

getLgProd<-function(numbers){
tot<-length(numbers)
topProd = 0
for (i in 1:tot-13){
	prod = 1
	for (x in 0:12){
		y = i+x
		prod<-prod*numbers[y]
	}
	ifelse(prod>topProd,topProd<-prod,NA)
}
return(topProd)
}

getLgProd(numbers)