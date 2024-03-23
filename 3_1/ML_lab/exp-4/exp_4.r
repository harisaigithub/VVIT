gc <- read.csv("D:\\VVIT.BTECH\\3_1\\ML_lab\\exp-4\\german_credit.csv")
gc.bkup <- gc
head (gc)


str(gc)
gc.subset <- gc[c('Creditability','Age..years.','Sex...Marital.Status','Occupation','Account.Balance','Credit.Amount','Length.of.current.employment','Purpose')]
head(gc.subset)
normalize <- function(x) {  return ((x - min(x)) / (max(x) - min(x))) }
gc.subset.n<- as.data.frame(lapply(gc.subset[,2:8], normalize))
head(gc.subset.n)
set.seed(123) 
dat.d <- sample(1:nrow(gc.subset.n),size=nrow(gc.subset.n)*0.7,replace = FALSE)
train.gc <- gc.subset[dat.d,]
test.gc <- gc.subset[-dat.d,]
train.gc_labels <- gc.subset[dat.d,1]
test.gc_labels <- gc.subset[-dat.d,1]

library(class)
NROW(train.gc_labels) 
knn.26 <- knn(train=train.gc, test=test.gc, cl=train.gc_labels, k=26)
knn.27 <- knn(train=train.gc, test=test.gc, cl=train.gc_labels, k=27)


ACC.26 <- 100 * sum(test.gc_labels == knn.26)/NROW(test.gc_labels) 
ACC.27 <- 100 * sum(test.gc_labels == knn.27)/NROW(test.gc_labels) 
ACC.26
ACC.27
table(knn.26 ,test.gc_labels) 
table(knn.27 ,test.gc_labels) 
install.packages('caret')
library(caret)
test.gc_labels=as.factor(test.gc_labels)
confusionMatrix(knn.26 ,test.gc_labels)


confusionMatrix(knn.27 ,test.gc_labels)

i=1 
k.optm=1 
for (i in 1:28){  
  knn.mod <- knn(train=train.gc, test=test.gc, cl=train.gc_labels, k=i)  
  k.optm[i] <- 100 * sum(test.gc_labels == knn.mod)/NROW(test.gc_labels)  
  k=i  
  cat(k,'=',k.optm[i],'\n')
}


plot(k.optm, type="b", xlab="K- Value",ylab="Accuracy level")


