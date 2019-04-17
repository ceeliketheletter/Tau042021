
'''Sum the total flux of a designated region'''

import astropy.io.fits as pf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import ndimage
from math import asin, pi

#Load up fits files                                                                                                                                                                              

#load fits files                                                                                                                                                                                 


F606W_horizontal = pf.open("/Users/CEE/Desktop/_new/F606W_horizontal.fits")
F814W1_horizontal = pf.open("/Users/CEE/Desktop/_new/F814W1_horizontal.fits")
F475W_horizontal = pf.open("/Users/CEE/Desktop/_new/F475W_horizontal.fits")
final_img_j_pad_horizontal = pf.open("/Users/CEE/Desktop/_new/final_img_j_pad_horizontal.fits")
final_img_kp_horizontal = pf.open("/Users/CEE/Desktop/_new/final_img_kp_horizontal.fits")

final_img_j_pad_horizontal_lessnoise = pf.open("/Users/CEE/Desktop/_new/final_img_j_pad_horizontal_lessnoise.fits")
final_img_kp_horizontal_lessnoise = pf.open("/Users/CEE/Desktop/_new/final_img_kp_horizontal_lessnoise.fits")


F606W_converted = pf.open("/Users/CEE/Desktop/cleaned/F606W_converted.fits")
F814W1_converted = pf.open("/Users/CEE/Desktop/cleaned/F814W1_converted.fits")
F814W2_converted = pf.open("/Users/CEE/Desktop/cleaned/F814W2_converted.fits")
F475W_converted = pf.open("/Users/CEE/Desktop/cleaned/F475W_converted.fits")
final_img_j_pad_converted = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_converted.fits")
final_img_kp_converted = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_converted.fits")


print 'print sumflux([pic_whatever])'

def sumflux(pic):   #, starcoordx, starcoordy):

     
     array = pic[0].data

     window = 0   #10 for binary star            #considering the region 5x around                                                                                                                                    
     lowy = 82      #starcoordy - window - 3          
     highy =  220     #starcoordy + window + 3
     lowx =    101      #starcoordx - window
     highx =   257       #starcoordx + window


     region = array[lowy:highy, lowx: highx] #takes in the coordinates, spits out an intensity                                                                                                   
     print 'Shape of Region : ' , region.shape
                                                                                
     
     
       
     
    
     sumflux = sum(i for i in region)
     sumsumflux = sum(sumflux)
     print 'sumsumflux = ', sumsumflux
     return sumsumflux

     #print 'Intensity : ', region[(centroid5)] #this is the intensity at the centroid20 coordinate                                                                                               

   
    