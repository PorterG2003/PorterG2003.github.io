#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:51:03 2019

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

example = 5

root = Tk()

imageLabel = Label(root, text='Image', font=("Courier", 24))
imageLabel.grid()

labelLabel = Label(root, text='Label', width=16, font=("Courier", 24))
labelLabel.grid(row=0, column=1)

label = Label(root, text=str(test_labels[example]), font=("Courier", 200))
label.grid(row=1, column=1)

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
