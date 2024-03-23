x=rnorm(100)
y=rnorm(100)
plot(x,y)
plot(x,y,xlab="this is the x-axis",ylab="this is the y-axis", main="Plot of X vs Y")
pdf("Figure.pdf") 
plot(x,y,col="green") 
dev.off()
x=seq(1,10)
x
x=1:10
x

