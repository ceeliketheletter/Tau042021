'''This program will slice an image with a jet in it, to take out the disk and piece the jet together, then find the brightest points for each pixel along the jet, to determine it's final pixel location/width'''


from scipy import stats
import numpy as np
import pylab
import matplotlib.pyplot as plt
import astropy.io.fits as pf
from math import  asin
from scipy import ndimage
from math import atan


F606W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal_final.fits")

print "This code will isolate the jet, then find brightest points along the jet and make a graph"
print " "
print "To run, type:  main(wavelength_horizontal_final)"


def main(pic):
    
    
    if  pic == F606W_horizontal_final:
            name = 'F606W'
            
    pic = pic[0].data

    xcoords = []
    ycoords = []
    
    
    #Cut out the disk
    print " "
    print "We will first isolate the jet"
    print " "
    disktop = np.int(raw_input("What y-pixel is the peak of the top nebulae of the disk? "))
    jettop = np.int(raw_input("What y-pixel is the top of the jet? "))
    diskbottom = np.int(raw_input("What y-pixel is the bottom of the lower nebulae of the disk? "))
    jetbottom = np.int(raw_input("What y-pixel is the bottom of the jet? "))
    
    diskstart = np.int(raw_input("Left endpoint of disk? "))
    diskstop = np.int(raw_input("Right endpoint of disk? "))
    
    top = pic[disktop:jettop, diskstart:diskstop]
    bottom = pic[jetbottom:diskbottom, diskstart:diskstop]
    
    
    
    plt.imshow(top)
    plt.show()
    plt.imshow(bottom)
    plt.show()
    
    frankenstein = np.vstack((top,bottom))
    plt.imshow(frankenstein)
    plt.show()
    
    xpoints = []
    ymaxpoints = []
    
    for i in range(diskstart, diskstop):
                vertrange = pic[0:len(pic[diskstart]), i:i+1] #in y:x form
            
                #the x doesnt change
                xpoints.append(i)
            
                #first find the brightest point so we know where the disk is
            
                ymax = max(vertrange)
            
                ymaxpoints.append(ymax)
                
     
    x = np.array(xpoints)

    y = np.array(ymaxpoints)
    
    mx = np.argmax(y)
    jetmax =  x[mx]
    print " " 
    print 'Jet Maximum Pixel: ', jetmax
    print 'Value: ', y[mx]
    print " "
    
    plt.plot(x, y, '.')
    
    title = 'Jet of ' + name
    plt.title(title)
    
    plt.show() 
    