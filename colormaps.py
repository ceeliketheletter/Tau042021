'''This program will take in an object in magnitudes and subract the first one from the second to get a color map!'''


import scipy 
import astropy.io.fits as pf
import numpy as np
import os


#import fits file

F606W_magnitude = pf.open("/Users/CEE/Desktop/cleaned/F606W_magnitude.fits")
F814W1_magnitude = pf.open("/Users/CEE/Desktop/cleaned/F814W1_magnitude.fits")
F814W2_magnitude = pf.open("/Users/CEE/Desktop/cleaned/F814W2_magnitude.fits")
F475W_magnitude = pf.open("/Users/CEE/Desktop/cleaned/F475W_magnitude.fits")
final_img_j_pad_magnitude = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_magnitude.fits")
final_img_kp_magnitude = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_magnitude.fits")

#make it all an array

F606W = np.array(F606W_magnitude[0].data)
F475W =np.array(F475W_magnitude[0].data)
F814W1 =np.array(F814W1_magnitude[0].data)
F814W2 =np.array(F814W2_magnitude[0].data)
final_img_j_pad =np.array(final_img_j_pad_magnitude[0].data)
final_img_kp =np.array(final_img_kp_magnitude[0].data)


first = input('First: ') #OMIGOD AT LONG LAST IVE DISCOVERED THE THING THAT MAKES IT NOT A STRING WITH USER INP
second = input('Second: ')   #this is a variable!

newfile = first - second
    
uno = raw_input('first: ')   #this is a string!
dos = raw_input('second: ')
        
        
        
filename = uno + '-' + dos
    
    
    
title = filename + '_color.fits' 
pf.writeto(title, newfile)
print "Your file may have been saved!"