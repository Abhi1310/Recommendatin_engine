# -*- coding: utf-8 -*-
"""Basic_Matrix Factorisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aAVjM33dJJMULNGcMJ9i38-_U5AzkoUP
"""

import numpy

def matrix_f(rating_matrix, user_matrix , item_matrix , no_of_latent_features , steps = 5000 , alpha = .0002 , beta = .02 ):
  item_matrix = item_matrix.T
  for step in range(steps):
    for i in range(len(rating_matrix)): # to change rows
      for j in range(len(rating_matrix[i])): # to change columns
        if rating_matrix[i][j] > 0 : # to check for positive rating
          eij = rating_matrix[i][j] - numpy.dot(user_matrix[i,:],item_matrix[:,j])  # difference between actual and measured rating
          for k in range(no_of_latent_features):
            user_matrix[i][k] = user_matrix[i][k] + alpha * (2 * eij * item_matrix[k][j] - beta * user_matrix[i][k]) # updated value for user_matrix
            item_matrix[k][j] = item_matrix[k][j] + alpha * (2 * eij * user_matrix[i][k] - beta * item_matrix[k][j])  # updated value for item_matrix
    
    e = 0
    for i in range(len(rating_matrix)):
      for j in range(len(rating_matrix[i])):
        if rating_matrix[i][j] > 0:
          e = e + pow(rating_matrix[i][j] - numpy.dot(user_matrix[i,:],item_matrix[:,j]),2)  # mse
          for k in range(no_of_latent_features):
            e = e + (beta/2) * ( pow(user_matrix[i][k],2)  +  pow(item_matrix[k][j],2)) # mse with L2 penelty term to avoid overfitting
      
    if e < 0.001:
      break

  return user_matrix , item_matrix.T

R = [[5,3,0,1],
     [4,0,0,1],
     [1,1,0,5],
     [1,0,0,4],
     [0,1,5,4]
     ]
R =  numpy.array(R)
n_users = len(R)
n_items = len(R[0])
n_latent_features  = 2 

P = numpy.random.rand(n_users,n_latent_features)
Q = numpy.random.rand(n_items , n_latent_features)

nP , nQ = matrix_f(R,P,Q,n_latent_features)
nR = numpy.dot(nP , nQ.T )
print(nR)

