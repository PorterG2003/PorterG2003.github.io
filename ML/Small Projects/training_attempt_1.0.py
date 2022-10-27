#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 23:03:31 2019

@author: porterg2003
"""

from scipy import optimize

class trainer(object):
    def __init__(self, N):
        #Make Local reference to network:
        self.N = N
        self.group = 20000
        self.iteration = 0
        self.X = []
        self.Y = []
        
    def split(self, x, y):
        start = 0
        for i in range(len(x)/self.group):
            self.X.append(x[start:self.group])
            self.Y.append(y[start:self.group])
            start += self.group
        return self.X, self.Y
    
    def avgGrad(self, x,y):
        groupindex = numpy.random.randint(0, high=len(x))
        
        W1grad, W2grad, W3grad = self.N.costPrime(x[groupindex][0], y[groupindex][0])
        
        for i in range(self.group -1):
            a, b, c = self.N.costPrime(x[groupindex][i+1], y[groupindex][i+1])
            W1grad += a
            W2grad += b
            W3grad += c
            
        W1grad = numpy.true_divide(W1grad, self.group)
        W2grad = numpy.true_divide(W2grad, self.group)
        W3grad = numpy.true_divide(W3grad, self.group)
        return W1grad, W2grad, W3grad
    
 #   def check(self, x, y, g1, g2, g3, m):
        #keep going = True
        #stop = False
        
        
        
#    def train(self, X, y):
        
