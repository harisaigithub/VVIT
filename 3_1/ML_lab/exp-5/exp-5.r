library(quantmod)
library(MASS)
library(e1071)
library(caret)
library(ggplot2)
library(pROC)

symbols <- c("AAPL","MSFT")
start_date <- "2020-01-01"
end_date <- "2023-01-01"
getSymbols(symbols, from = start_date, to = end_date)
stock_data <- merge(Ad(AAPL),Ad(MSFT))
colnames(stock_data) <- symbols
stock_returns <- diff(log(stock_data))
return_threshold <- 0.01
stock_labels <- ifelse(apply(abs(stock_returns), 1, max) > return_threshold, "High", "Low")
stock_df <- data.frame(stock_returns, stock_labels)
set.seed(123)
train_indices <- sample(1:nrow(stock_df),0.75* nrow(stock_df))
train_data <- stock_df[train_indices, ]
test_data <- stock_df[-train_indices, ]
any_na <-apply(test_data,2,function(column)
  any(is.na(column)))
print(any_na)
test_data <- test_data[complete.cases(test_data), ]
lda_model <- lda(stock_labels ~ ., data = train_data)
lda_predictions <- predict(lda_model, newdata = test_data)$class
qda_model <- qda(stock_labels ~ ., data = train_data)
qda_predictions <- predict(qda_model, newdata = test_data)$class
nb_model <- naiveBayes(stock_labels ~ ., data = train_data)
nb_predictions <- predict(nb_model, newdata = test_data)
lda_accuracy <- mean(lda_predictions == test_data$stock_labels)
qda_accuracy <- mean(qda_predictions == test_data$stock_labels)
nb_accuracy <- mean(nb_predictions == test_data$stock_labels)
cat("LDA ACCURACY:" , lda_accuracy,"\n")
cat("QDA ACCURACY:" , qda_accuracy, "\n")
cat("navive bayes accuracy:",nb_accuracy, "\n")

test_data$stock_labels=as.factor(test_data$stock_labels)
lda_cm <- confusionMatrix(lda_predictions, test_data$stock_labels)
qda_cm <- confusionMatrix(qda_predictions, test_data$stock_labels)
nb_cm <- confusionMatrix(nb_predictions, test_data$stock_labels)
print(lda_cm)
print(qda_cm)
print(nb_cm)

accuracy_df <- data.frame(Classifier = c("LDA", "QDA", "Naive Bayes"),Accuracy = c(lda_accuracy,qda_accuracy,nb_accuracy))
accuracy_plot <- ggplot(accuracy_df, aes(x= Classifier, y= Accuracy, fill = Classifier))+ geom_bar(stat = "identity", position = "dodge")+labs(y = "Accuracy", title = "Classifier Comparision")+theme_minimal()+theme(legend.position = "bottom")
print(accuracy_plot)

roc_lda <- roc(test_data$stock_labels, as.numeric(lda_predictions == "high"))
roc_qda <- roc(test_data$stock_labels, as.numeric(qda_predictions == "High"))
roc_nb <- roc(test_data$stock_labels, as.numeric(nb_predictions == "High"))
min_length <- min(length(roc_lda$sensitivities), length(roc_qda$sensitivities), length(roc_nb$sensitivities))

roc_data <- data.frame(
  FPR = c(roc_lda$specificities[1:min_length], roc_qda$specificities[1:min_length], roc_nb$specificities[1:min_length]),
  TPR = c(roc_lda$sensitivities[1:min_length], roc_qda$sensitivities[1:min_length], roc_nb$sensitivities[1:min_length]),
  Classifier = rep(c("LDA", "QDA", "Naive Bayes"), each = min_length)
)

roc_combined_plot <- ggplot(roc_data, aes(x = FPR, y = TPR, color = Classifier, linetype = Classifier)) + geom_line(linewidth = 1)+
  labs(x = "False Positive Rate (1 - Specificity)", y = "True Positive Rate (Sensitivity)", title = "ROC Curves - Classifier Comparision") +
  scale_color_manual(values = c("blue", "green", "red"))+
  scale_linetype_manual(values = c("solid", "dashed", "dotted"))+
  theme_minimal()+
  theme(legend.position = "bottom")
print(roc_combined_plot)