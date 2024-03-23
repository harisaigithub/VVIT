#Implement r prog to perform principle component analysis on USArrest dataset
install.packages("ggplot2")
install.packages("gridExtra")
install.packages("caret")
library(ggplot2)
library(gridExtra)
library(caret)


data("USArrests")

scaled_data <- scale(USArrests)

pca_result <- prcomp(scaled_data, center=TRUE, scale.=TRUE)

summary(pca_result)

variance_explained <- pca_result$sdev^2 / sum(pca_result$sdev^2) * 100

cat("variance explained by each principal component")
print(variance_explained)

plot(variance_explained, type= "b" , xlab="principal component", ylab="variance Explained (%)")

variance_explained <- pca_result$sdev^2 / sum(pca_result$sdev^2)
cumulative_variance_explained <- cumsum(variance_explained)

plot(cumulative_variance_explained, type="b" , xlab= "Number of Principal Components", ylab="Cumulative variance explained", ylim=c(0,1))

abline(h=0.95 , col="red", lty=2)

num_pcs_to_reach_95_percent <- which(cumulative_variance_explained >=0.95)[1]
text(num_pcs_to_reach_95_percent,0.96,labels=paste("PCs=",num_pcs_to_reach_95_percent), col="blue")

desired_threshold <- 0.90

num_pcs_to_reach_threshold <- which(cumulative_variance_explained >= desired_threshold)[1]

top_n_pcs <- pca_result$x[, 1:num_pcs_to_reach_threshold]

cat("Number of PCs to cover at least", (desired_threshold*100), "% variance:",num_pcs_to_reach_threshold, "\n")

top_4_pcs <- pca_result$x[, 1:4]

data_with_pcs <- data.frame(top_4_pcs, mpg=USArrests$Murder)

set.seed(123)
train_index <- createDataPartition(data_with_pcs$mpg, p=0.75, list=FALSE)
train_data <- data_with_pcs[train_index,]
test_data <- data_with_pcs[-train_index,]

model <- lm(mpg~.,data=train_data)

predictions <- predict(model, newdata= test_data)

rmse <- sqrt(mean((test_data$mpg-predictions)^2))
cat("Root Mean Square Error (RMSE):", rmse, "\n")

result_data <- data.frame(Actual = test_data$mpg, Predicted= predictions)

ggplot(result_data, aes(x=Actual, y= Predicted))+
  geom_point()+
  geom_smooth(method= "lm", se=FALSE, color = "blue")+
  labs(
    x= "Actual mpg",
    y= "Predicted mpg",
    title = "Actual vs. Predicted mpg"
  )

residuals <- test_data$mpg - predictions


scree_plot <- ggplot(NULL, aes(x= 1:ncol(top_4_pcs),
                               y=cumulative_variance_explained))+
  geom_bar(stat="identity", fill = "blue")+
  labs(
    x= "Principal Component",
    y= "Cumulative Variance Explained",
    title = "Scree Plot (PCA)"
  )

residuals_plot <- ggplot(NULL, aes(x= residuals)) +
  geom_histogram(binwidth=1, fill ="green",color ="black")+
  labs(
    x="Residuals",
    y="frequency",
    title= "Residuals plot (Regression)"
  )

actual_vs_predicted_plot <- ggplot(result_data, aes(x=Actual,y=Predicted))+
  geom_point()+
  geom_smooth(method= "lm", se=FALSE, color = "blue")+
  labs(
    x= "Actual mpg",
    y= "Predicted mpg",
    title="Actual vs. Predicted mpg"
  )

summary_plot <- grid.arrange(scree_plot, residuals_plot , actual_vs_predicted_plot, ncol=2)

print(summary_plot)