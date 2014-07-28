#Spambase dataset#

 * **Structure.**  58 variables, 4600 observations
 * **Contents.**  Each observation corresponds to one e-mail message.  One variable captures whether the e-mail was labelled as spam by humans; the other 57 variables contain quantitative measurements of the e-mail (e.g., the relative frequency of a particular word, the frequency of a particular character, or the total number of capital letters).
 * **Missing Values.** There are no missing values in the dataset, per the handy little script below pulled from good ol' Stack Overflow.

        for (Var in names(data)) {
        missing <- sum(is.na(data[,Var]))
        print(c(Var,missing))
        } 

 * **History.** HP engineers made the dataset back in the late `90s and donated it to the UCI Machine Learning Repository.  [One webpage][1] using the dataset refers to it as "a classical dataset for spam detection," so it presumably has a storied past being used by neophyte spam analysts.

 * **Loading into R.**  After downloading spambase.data to my Desktop, changing the filename to spambase.csv because it looked like a csv file, adding in a header row with some Excel text splitting, and changing my R working directory to my Desktop, loading the data was as easy as:

        data <- read.csv('spambase.csv')

###Basic statistics###

 * 39% of the observations were classified as spam
 * E-mails classified as spam have an average of 470.7 capital letters, whereas e-mails classified as not spam have an average of only 161.5 capital letters.
 * The variance of the average length of uninterrupted sequences of captial letters is 26.15 for non-spam messages, but a whopping 2486.00 for spam messages.

[1]: http://personal.ie.cuhk.edu.hk/~zj012/projects/spam_detection.html