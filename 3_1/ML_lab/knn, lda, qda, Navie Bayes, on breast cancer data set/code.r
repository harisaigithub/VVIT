
# Load the required libraries
library(class)
library(MASS)
library(e1071)
library(caret)

# Load the breast cancer dataset (assuming it's available in your environment)
data <- read.csv("D:\VVIT.BTECH\3_1\ML_lab\knn, lda, qda, Navie Bayes, on breast cancer data set\BreastCancer.csv")

# Split the data into training and test sets (you can adjust the ratio as needed)
set.seed(123)
sample_index <- sample(1:nrow(data), 0.7 * nrow(data))
train_data <- data[sample_index, ]
test_data <- data[-sample_index, ]

# Define the target variable (class) for training and testing
train_labels <- train_data$Class
test_labels <- test_data$Class

# Feature selection (optional)
# You can choose specific features based on domain knowledge

# K-Nearest Neighbors (KNN)
knn_model <- knn(train_data[, -1], test_data[, -1], train_labels, k = 5)
knn_confusion <- confusionMatrix(knn_model, test_labels)

# Linear Discriminant Analysis (LDA)
lda_model <- lda(train_labels ~ ., data = train_data)
lda_pred <- predict(lda_model, test_data)$class
lda_confusion <- confusionMatrix(lda_pred, test_labels)

# Quadratic Discriminant Analysis (QDA)
qda_model <- qda(train_labels ~ ., data = train_data)
qda_pred <- predict(qda_model, test_data)$class
qda_confusion <- confusionMatrix(qda_pred, test_labels)

# Naive Bayes
nb_model <- naiveBayes(train_labels ~ ., data = train_data)
nb_pred <- predict(nb_model, test_data)$class
nb_confusion <- confusionMatrix(nb_pred, test_labels)

# Print the accuracies and confusion matrices
cat("KNN Accuracy:", knn_confusion$overall["Accuracy"], "\n")
print(knn_confusion$table)

cat("LDA Accuracy:", lda_confusion$overall["Accuracy"], "\n")
print(lda_confusion$table)

cat("QDA Accuracy:", qda_confusion$overall["Accuracy"], "\n")
print(qda_confusion$table)

cat("Naive Bayes Accuracy:", nb_confusion$overall["Accuracy"], "\n")
print(nb_confusion$table)