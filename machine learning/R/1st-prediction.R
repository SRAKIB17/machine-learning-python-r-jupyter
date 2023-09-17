train <- read.csv("machine learning/datasets/titanic/train.csv")
test <- read.csv("machine learning/datasets/titanic/test.csv")
str(train)

table(train$Survived)

prop.table(table(train$Survived))

test$Survived <- rep(0, 418)
str(test)
