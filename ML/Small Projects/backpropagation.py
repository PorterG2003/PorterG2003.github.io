#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:08:54 2019

@author: porterg2003
"""

import numpy as np

class NN(object):
    def __init__(self):
        self.inputLayerSize = 2
        self.hiddenLayerSize = 2
        self.outputLayerSize = 2
        
        self.W1 = np.array([[.15,.25],[.20,.30]])
        self.W2 = np.array([[.40,.50],[.45,.55]])
        self.W3 = np.array([[.60,.70],[.65,.75]])
        
        self.B1 = .35
        self.B2 = .60
        
    def fwd(self, X):
        self.Z2 = np.dot(X, self.W1)
        #for i in range(len(self.Z1)):
        #    self.Z1[i] += self.B1
        self.A2 = self.reLu(self.Z2)
        self.Z3 = np.dot(self.A2, self.W2)
        #for i in range(len(self.Z2)):
        #    self.Z2[i] += self.B2
        self.A3 = self.reLu(self.Z3)
        self.Z4 = np.dot(self.A3, self.W3)
        #for i in range(len(self.Z2)):
        #    self.Z2[i] += self.B2
        self.A4 = self.reLu(self.Z4)
        
        return self.A4

    def reLu(self, z):
        for i in range(len(z)):
            for x in range(len(z[i])):
                z[i][x] = z[i][x] * (z[i][x] > 0)
        return z

    def reLuPrime(self, z):
        for i in range(len(z)):
            for j in range(len(z[i])):
                if z[i][j] <= 0:
                    z[i][j] = 0
                if z[i][j] > 0:
                    z[i][j] = 1
        return z

    def cost(self, y):
        self.yhat = self.fwd(x)
        cost = 0
        for i in range(len(y)):
            cost += ((y[i]-self.yhat[i])**2)/2
        return cost
    
    def costPrime(self, X, y):
        #Computes Gradients
        self.yhat = self.fwd(x)
        
        delta4 = np.multiply(self.yhat-y, self.reLuPrime(self.Z4))
        self.dJdW3 = np.dot(self.A3.T, delta4)
        
        delta3 = np.dot(delta4, self.W3.T)*self.reLuPrime(self.Z3)
        self.dJdW2 = np.dot(self.A2.T, delta3)  
        
        #delta2 = np.dot(delta3, self.W2)*self.reLuPrime(self.Z2)
        #self.dJdW1 = np.dot(X.T, delta2)
        
    
    def train(self, x, y, lr, il):
        
        i = 0
        while i < il:
            self.costPrime(x,y)
            self.W1 = self.W1 - np.multiply(self.W1, self.dJdW1)
            #self.W2 = self.W2 - np.multiply(self.W2, self.dJdW2)
            #self.W3 = self.W3 - np.multiply(self.W3, self.dJdW3)
            i += 1
            if i % 10 == 0:
                print i
                print self.cost(y)
                print self.W1, self.W2, self.W3
    
    
nn = NN()
x = np.array([[.05, .10]])
y = np.array([[.01, .99]])
lr = .05
#gradient = nn.gradient(Y, y, nn.A1, nn.W2)
#nn.W2 = nn.update(gradient, nn.W2, lr)
#gradient
