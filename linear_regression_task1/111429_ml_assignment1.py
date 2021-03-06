# -*- coding: utf-8 -*-
"""111429_ML_assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x_Hg1r2hOrycHcOqKISG01hSOPpqgAUP
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset_size=100

x=np.random.normal(100, 1, dataset_size)

y=np.random.normal(70000, 10000, dataset_size)

dataset = {'Office size(x)': x,
        'Office price(y)': y,
       }

pd.DataFrame(dataset)

plt.scatter(x,y)
plt.show

def mean_squared_error(y, y_pred, n):
  sum = 0

  for i in range (0,n):
    difference = y[i] - y_pred[i]  
    squared_difference = difference**2
    sum = sum + squared_difference

  MSE = sum/n

  return MSE

def gradient_descent(x, y, learning_rate, epochs):
  m = 0
  c = 0

  n=len(x)

  for i in range(epochs): 
    y_pred = m*x + c
    D_m = (-2/n) * sum(x * (y - y_pred))
    D_c = (-2/n) * sum(y - y_pred)
    m = m - learning_rate * D_m  
    c = c - learning_rate * D_c  

    global gradient
    gradient = m

    global y_intercept
    y_intercept = c
    
  plt.scatter(x, y) 
  plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)], color='red')
  plt.show()
  return (m, c)

def predict(size):
  gradient_descent(x, y, 0.00001, 10)
  global gradient
  global y_intercept
  price = gradient * size + y_intercept
  print('Price: ' + str(price))

predict(100)