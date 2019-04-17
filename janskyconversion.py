'''This program will take an object as an input, and convert the pixel values into Janskys'''

import scipy 
import astropy.io.fits as pf
import numpy as np
import glob 

#import fits file

F606W_lessnoise = pf.open("/Users/CEE/Desktop/cleaned/F606W_lessnoise.fits")
F814W1_lessnoise = pf.open("/Users/CEE/Desktop/cleaned/F814W1_lessnoise.fits")
F814W2_lessnoise = pf.open("/Users/CEE/Desktop/cleaned/F814W2_lessnoise.fits")
F475W_lessnoise = pf.open("/Users/CEE/Desktop/cleaned/F475W_lessnoise.fits")
final_img_j_pad_lessnoise = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_lessnoise.fits")
final_img_kp_lessnoise = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_lessnoise.fits")

#make it all an array

F606W = np.array(F606W_lessnoise[0].data)
F475W =np.array(F475W_lessnoise[0].data)
F814W1 =np.array(F814W1_lessnoise[0].data)
F814W2 =np.array(F814W2_lessnoise[0].data)
final_img_j_pad =np.array(final_img_j_pad_lessnoise[0].data)
final_img_kp =np.array(final_img_kp_lessnoise[0].data)

files = [F606W, F475W, F814W1, final_img_kp, final_img_j_pad]

print "To run, type 'convert( ' [filename] ' )"

def convert(filename):

        c = 2.998e8
        ergperstowattconversion = 0.00000010 #watts
        cm2tom2conversion = 0.0001 #m2
        angstromtometersconversion = 1e-10 #m
        janskyfactor = 1e-26
        pixscale_475 = 0.03962306984   #arcseconds
  

        if filename == 'F606W':
            image = F606W
            inversesensitivity = 7.8624312E-20 
            wavelength = 6.06e-7
            wavelenth2overc = (wavelength)**2 / c
            factors = inversesensitivity * ergperstowattconversion  * wavelenth2overc / (cm2tom2conversion * angstromtometersconversion * janskyfactor)
            

        if filename == 'F475W':
            image = F475W
            inversesensitivity =  2.57266105E-19 
            wavelength = 4.773e-7
            wavelenth2overc = (wavelength)**2 / c
            factors = inversesensitivity * ergperstowattconversion  * wavelenth2overc / (cm2tom2conversion * angstromtometersconversion * janskyfactor)
            
  
        if filename == 'F814W1':
            image = F814W1
            inversesensitivity = 7.0331646E-20  
            wavelength = 8.14e-7
            wavelenth2overc = (wavelength)**2 / c
            factors = inversesensitivity * ergperstowattconversion  * wavelenth2overc / (cm2tom2conversion * angstromtometersconversion * janskyfactor)
            
            

        if filename == 'F814W2':
            image = F814W2
            inversesensitivity =  1.5304799E-19 
            wavelength = 8.14e-7
            wavelenth2overc = (wavelength)**2 / c
            factors = inversesensitivity * ergperstowattconversion  * wavelenth2overc / (cm2tom2conversion * angstromtometersconversion * janskyfactor)
            
        
     
        if filename == 'final_img_j_pad':
            jpadcounts = 2058045.8
            jpadjansky = 0.0010827
            image = final_img_j_pad
            factors = jpadjansky/jpadcounts
            
            
    
        if filename == 'final_img_kp':
            image = final_img_kp
            kpcounts = 1215444.9 
            kpjansky = 0.001215
            factors = kpjansky/kpcounts

        ''' 
        for x in range(len(image[0])):
            x = x * pixscale_475
            
            
        for y in range(len(image)):
            y = y * pixscale_475
        '''
        
                  
            
        newfile = image *  factors 
        title = filename + '_jansky1.fits' 
        pf.writeto(title, newfile)
        print "Your file may have been saved!" 
        
        
  