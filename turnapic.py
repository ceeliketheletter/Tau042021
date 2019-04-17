'''
this program will attempy to rotate an array by some degrees
'''

import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as pf
from math import  acos
from math import pi
from scipy import ndimage


#load fits files
F606W = pf.open("/Users/CEE/Desktop/cleaned/F606W.fits")                                                                                                                          
F814W1 = pf.open("/Users/CEE/Desktop/cleaned/F814W1.fits")    

F475W = pf.open("/Users/CEE/Desktop/cleaned/F475W.fits")
F814W2 = pf.open("/Users/CEE/Desktop/cleaned/F814W2.fits")

#final_img_kp = pf.open("/Users/CEE/Desktop/research/final_img_kp.fits")
#final_img_j_pad = pf.open("/Users/CEE/Desktop/research/final_img_j_pad.fits")

#specifying the [1] matrix that has intensities

#F606W_data = F606W[1].data
           #F606W[1].header   Reference pixel/CRPIX1,2:( 2100.0, 1024.0 )                                                                                                                         
#F814W1_data = F814W1[1].data
           #F814W[1].header  Reference pixel/CRPIX1,2:( 2100.0, 1024.0 )   

#F475W_data = F475W[1].data
           #F475W[1].header   Reference Pixel: (2062.0 , 2192.5 )

#F814W2_data = F814W2[1].data
           #F814W2[1].header  Reference Pixel: (2062.5, 2193.0 )


def angle(pic):
 '''[In] : Filter name
   [Out]: The angle the picture needs to be rotated for North to be up 
 '''

 delta_squared = ( pic[1].header["CD1_1"]**2  + pic[1].header["CD2_1"]**2 )

 delta = (delta_squared)**.5

 print 'delta : ' ,delta

 cosine_angle = ((pic[1].header["CD1_1"]) / delta )

 angle = acos (cosine_angle)

 print angle, ' radians'

 #degrees = 180 + (angle * (180/pi))   #F606W                           #converting radians to degrees
 #degrees = 180 + (angle * (180/pi))   #F814W1
 #degrees = 180 + (angle * (180/pi))   #F814W2
 degrees = 180 + (angle * (180/pi))   #F475W
 

 print degrees, ' degrees'
 

 print 'This is the angle the picture needs to be rotated for North to be up '
 print 'Uncomment the code to run rotate(pic, degrees) as well as to save the file'
 
 #rotate(pic, degrees)  #only uncomment this what u wanna make a thing



def rotate(pic,degrees):


    m = ndimage.interpolation.rotate(pic[0].data, degrees, axes=(1,0), reshape=True, output=None, order=3, mode='constant', cval=0.0, prefilter=True)


                                                                                                                               

    plt.imshow(m, origin='lower', vmin=-.2, vmax=1)  #this views in python                                                                                                                       
    plt.colorbar()
    plt.show()

    #pf.writeto('F814W2_turned.fits', m) #this saves it as a fits file 

