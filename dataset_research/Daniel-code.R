### Processing abalone data

# Pull in abalone data
abalone.data <- read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data", 
                         header=F)

# Define column names
abalone.columns <- c("Sex","Length","Diameter","Height",
                     "Weight.Whole","Weight.Shucked",
                     "Weight.Viscera","Weight.Shell","Rings")

# Rename variables
colnames(abalone.data) <- c(abalone.columns)

# Summarize data
summary(abalone.data)

# Loop over variables and count the number of missing records
for (i in abalone.columns){
  x <-abalone.data[[i]]
  print(i)
  print(sum(is.na(x)==T))
}


### EOF ###