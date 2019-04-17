'''This program will take an object as an input, and convert the pixel values into Janskys'''

import scipy 
import astropy.io.fits as pf
import numpy as np
import glob 

#import fits file

F606W_lessnoise = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_lessnoise.fits")
F814W1_lessnoise = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_lessnoise.fits")
F814W2_lessnoise = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_lessnoise.fits")
F475W_lessnoise = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_lessnoise.fits")

print "This code will convert the pixel values into Janskys"
print" "

print "To run, type 'convert( wavelength_lessnoise )"

def convert(pic):
    
    
        if pic == F606W_lessnoise:
            name = 'F606W'
            wavelength = 6.06e-7
     
        elif pic == F475W_lessnoise:
            name = 'F475W'
            wavelength = 4.773e-7
     
        elif pic == F814W1_lessnoise:
            name = 'F814W1'
            wavelength = 8.14e-7
     
        elif pic == F814W2_lessnoise:
            name = 'F814W2'
            wavelength = 8.14e-7
     
        pic = pic[0].data

        c = 2.998e8
        ergperstowattconversion = 0.00000010 #watts
        cm2tom2conversion = 0.0001 #m2
        angstromtometersconversion = 1e-10 #m
        janskyfactor = 1e-26
        
        #pixscale_475 = 0.03962306984   #arcseconds
        
        wavelenth2overc = (wavelength)**2 / c
        
        print " "
        inversesensitivity = np.float(raw_input("Inverse sensitivity of filter? (in ergs/cm2/Ang/electron ) "))
        
        factors = inversesensitivity * ergperstowattconversion  * wavelenth2overc / (cm2tom2conversion * angstromtometersconversion * janskyfactor)
            
  
        '''
        if filename == 'F606W':
            inversesensitivity = 7.8624312E-20 
            

        if filename == 'F475W':
            inversesensitivity =  2.57266105E-19 
            
            
  
        if filename == 'F814W1':
            inversesensitivity = 7.0331646E-20  
            

        if filename == 'F814W2':
            inversesensitivity =  1.5304799E-19 
        '''  
        
     
        
                  
            
        newfile = pic *  factors 
        title = name + '_jansky.fits' 
        pf.writeto(title, newfile)
        print " "
        print "Your file may have been saved!" 
        
        
  