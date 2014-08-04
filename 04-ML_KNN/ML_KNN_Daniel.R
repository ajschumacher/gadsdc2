# Daniel Chung

# Implement a one-nearest-neighbor algorithm 
# as a function in R that takes three arguments:
#     1. A data frame of numeric columns, the training data.
#     2. A vector of labels for the training data.
#     3. A data frame with the same columns as the first data frames, 
#         this one the data to predict for.

# Next steps:
#   Implement KNN algorithm, where K > 1
#   by updating the f.nn_label function to identify the correct label

############
# KNN Code #
############

### 1. Define a function as described to implement 1NN
    f.find_KNN <- function(training_data, labels, test_data) {
      
      # Apply the f.nn_label function for each row in test_data
      knn_labels <- apply(test_data, 1, f.nn_label, training_data, labels)
      final <- test_data
      final$knn_label <- knn_labels
      return(final)
    }


### 2. Define helper functions
    f.nn_label <- function(test_data_row, training_data, labels) {  
      # For each test_data_row value, find all labels and Euclidean
      # distances between it and the training_data
      euc_dist <- apply(training_data, 1, f.euc_dist, test_data_row)
      knn_dist <- labels
      knn_dist$dist <- euc_dist
      # Return the label associated with the minimun value of 
      # the Euclidean distance to get the 1NN
      return(knn_dist[which.min(knn_dist$dist), 1])
    }
    
    f.euc_dist <- function(training_data_row, test_data_row) {
      return( sqrt(sum((training_data_row-test_data_row)^2)) )
    }


### 3. Run the main KNN function
    
    # Create datasets to test my code (optional)
    training.data <- iris[seq(1, 150, 25),][1:2]
    label.data <- iris[seq(1, 150, 25),][5]
    test.data <- iris[seq(5, 120, 21),][1:2]
    
    # Run the function using above dataset
    KNN.results <- f.find_KNN(training.data, label.data, test.data)


### EOF ###