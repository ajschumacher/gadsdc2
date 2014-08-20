library(rpart)
library(DMwR)
test <- read.csv('test.csv')
train <- read.csv('train.csv')

lm <- lm(log(response) ~ log(h) * log(a) + poly(c,4) * poly(h,4) + b * a + b * j + b * e + b*c + e * j + c*j + a*j + log(e) * log(a) + log(j) * log(g) + log(b) * log(a) + poly(g,4) + ., data=train)
lmrefined <- step(lm)
logresp <- log(test$response)
ssr <- sum((logresp - predict(lmrefined,test))^2)