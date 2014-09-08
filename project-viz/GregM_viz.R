# Import Libraries --------------------------------------------------------
library(stringr)
library(plyr)
library(lubridate)
library(randomForest)
library(reshape2)
library(ggplot2)


# Set Variables -----------------------------------------------------------
setwd("C:/Users/gmorneault/Documents/Data/Lending Club")


# Immport Source ----------------------------------------------------------
loanStats3a <- read.csv(file="LoanStats3a.csv", skip=1, stringsAsFactors=FALSE)
loanStats3a$file_source <- "loanStats3a"
loanStats3b <- read.csv(file="LoanStats3b.csv", skip=1, stringsAsFactors=FALSE)
loanStats3b$file_source <- "loanStats3b"
loanStats3c <- read.csv(file="LoanStats3c.csv", skip=1, stringsAsFactors=FALSE)
loanStats3c$file_source <- "loanStats3c"

loan.stats <- rbind(loanStats3a, loanStats3b, loanStats3c)
rm(loanStats3a,loanStats3b,loanStats3c)

#headers <- read.csv(file="headers.csv", stringsAsFactors=FALSE)
#SubFields <- headers[headers$SubFields==1, 'Fields']
#loan.stats <- loan.stats[,SubFields]


# General Analysis --------------------------------------------------------
typeof(loan.stats)
attributes(loan.stats)
class(loan.stats)
names(loan.stats)
str(loan.stats)
summary(loan.stats)


# Get rid of fields that are mainly NA ------------------------------------
poor_coverage <- sapply(loan.stats, function(x) {
  coverage <- 1 - sum(is.na(x)) / length(x)
  coverage < 0.8
})

names(loan.stats[,poor_coverage==TRUE])
names(loan.stats[,poor_coverage==FALSE])
loan.stats <- loan.stats[,poor_coverage==FALSE]


# Clean Loan Status -------------------------------------------------------
ddply(loan.stats, .(loan_status), nrow)
loan.stats <- loan.stats[loan.stats$loan_status!="",]


# Create Bad Indicator (Delinquent/Default vs Payoff) ---------------------
bad_indicators <- c("Late (16-30 days)", "Late (31-120 days)", "Default", "Charged Off")
paid_indicators <- c("Fully Paid")

loan.stats$is_bad <- ifelse(loan.stats$loan_status %in% paid_indicators, 0,
                            ifelse(loan.stats$loan_status %in% bad_indicators, 1,
                                   NA))


# Clean Fields ------------------------------------------------------------
loan.stats$issue_d <- ifelse(loan.stats$file_source %in% "loanStats3a",
                                  as.Date(loan.stats$issue_d, "%m/%d/%Y"),
                                  as.Date(loan.stats$issue_d, "%Y-%m-%d"))
class(loan.stats$issue_d) <- "Date"
loan.stats$year_issued <- year(loan.stats$issue_d)
loan.stats$month_issued <- month(loan.stats$issue_d)

#loan.stats$earliest_cr_line <- as.Date(loan.stats$earliest_cr_line, "%m/%d/%y")
loan.stats$revol_util <- as.numeric(sub("%", "", loan.stats$revol_util))
loan.stats$int_rate <- as.numeric(sub("%", "", loan.stats$int_rate))

ddply(loan.stats, .(year_issued, is_bad), nrow)

table(loan.stats$loan_status, loan.stats$is_bad, useNA = "ifany")
table(loan.stats$loan_status, loan.stats$is_bad)
table(loan.stats$year_issued, loan.stats$is_bad)

# Visual #1 ---------------------------------------------------------------
default.by.vintage <- ddply(loan.stats[is.na(loan.stats$is_bad)==FALSE,], .(year_issued), function(x) {
  c("percent_bad"=sum(x$is_bad) / nrow(x),
    "n_bad"=nrow(x[x$is_bad==1,]),
    "n_paid"=nrow(x[x$is_bad==0,]),
    "n_open"=nrow(x[x$is_bad=="NA",]),
    "n_loans"=nrow(x))
})
default.by.vintage$year_as_factor = factor(default.by.vintage$year_issued)
qplot(x=year_as_factor, y=percent_bad, data=default.by.vintage)

#qplot(x=year_as_factor, y=percent_bad, data=default.by.vintage, geom="bar")

# Visual #2 ---------------------------------------------------------------
qplot(grade, int_rate, data=loan.stats, geom="boxplot", fill=grade)

# Visual #3 ---------------------------------------------------------------
qplot(loan_amnt, data=loan.stats, geom="histogram", fill=grade, binwidth=2000)
