'''                                                                            
this function takes points along the disk, creates a line, determines angle from horizontal, and rotates the image that much.                                 '''


from scipy import stats
import numpy as np
import pylab
import matplotlib.pyplot as plt
import astropy.io.fits as pf
from math import  asin
from scipy import ndimage
from math import atan
from scipy import ndimage


F475W_cut_corners = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_cut_corners.fits") 
F606W_shifted = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_shifted.fits")
F814W1_shifted = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_shifted.fits")
F814W2_shifted = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_shifted.fits")


F475W_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_horizontal.fits") 
F606W_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal.fits")
F814W1_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_horizontal.fits")
F814W2_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_horizontal.fits")

F606W_horizontal_1 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal_1.fits")
F475W_horizontal_1 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_horizontal_1.fits")
F814W1_horizontal_1 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_horizontal_1.fits")
F814W2_horizontal_1 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_horizontal_1.fits")

F814W2_cropped_better = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_cropped_better.fits")

F606W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal_final.fits")
F475W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_horizontal_final.fits")
F814W1_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_horizontal_final.fits")
F814W2_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_horizontal_final.fits")


print "This code will pull the brightest points along the disk, create a parabola, finding the peak of the parabola, determines angle from horizontal, and rotate the image that much."
print " "
print "To run, type: main([wavelength_shifted)] or main([wavelength_horizontal])"

def main(pic):
    
    
    if pic == F606W_shifted or pic == F606W_horizontal or pic == F606W_horizontal_final:
            name = 'F606W'
    if pic == F814W1_shifted or pic == F814W1_horizontal or pic == F814W1_horizontal_final:
            name = 'F814W1'
    if pic == F475W_cut_corners or pic == F475W_horizontal or pic == F475W_horizontal_final:
            name = 'F475W'
    if pic == F814W2_shifted or pic == F814W2_horizontal or pic == F814W2_cropped_better or pic == F814W2_horizontal_final:
            name = 'F814W2'
    

    pic = pic[0].data

    xcoords = []
    ycoords = []
    
      
    question = raw_input("Do you already have a degree of rotation? y/n: " )
    if question == 'y':
         degrees = np.float(raw_input("Degree to rotate image: "))
         apply(pic, degrees, name)
         
    if question == 'n':
        


        #This is for individually choosing points
        '''
        
        '''
       # going = raw_input('Would you like to proceed? y/n ')
       # while going == 'y':
        
       #     userimput =  raw_input('X coordinate: ')
       #     x_coord1 = userimput
   #	     userimput = raw_input('Y coordinate: ')
   #         y_coord1 = userimput
    #        going = raw_input('Would you like to proceed? y/n ')
     #       xcoords.append(float(x_coord1))
      #      ycoords.append(float(y_coord1))
      
            
        
        
        #This is for having the code select the brightest points 
        
        startvalue = np.int(raw_input("What x-pixel should the code start at?  "))
        endvalue = np.int(raw_input("What x-pixel should the code end at?  "))
    
    
     
 
 
 
        new = raw_input("Run new method? ")
        if new == 'n':
            apply(pic, degrees, name)
        elif new == 'y':

 

 
            '''our method of using the brightest pixel is inherently flawed because it uses integers instead of floats, so I should do a 1D centroid on each yvalue to put into another array, and that array is then the ycoords, but it will be in floats. '''
 
            xpoints = []
            ymaxpoints = []
            ycentpoints = []
            #disk_bottom = raw_input ("What y pixel is the bottom of the disk?")
            #disk_top = raw_input ("What y pixel is the top of the disk?")
 
            print " "
 
            for i in range(startvalue, endvalue):
                vertrange = pic[0:len(pic[startvalue]), i:i+1] #in y:x form
            
                #the x doesnt change
                xpoints.append(i)
            
                #first find the brightest point so we know where the disk is
            
                ymax = np.argmax(vertrange)
                #print 'ymax: ', ymax
                #print 'intensity: ', pic[ymax, i] 
            
                ymaxpoints.append(ymax)
 
                #now take a window around the largest point and take the centroid of the window to find the float brightest point
     
                window = 5.0
            
                rangestart = ymax - window
                rangestop = ymax + window 
                
                vector = pic[rangestart:rangestop +1, i:i+1]
                vector = np.reshape(vector, 2 * window + 1)
                vector2 = np.arange(rangestart,rangestop + 1,1)
                vector3 = vector * vector2
                #print vector
                #print vector2
                #print vector3
                
                centroid = sum(vector3) / sum(vector)
                #print centroid
                ycentpoints.append(centroid)
                
                
            points(xpoints, ycentpoints, pic, startvalue, endvalue, name) #call the next function
    
        '''
        
        #print len(pic[startvalue])
    
        #print pic[0:len(pic[startvalue]), startvalue]  #pic[0:400, startvalue]
        
        
        yo = np.argmax(pic[0:len(pic[startvalue]), startvalue] )
        
        
        
        #print 'location of largest pixel: ' , startvalue, ',' , yo
        
    	

        
        for i in range(startvalue, endvalue):
            vertrange = pic[0:len(pic[startvalue]), i:i+1] #in y:x form
            xcoords.append(i)
            
            ymax = np.argmax(vertrange)
            ycoords.append(ymax)
    
        
        #print xcoords
        #print ycoords
    	
        points(xcoords, ycoords, pic, startvalue, endvalue, name) #call the next function
        '''


def points(xcoords, ycoords, pic, startvalue, endvalue, name):


# Fit the model
 x = np.array(xcoords)

 y = np.array(ycoords)
 
 print " " 
 print 'x_points: ', x 
 print 'y_points: ', y
 print " "

 stuff = np.polyfit(x, y, 2)
 slope = stuff[1]
 print 'm = ', slope 
 intercept = stuff [2]
 print 'b = ', intercept
 parabola = stuff[0]
 print 'parabola = ', parabola
 
 
 
 #slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
 # Calculate some additional outputs
 
 predict_y = intercept + slope * x + parabola * x**2
 y_max = np.argmax(predict_y)
 
 print 'predicted y_max: ', y_max

 center = x[y_max]
 print 'predicted center x-pixel: ', center
 print 'predicted center y-pixel: ', y[y_max]
 
 '''
 zerox = []
 for i in x:
     i = i -center
     zerox.append(i)

 x = np.array(zerox)
'''
 
 
 #print predict_y #[center]
 
 

# Plotting the first go (uncropped)

 pylab.plot(x, y, 'o')
 pylab.plot(x, predict_y, 'k-')
 pylab.show()


 remove = raw_input( "Remove any points? " )
 while remove == 'y':
     point = np.int(raw_input( "What number data point is it? "))
     
     
     xfirst = x[0:point-1]
     xsecond = x[point: len(x)]
     
     x = np.array(list(xfirst) + list(xsecond))
     
     yfirst = y[0:point-1]
     ysecond = y[point: len(y)]
     
     y = np.array(list(yfirst) + list(ysecond))
     
     pylab.plot(x, y, 'o')
     #pylab.plot(x, predict_y, 'k-')
     pylab.show()
 
     remove = raw_input( "Remove any more points? " )
    

 print " "
 print 'Now to even out the arrays...'
 print " " 

 
 insertwindow = raw_input("Automate window radius? (y/n) ")
 if insertwindow == 'y':
 
    window1 = endvalue - center #need to find if start or end values are closer
    window2 = center - startvalue
    if window1 < window2:
        window = window1
    elif window2 < window1:
        window = window2
    elif window1 == window2:
        window = window1
     
    print 'window radius: ', window
 
 elif insertwindow == 'n':
     window = np.int(raw_input("Window radius: "))
 
 
 print " " 



 
 newstart = y_max - window + 1
 newstop = y_max + window 
 
 print 'y_max - window : ' , newstart
 print 'y_max + window : ' , newstop
 
 xnew = x[newstart : newstop] - center  #crop the x array  #- center exists to try to shift the graph to center on zero
 ynew = y[newstart : newstop]  #crop the y array

 #print 'xnew: ' ,xnew
 #print 'ynew: ', ynew
 
 print " " 
 
 stuf = np.polyfit(xnew, ynew, 2)
 #print stuf
 parabola = stuf[0]
 print 'parabola = ', parabola
 slope = stuf[1]
 print 'm = ', slope 
 intercept = stuf [2]
 print 'b = ', intercept

 
 print " " 
 
 predict_y = intercept + slope * xnew + parabola * xnew**2
 
 y_max = np.argmax(predict_y)
 
 print 'predicted y_max: ', y_max
 
 center = xnew[y_max]
 print 'predicted center x-pixel: ', center
 print 'predicted center y-pixel: ', ynew[y_max]
 
 print " "
 
 # Plotting the cropped version after taking a window of points
 pylab.plot(xnew, ynew, 'o')
 pylab.plot(xnew, predict_y, 'k-')
 pylab.show()
 


 #plotting the estimated parabola on the actual image
 plt.imshow(pic, origin='lower', vmin=0, vmax=.5)
 plt.colorbar()
 
 plt.plot(xnew, predict_y, linestyle = '-', linewidth=2, color = 'k')
 plt.show()



 #take the derivative 

#recall tan(angle) = slope
 angle = atan(slope)
 print 'angle from horizontal: ',angle, 'in radians'
 degrees =  angle *  57.2957795 
 print degrees, ' degrees'

 
 print " " 

                
            
                                 
 apply(pic, degrees, name)  
 




def apply(pic, degrees, name):
  
 m = ndimage.interpolation.rotate(pic, degrees, axes=(1,0), reshape=False, output=None,  order=3, mode='constant', cval=0.0, prefilter=True)

 print "Your image has been rotated!"

 plt.imshow(m, origin='lower', vmin=-0, vmax=.5) 
 plt.colorbar()
 plt.show()                                                                                         




        
 version = raw_input("What extension is this? ")    
 title = name + version + '.fits'            
 pf.writeto(title, m)
 print " "
 
 print "Your file may have been saved!"



