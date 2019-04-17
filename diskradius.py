''' This function will find the brightest points along the disk and make a graph, used to determine the edges of the disk'''


from scipy import stats
import numpy as np
import pylab
import matplotlib.pyplot as plt
import astropy.io.fits as pf
from math import  asin
from scipy import ndimage
from math import atan
from scipy import ndimage



F606W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal_final.fits")
F475W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_horizontal_final.fits")
F814W1_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_horizontal_final.fits")
F814W2_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_horizontal_final.fits")

print "This code will pull the brightest points along the disk and make a graph"
print " "
print "To run, type:  main(wavelength_horizontal_final)"

def main(pic):
    
    
    if  pic == F606W_horizontal_final:
            name = 'F606W'
    elif  pic == F814W1_horizontal_final:
            name = 'F814W1'
    elif  pic == F475W_horizontal_final:
            name = 'F475W'
    elif pic == F814W2_horizontal_final:
            name = 'F814W2'
    
            
                            
    pic = pic[0].data

    xcoords = []
    ycoords = []
    
    startvalue = np.int(raw_input("What x-pixel should the code start at?  "))
    endvalue = np.int(raw_input("What x-pixel should the code end at?  "))
    
    xpoints = []
    ymaxpoints = []


 
    print " "
 
    for i in range(startvalue, endvalue):
                vertrange = pic[0:len(pic[startvalue]), i:i+1] #in y:x form
            
                #the x doesnt change
                xpoints.append(i)
            
                #first find the brightest point so we know where the disk is
            
                ymax = max(vertrange)
            
                ymaxpoints.append(ymax)
                
     
    x = np.array(xpoints)

    y = np.array(ymaxpoints)
 
    print " " 
    #print 'x_points: ', x 
    #print 'y_points: ', y
    print " "
    
    q = raw_input("Find max value within disk? ")
    if q == 'y':
        mx = np.argmax(y)
        leftmax =  x[mx]
        print 'Pixel number: ', leftmax
        print 'Value: ', y[mx]
    else: 
        maxx = np.int(raw_input("Max? "))
      
    calculate = raw_input("Calculate thirds? ")
    if calculate == 'y':  
        if (maxx - startvalue) <= (endvalue - maxx):
            third = ((maxx - startvalue) /3 ) 
        elif (endvalue - maxx) < (maxx - startvalue):
            third = ((endvalue - maxx) /3 ) 
        
        left1 = maxx - third
        left2 = startvalue + third
        right1 = maxx + third
        right2 = endvalue - third
        
        print 'Third: ', third
        print "Left 1/3 ", left1
        print "Left 2/3 ", left2
        print "Right 1/3 ", right1
        print "Right 2/3 ", right2

    plt.plot(x, y, '.')
    
    title = 'Radius of ' + name
    plt.title(title)
    
    plt.show() 
    


        