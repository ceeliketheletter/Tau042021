'''This program will allow the user to insert a fits image in Janskys and turn it into a fits image in magnitudes.'''
'''sumsumflux -- total flux of disk in Janskys'''
'''      m    -- total flux of disk in Mag'''   

  
import scipy 
import astropy.io.fits as pf
import numpy as np
import os


#import fits file

F606W_jansky = pf.open("/Users/CEE/Desktop/cleaned/F606W_jansky.fits")
F814W1_jansky = pf.open("/Users/CEE/Desktop/cleaned/F814W1_jansky.fits")
F814W2_jansky = pf.open("/Users/CEE/Desktop/cleaned/F814W2_jansky.fits")
F475W_jansky = pf.open("/Users/CEE/Desktop/cleaned/F475W_jansky.fits")
final_img_j_pad_jansky = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_jansky.fits")
final_img_kp_jansky = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_jansky.fits")

#make it all an array

F606W = np.array(F606W_jansky[0].data)
F475W =np.array(F475W_jansky[0].data)
F814W1 =np.array(F814W1_jansky[0].data)
F814W2 =np.array(F814W2_jansky[0].data)
final_img_j_pad =np.array(final_img_j_pad_jansky[0].data)
final_img_kp =np.array(final_img_kp_jansky[0].data)



print "to run, print: convert(['filename'], ['telescope'])" 

def convert(filename, telescope):
 
 pixscale_475 = 0.03962306984   #arcseconds
 
 c = 2.998e8
 ergperstowattconversion = 0.00000010 #watts
 cm2tom2conversion = 0.0001 #m2
 angstromtometersconversion = 1e-10 #m
 janskyfactor = 1e-26

 if telescope == 'hst':
        


        if filename == 'F606W':
            image = F606W
            
            wavelength = 6.06e-7
            wavelenth2overc = (wavelength)**2 / c
            sumsumflux = 0.00022812709717372475 #this is found using sumflux.py
            fv_vega_ergcmsA = 2.869e-9           
            factors = ergperstowattconversion  * wavelenth2overc / (cm2tom2conversion * angstromtometersconversion * janskyfactor)
            
            
            '''To find the Jansky vega equivilant'''
            fv_vega = fv_vega_ergcmsA * factors 
            print 'fv_vega: ', fv_vega #3514.34317545  #Jy  
               
            '''To get m, converting the total flux from Janskys to magnitude'''
            m = -2.5* np.log10(sumsumflux) + 2.5*np.log10(fv_vega)
            print 'm: ', m     #17.9691682344
            
            '''To convert from Janskys to Janskys per square arc second'''
            jpersqasec = image / (pixscale_475)**2 
            image = jpersqasec
            
            '''To convert from jpersqasec to magnitudes'''
           
            for i in range(len(image)):        #y direction
                for j in range(len(image[1])):   #x direction
                    pixel = image[i][j]
                    newpixel = -2.5* np.log10(pixel) + 2.5*np.log10(fv_vega)
                    image[i][j] = newpixel
            

            
            title = filename + '_magnitude.fits' 
            pf.writeto(title, image)
            print "Your file may have been saved!"
            
                
                
        if filename == 'F475W':
            image = F475W
            wavelength = 4.773e-7
            wavelenth2overc = (wavelength)**2 / c
            VEGAMAG = 25.7783
            sumsumflux = 3.9065681130212582e-05
            PHOTOFLAM = 2.5536e-19
            
            
            '''To find the Jansky vega equivilant'''
            fv_vega = (PHOTOFLAM * ergperstowattconversion* wavelenth2overc * 10**(.4 * VEGAMAG)) / (cm2tom2conversion * angstromtometersconversion * janskyfactor ) #0.000397396565949
            print 'fv_vega: ', fv_vega #3973.96565949
            
            '''To get m, converting the total flux from Janskys to magnitude'''
            m = -2.5* np.log10(sumsumflux) + 2.5*np.log10(fv_vega)
            print 'm: ', m   #20.0185717726
          
            '''To convert from Janskys to Janskys per square arc second'''
            jpersqasec = image / (pixscale_475)**2 
            image = jpersqasec
        
            '''To convert from jpersqasec to magnitudes'''
            for i in range(len(image)):
                for j in range(len(image[1])):
                    pixel = image[i][j]
                    newpixel = -2.5* np.log10(pixel) + 2.5*np.log10(fv_vega)
                    image[i][j] = newpixel
            

            
            title = filename + '_magnitude.fits' 
            pf.writeto(title, image)
            print "Your file may have been saved!"
  
        if filename == 'F814W1':
            image = F814W1
            wavelength = 8.14e-7
            wavelenth2overc = (wavelength)**2 / c
            sumsumflux = 0.0005858313557589944
            fv_vega_ergcmsA = 1.134e-9
            factors = ergperstowattconversion  * wavelenth2overc / (cm2tom2conversion * angstromtometersconversion * janskyfactor)
            
            '''To find the Jansky vega equivilant'''
            fv_vega = fv_vega_ergcmsA * factors  
            print 'fv_vega: ', fv_vega #2506.28373582 #Jy  
            
            '''To get m, converting the total flux from Janskys to magnitude'''          
            m = -2.5* np.log10(sumsumflux) + 2.5*np.log10(fv_vega)
            print 'm: ', m   #16.5781440572
            
            '''To convert from Janskys to Janskys per square arc second'''
            jpersqasec = image / (pixscale_475)**2 
            image = jpersqasec
        
            '''To convert from jpersqasec to magnitudes'''
            for i in range(len(image)):
                for j in range(len(image[1])):
                    pixel = image[i][j]
                    newpixel = -2.5* np.log10(pixel) + 2.5*np.log10(fv_vega)
                    image[i][j] = newpixel
            

            
            title = filename + '_magnitude.fits' 
            pf.writeto(title, image)
            print "Your file may have been saved!"
            
            
        if filename == 'F814W2':
            image = F814W2 
            wavelength = 8.14e-7
            wavelenth2overc = (wavelength)**2 / c
            VEGAMAG = 24.6803
            sumsumflux = 0.00029683309693477025
            PHOTOFLAM = 1.5419e-19
            
            '''To find the Jansky vega equivilant'''
            fv_vega = (PHOTOFLAM * ergperstowattconversion * wavelenth2overc * 10**(.4 * VEGAMAG)) / (cm2tom2conversion * angstromtometersconversion * janskyfactor )  #0.000253859482097
            print 'fv_vega: ', fv_vega #2538.59482097
      
            '''To get m, converting the total flux from Janskys to magnitude'''
            m = -2.5* np.log10(sumsumflux) + 2.5*np.log10(fv_vega)
            print 'm: ', m     #17.3302026662

            '''To convert from Janskys to Janskys per square arc second'''
            jpersqasec = image / (pixscale_475)**2 
            image = jpersqasec
        
            '''To convert from jpersqasec to magnitudes'''
            for i in range(len(image)):
                for j in range(len(image[1])):
                    pixel = image[i][j]
                    newpixel = -2.5* np.log10(pixel) + 2.5*np.log10(fv_vega)
                    image[i][j] = newpixel
            

            
            title = filename + '_magnitude.fits' 
            pf.writeto(title, image)
            print "Your file may have been saved!"
        
 
        
 if telescope == 'keck':
     
        if filename == 'final_img_j_pad':
            image = final_img_j_pad
            fv_vega = 1600 #Jy
            sumsumflux = 0.0015104938320814171
            
            '''To get m, converting the total flux from Janskys to magnitude'''
            m = -2.5* np.log10(sumsumflux) + 2.5*np.log10(fv_vega)
            print 'm: ', m  #15.0625025661
    
            '''To convert from Janskys to Janskys per square arc second'''
            jpersqasec = image / (pixscale_475)**2  
            image = jpersqasec
        
            '''To convert from jpersqasec to magnitudes'''
            for i in range(len(image)):
                for j in range(len(image[1])):
                    pixel = image[i][j]
                    newpixel = -2.5* np.log10(pixel) + 2.5*np.log10(fv_vega)
                    image[i][j] = newpixel
            

            
            title = filename + '_magnitude.fits' 
            pf.writeto(title, image)
            print "Your file may have been saved!"
            
            
    
        if filename == 'final_img_kp':
            image = final_img_kp
            fv_vega = 657 #Jy
            sumsumflux = 0.0027735996731618699
            
            '''To get m, converting the total flux from Janskys to magnitude'''
            m = -2.5* np.log10(sumsumflux) + 2.5*np.log10(fv_vega)
            print 'm: ', m     #13.4363039802
     
            '''To convert from Janskys to Janskys per square arc second'''
            jpersqasec = image / (pixscale_475)**2 
            image = jpersqasec
        
            '''To convert from jpersqasec to magnitudes'''
            for i in range(len(image)):
                for j in range(len(image[1])):
                    pixel = image[i][j]
                    newpixel = -2.5* np.log10(pixel) + 2.5*np.log10(fv_vega)
                    image[i][j] = newpixel
            

            
            title = filename + '_magnitude.fits' 
            pf.writeto(title, image)
            print "Your file may have been saved!"
            
       
    
 print "Complete" 