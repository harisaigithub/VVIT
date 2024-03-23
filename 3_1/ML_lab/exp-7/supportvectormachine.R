library(ISLR2)

# Load the Khan dataset
data(Khan)

# Check dataset information
names(Khan)
dim(Khan$xtrain)
dim(Khan$xtest)
length(Khan$ytrain)
length(Khan$ytest)
table(Khan$ytrain)
table(Khan$ytest)

# Create a data frame for training
dat <- data.frame(
  x = Khan$xtrain,
  y = as.factor(Khan$ytrain)
)

# Train a linear SVM model
out <- svm(y ~ ., data = dat, kernel = "linear", cost = 10)

# Display the SVM model summary
summary(out)

# Create a data frame for testing
dat.te <- data.frame(
  x = Khan$xtest,
  y = as.factor(Khan$ytest)
)

# Make predictions on the test data
pred.te <- predict(out, newdata = dat.te)

# Create a confusion matrix to evaluate the predictions
confusion_matrix <- table(pred.te, dat.te$y)
print(confusion_matrix)
accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
precision <- confusion_matrix[2, 2] / sum(confusion_matrix[, 2])
recall <- confusion_matrix[2, 2] / sum(confusion_matrix[2, ])
f1_score <- 2 * (precision * recall) / (precision + recall)

cat("Accuracy:", accuracy, "\n")
cat("Precision:", precision, "\n")
cat("Recall:", recall, "\n")
cat("F1-Score:", f1_score, "\n")