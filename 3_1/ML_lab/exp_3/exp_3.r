library(ISLR)
data("Auto")
pairs(Auto)
cor(subset(Auto, select = -name))
lm.fit1 <- lm(mpg~ -name, data = Auto)
summary (lm.fit1)

par(mfrow= c(2,2))
plot(lm.fit1)
plot(predict(lm.fit1), rstudent(lm.fit1))

lm.fit2 <- lm(mpg~ cylinders * displacement * displacement *weight, data = Auto)
summary(lm.fit2)