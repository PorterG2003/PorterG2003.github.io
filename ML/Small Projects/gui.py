#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:39:05 2019

@author: porterg2003
"""

# ***** Getting Data *****
from mnist import MNIST
mndata = MNIST('./Database')
train_images, train_labels =  mndata.load_training()
test_images, test_labels = mndata.load_testing()


# ***** Making GUI *****
from Tkinter import *
import tkMessageBox

root = Tk()

imageLabel = Label(root, text='Image', font=("Courier", 24))
imageLabel.grid()

imageFrame = Frame(root)
imageFrame.grid(row=1, column=0)
image = Canvas(imageFrame, width=290, height=290)
image.pack()


k = 0
for i in range(28):
    for j in range(28):
        color = 'rgb(' + test_images[0][k] + ',' + test_images[0][k] + ',' + test_images[0][k] + ')'
        image.create_rectangle(j*10, i*10, (j+1)*10, (i+1)*10, fill=color)


root.mainloop()