#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: porterg2003
"""

# ***** TODO *****
'''
-------------------------------------------------------------------------------

fix delta2 and djdw1 in NeuralNet.CostPrime()

-------------------------------------------------------------------------------

make update function with a iteration limit
^^after^^
make check function to stop update function

-------------------------------------------------------------------------------

beautify gui

-------------------------------------------------------------------------------
'''



# ***** Getting Data *****
import numpy
from mnist import MNIST

mndata = MNIST('./Database')
train_images, train_labels =  mndata.load_training()
test_images, test_labels = mndata.load_testing()
train_labels_formatted = []
test_labels_formatted = []
ni = [0,0,0,0,0,0,0,0,0,0]
for l in train_labels:
    ni[l] = 1
    train_labels_formatted.append(ni)
    ni = [0,0,0,0,0,0,0,0,0,0]
for l in test_labels:
    ni[l] = 1
    test_labels_formatted.append(ni)
    ni = [0,0,0,0,0,0,0,0,0,0]




# ***** Neural Network *****
class NeuralNet(object):
    def __init__(self):
        self.inputLayerSize = 784
        self.hiddenLayerSize1 = 28
        self.hiddenLayerSize2 = 28
        self.outputLayerSize = 10

        #self.W1 = numpy.random.randn(self.inputLayerSize, self.hiddenLayerSize1)
        #self.W2 = numpy.random.randn(self.hiddenLayerSize1, self.hiddenLayerSize2)
        #self.W3 = numpy.random.randn(self.hiddenLayerSize2, self.outputLayerSize)
        
        self.W1 = []
        self.W2 = []
        self.W3 = []
        for i in range(self.inputLayerSize):
            self.W1.append([])
        for i in range(self.hiddenLayerSize1):
            self.W2.append([])
        for i in range(self.hiddenLayerSize2):
            self.W3.append([])
        for i in self.W1:
            for j in range(self.hiddenLayerSize1):
                i.append(0.5)
        for i in self.W2:
            for j in range(self.hiddenLayerSize2):
                i.append(0.5)
        for i in self.W3:
            for j in range(self.outputLayerSize):
                i.append(0.5)
                
        self.W1 = numpy.array(self.W1)
        self.W2 = numpy.array(self.W2)
        self.W3 = numpy.array(self.W3)
        #self.B1 = numpy.random.randn(self.hiddenLayerSize1)
        #self.B2 = numpy.random.randn(self.hiddenLayerSize2)
        #self.B3 = numpy.random.randn(self.outputLayerSize)

    def fwd(self, X):
        self.Z2 = numpy.dot(X, self.W1)
        #for i in self.Z2:
        #    i += self.B1
        self.A2 = self.reLu(self.Z2)
        self.Z3 = numpy.dot(self.A2, self.W2)
        #for i in self.Z3:
        #    i += self.B2
        self.A3 = self.reLu(self.Z3)
        self.Z4 = numpy.dot(self.A3, self.W3)
        #for i in self.Z4:
        #    i += self.B3
        yhat = self.reLu(self.Z4)
        return yhat

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

    def cost(self, y, a):
        self.yhat = NN.fwd(x)
        cost = 0
        for i in range(len(y)):
            cost += (y[i]-self.yhat[i])**2/2
        return cost
    
    def costPrime(self, X, y):
        #Computes Gradients
        self.yhat = self.fwd(X)
        
        delta4 = numpy.multiply(self.yhat-y, self.reLuPrime(self.Z4))
        self.dJdW3 = numpy.dot(self.A3.T, delta4)
        
        delta3 = numpy.dot(delta4, self.W3.T)*self.reLuPrime(self.Z3)
        self.dJdW2 = numpy.dot(self.A2.T, delta3)  
        
        delta2 = numpy.dot(delta3, self.W2)*self.reLuPrime(self.Z2)
        self.dJdW1 = numpy.dot(X.T, delta2)
        #delta2 must be of size (60000, 28)
        
        return self.dJdW1, self.dJdW2, self.dJdW3
    

# ***** Training the Neural Network *****
        
from scipy import optimize

class trainer(object):
    def __init__(self, N):
        #Make Local reference to network:
        self.N = N
        self.num_of_groups = 30000
        self.iteration = 0
        self.X = []
        self.Y = []
        
        
    #split x and y into groups
    #adapted from http://code.activestate.com/recipes/425397-split-a-list-into-roughly-equal-sized-pieces/
    def group(self, x, y):
        x_grouped = []
        splitsize = 1.0/self.num_of_groups*len(x)
        for i in range(self.num_of_groups):
                x_grouped.append(x[int(round(i*splitsize)):int(round((i+1)*splitsize))])
                
        y_grouped = []
        for i in range(self.num_of_groups):
                y_grouped.append(y[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        
        self.X, self.Y = x_grouped, y_grouped
    
    #take random group then find avg gradient
    def rand_grad(self, x, y):
        ran_grp_ind = numpy.random.randint(0, high=len(x))
        dJdW1, dJdW2, dJdW3 = NN.costPrime(T.X[ran_grp_ind], T.Y[ran_grp_ind])
        return numpy.mean(dJdW1), numpy.mean(dJdW2), numpy.mean(dJdW3)
        
    
    
    
 #   def check(self, x, y, g1, g2, g3, m):
        #keep going = True
        #stop = False
        
        
        
#    def train(self, X, y):
        



#def main():
x, y, X_test, Y_test = numpy.array(train_images, dtype=float), numpy.array(train_labels_formatted, dtype=float), numpy.array(test_images), numpy.array(test_labels_formatted)
NN = NeuralNet()
T = trainer(NN)


#main()


# ***** Making GUI *****
from Tkinter import *
import tkMessageBox

example = 5

root = Tk()

imageLabel = Label(root, text='Image', font=("Courier", 24))
imageLabel.grid()

labelLabel = Label(root, text='Label', width=16, font=("Courier", 24))
labelLabel.grid(row=0, column=1)

labelLabel = Label(root, text='Output', width=16, font=("Courier", 24))
labelLabel.grid(row=0, column=2)

label = Label(root, text=str(test_labels[example]), font=("Courier", 200))
label.grid(row=1, column=1)

label = Label(root, text=str(NN.fwd(x)[example]), font=("Courier", 10))
label.grid(row=1, column=2)

imageFrame = Frame(root)
imageFrame.grid(row=1, column=0)
image = Canvas(imageFrame, width=280, height=280)
image.pack()


def fromRGB(rgb):
    #translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb


k = 0
for i in range(28):
    for j in range(28):
        color = fromRGB((test_images[example][k],test_images[example][k],test_images[example][k]))
        image.create_rectangle(j*10, i*10, (j+1)*10, (i+1)*10, fill=color, outline=color)
        k +=1


root.mainloop()
