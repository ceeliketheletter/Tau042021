'''This program will take a 10x10 region of space in an image, with user imput about the location, and take the median. The median will be subtracted from the intensity over the whole image. This will remove the background noise'''

import scipy 
import astropy.io.fits as pf
import numpy as np
import glob 

#import fits file

F606W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal_final.fits")
F814W1_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_horizontal_final.fits")
F814W2_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_horizontal_final.fits")
F475W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_horizontal_final.fits")




print "This code will take a 10x10 region of space in an image, with user imput about the location, and take the median. The median will be subtracted from the intensity over the whole image. "
print " "
print "To run, type: noise(wavelength_horizontal_final)"


def noise(pic):

 if pic == F606W_horizontal_final:
     name = 'F606W'
     
 elif pic == F475W_horizontal_final:
     name = 'F475W'
     
 elif pic == F814W1_horizontal_final:
     name = 'F814W1'
     
 elif pic == F814W2_horizontal_final:
     name = 'F814W2'
     
 pic = pic[0].data
     
 print "Open your chosen file in DS9, and choose a single pixel with 10x10 distance around it, pretty close to the disk"

 print " "
 xpix = np.int(raw_input("X-coordinate of pixel: "))
 ypix = np.int(raw_input("Y-coordinate of pixel: "))
 print " " 

 ymin = int(ypix)-5
 ymax = int(ypix)+5
 xmin = int(xpix)-5
 xmax = int(xpix)+5



 region = pic[ymin:ymax, xmin:xmax] 

 median = np.median(region)

 print " " 
 print 'The median of this 10x10 region is: ', median
 print " " 

 newfile = pic - median 

 
 title = name + '_lessnoise.fits' 

 pf.writeto(title, newfile)

 print "Your file may have been saved!"
