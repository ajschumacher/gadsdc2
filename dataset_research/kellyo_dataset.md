###Dataset Research - Kelly O.
[Seeds Data Set from the UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/seeds)  

####What are the structure and contents of your dataset? (Number of records, columns, missing values, etc.)  
Records: 210  
Columns: 8 
Missing Values: Y  
Attribute Info:  
1. area A 
2. perimeter P
3. compactness C = 4*pi*A/P^2 
4. length of kernel 
5. width of kernel 
6. asymmetry coefficient 
7. length of kernel groove
8. classification type

####What is the history of your dataset (How was it created?)  
Collected in an experiment by the Institute of Agrophysics of the Polish Academy of Sciences in Lublin.  
Seeds are from three kinds of wheat (Kama, Rosa and Canadian).  

####Has your dataset been written about? What have others used it for?
Seems to be a classification dataset (Used in testing classifier programs). This would suggest that the three types of wheat seeds can be differentiated based on the meassurement data attributes.  

####How do you acquire and load the dataset into R? (Include code.) 
The dataset is a text file on UCI, so I saved a copy to my Documents -> `seed_data.txt`  
To read the txt file into R: `seeds<-read.table("seed_data.txt",header=FALSE)`  
I should probably also create column headings for each attribute so that I don't have to be looking them up constantly.  
````
names(seeds)<-c("Area","Perimeter","Compactness","Length", "Width","Asymmetry","GrooveLength","ClassType")
````
####What are some simple statistics describing the dataset?
See the Min, Max and Mean for each attribute quickly with: `summary(seeds)`

