# Step 1: Create a vector x with the values 1, 3, 2, and 5.
x <- c(1, 3, 2, 5) 
x

# Step 2: Reassign x with a new vector containing the values 1, 6, and 2.
x <- c(1, 6, 2) 
x

# Step 3: Create a new vector y with the values 1, 4, and 3.
y <- c(1, 4, 3)

# Step 4: Get the length of the vector x.
length(x)

# Step 5: Get the length of the vector y.
length(y)

# Step 6: Perform element-wise addition of vectors x and y.
x + y

# Step 7: List all the objects in the current R environment.
ls()

# Step 8: Remove the objects x and y from the R environment.
rm(x, y)

# Step 9: List all the objects in the current R environment.
ls()

# Step 10: An alternative way to remove all objects from the R environment.
rm(list = ls())

# Step 11: Open the help documentation for the matrix function in R.
?matrix

# Step 12: Create a 2x2 matrix x with the data provided (1, 2, 3, and 4).
x <- matrix(data = c(1, 2, 3, 4), nrow = 2, ncol = 2) 
x
