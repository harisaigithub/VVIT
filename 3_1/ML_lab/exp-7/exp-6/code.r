# Load the required libraries
library(rpart)
library(caret)
library(pROC)
library(ROCR)
library(rpart.plot)

# Read the mushroom dataset (replace 'dataset.csv' with your actual dataset file)
dataset <- read.csv("D:\\VVIT.BTECH\\3_1\\ML_lab\\Decision tree on Mushroom data set\\mushrooms.csv")

# Convert class labels to factors
dataset$class <- as.factor(dataset$class)

# Split the dataset into training and testing sets
set.seed(123)
sample_indices <- sample(nrow(dataset), 0.8 * nrow(dataset))
train_data <- dataset[sample_indices, ]
test_data <- dataset[-sample_indices, ]

# Build a decision tree model
tree_model <- rpart(class ~ ., data = train_data, method = "class")

# Display the decision tree
rpart.plot(tree_model)

# Make predictions on the test data
predictions <- predict(tree_model, test_data, type = "class")

# Evaluate accuracy
accuracy <- sum(predictions == test_data$class) / nrow(test_data)
cat("Accuracy:", accuracy, "\n")

# Create a confusion matrix
confusion_matrix <- table(Actual = test_data$class, Predicted = predictions)
print(confusion_matrix)

# Calculate precision, recall, and F1-score
precision <- diag(confusion_matrix) / rowSums(confusion_matrix)
recall <- diag(confusion_matrix) / colSums(confusion_matrix)
f1_score <- 2 * (precision * recall) / (precision + recall)
result_df <- data.frame(Precision = precision, Recall = recall, F1_Score = f1_score)
print(result_df)

# Convert predictions to binary (1 for 'p', 0 for 'e')
binary_predictions <- ifelse(predictions == "p", 1, 0)

# Calculate ROC curve
roc_obj <- roc(test_data$class == "p", binary_predictions)

# Plot ROC curve
plot(roc_obj, print.auc = TRUE)

# Calculate AUC-ROC
auc_score <- auc(roc_obj)
cat("AUC-ROC:", auc_score, "\n")