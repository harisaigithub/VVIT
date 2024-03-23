#!/usr/bin/env python
# coding: utf-8

# # Multi-layer Perceptron
# 
# <ol>
#     <li> Components: Input layer, Hidden layer(s) and Output layer. </li>
#     <li> Fully connected </li>
# </ol>
# 

# ### Steps:
# 
# For every epoch,
# 
# <ol>
#     <li> Training data is propagated to the MLP through input layers. It passes through the hidden layers, if any forwarding outputs of activation functions to the next layer. Finally the output is generated at the output layer by applying activation functions. </li>
#     <li> The predicted output will be compared with actual output and hence error will be calculated. </li>
#     <li> If error>0, apply backpropagation methodology to modify weights starting from output layer moving towards input layer. </li>
#     <li> Check accuracy score. If satisfied, stop. Else, go to step 1. </li>
# </ol>
# 

# ## Bank Notes dataset
# 
# Download from https://www.kaggle.com/aariyan101/bank-notes 
# 
# ### Attributes
# 
# 1. Variance of image 
# 2. Skewness of image 
# 3. Curtosis of image 
# 4. Entropy 
# 5. Class  

# ### Import dataset

# In[1]:


import pandas as pd
import numpy as np

bnotes = pd.read_csv("C:\\Users\\kgnan\\Downloads\\bank_note_data.csv")
print(bnotes.head())
print(bnotes['class'].unique())


# In[ ]:





# In[2]:


bnotes.shape


# In[3]:


bnotes.describe(include = 'all')


# In[4]:


X = bnotes.drop('class', axis=1)
y = bnotes['class']
print(X.head(2))
print(y.head(2))


# ### Splitting to training and testing
# 

# In[5]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
print(X_train.shape)
print(y_test.shape)


# Normalized input X train

# ## Train the model
# 
# Import the MLP classifier model from sklearn

# In[7]:


from sklearn.neural_network import MLPClassifier


# In[16]:


mlp = MLPClassifier(max_iter=500, activation='relu')
mlp


# ### About parameters 
# 
# 1. hidden_layer_sizes : tuple, length = n_layers - 2, default (100,)
# 
# The ith element represents the number of neurons in the ith hidden layer.
# 
# 2. activation : {‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default ‘relu’
# 
# Activation function for the hidden layer.
# 
# ‘identity’, no-op activation, useful to implement linear bottleneck, returns f(x) = x
# ‘logistic’, the logistic sigmoid function, returns f(x) = 1 / (1 + exp(-x)).
# ‘tanh’, the hyperbolic tan function, returns f(x) = tanh(x).
# ‘relu’, the rectified linear unit function, returns f(x) = max(0, x)
# 
# 3. learning_rate : {‘constant’, ‘invscaling’, ‘adaptive’}, default ‘constant’
# 
# 4. learning_rate_init : double, optional, default 0.001
# 
# 5. max_iter : int, optional, default 200
# 
# Maximum number of iterations. The solver iterates until convergence (determined by ‘tol’) or this number of iterations. For stochastic solvers (‘sgd’, ‘adam’), note that this determines the number of epochs (how many times each data point will be used), not the number of gradient steps.
# 
# 6. shuffle : bool, optional, default True
# 
# Whether to shuffle samples in each iteration. Only used when solver=’sgd’ or ‘adam’.
# 
# 7. momentum : float, default 0.9
# 
# Momentum for gradient descent update. Should be between 0 and 1. Only used when solver=’sgd’.
# 
# 8. early_stopping : bool, default False
# 
# Whether to use early stopping to terminate training when validation score is not improving. If set to true, it will automatically keep 10% of training data as validation and terminate training when validation score is not improving by at least tol for two consecutive epochs. Only effective when solver=’sgd’ or ‘adam’
# 

# ### Training

# In[17]:


mlp.fit(X_train,y_train)


# ### Testing

# In[18]:


pred = mlp.predict(X_test)
pred


# ## Evaluation metrics- Confusion matrix and F2 score

# In[19]:


from sklearn.metrics import classification_report,confusion_matrix

confusion_matrix(y_test,pred)


# In[20]:


print(classification_report(y_test,pred))


# TOTAL CODE :

# In[2]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
bnotes = pd.read_csv("C:\\Users\\kgnan\\Downloads\\bank_note_data.csv")
X = bnotes.drop('Class', axis=1)
y = bnotes['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)

mlp = MLPClassifier(hidden_layer_sizes=(64,60,50),max_iter=500, activation='relu')
mlp.fit(X_train,y_train)
pred = mlp.predict(X_test)
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))


# In[ ]:




