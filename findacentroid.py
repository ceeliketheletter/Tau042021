'''This looks like it was adapted from the top part of centroids.py, which was the original code. This code seems to just find the center of mass of a determined region, when an eye-balled estimate of a star's position has already been given. It does so by taking adding a pre-determined number of units above, below, left, and right of the point, cropping the image to this box, applying the center of mass function, then with this center of mass point, figuring out what the whole-picture equivilent of this point is.'''


import astropy.io.fits as pf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import ndimage
from math import asin, pi

#Load up fits files                                                                                                                                                                              

#load fits files                                                                                                                                                                                 
F606W_larger1 = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F606W_larger1.fits")
F475W_turned4 = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F475W_turned4.fits")
F814W1_larger1 = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F814W1_larger1.fits")
F814W2_larger1 = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F814W2_larger1.fits")

F606W_cropped = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F606W_cropped.fits")
F475W_cropped = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F475W_cropped.fits")
F814W1_cropped = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F814W1_cropped.fits")
F814W2_cropped = pf.open("/Users/CEE/Desktop/new_objects/2massj1116/F814W2_cropped.fits")

print "find the center of mass of a determined region, when an eye-balled estimate of a star's position has already been given."
print " "
print "To run, please type: centroid([wavelength_larger1], starcoordx, starcoordy, window radius)"

def centroid(pic, starcoordx, starcoordy, window):

     
     array = pic[0].data

                                                                                                                         
     lowy = starcoordy - window          
     highy = starcoordy + window
     lowx = starcoordx - window
     highx = starcoordx + window


     orig_coords = (starcoordx, starcoordy)
     #print 'Orig Coords :  ' , orig_coords
     #print 'Intensity :  ' , array[(orig_coords)]

     region = array[lowy:highy, lowx: highx] #takes in the coordinates, spits out an intensity                                                                                                   
     #print 'Shape of Region : ' , region.shape

     centroid5 = ndimage.center_of_mass(region) #finding xy cm of region, its a coordinate                                                                                                      \
     
                                                                                                                                                                                                                                                          
     #print 'Coordinates of centroid5 : ' , (centroid5[1], centroid5[0])  #listed as x,y for viewing purposes


     #print 'Intensity : ', region[(centroid5)] #this is the intensity at the centroid20 coordinate                                                                                               

     ycm_region = centroid5[0] #check to see if this is right
     xcm_region = centroid5[1]

     ycm_real = lowy + ycm_region
     xcm_real = lowx + xcm_region
     
     real_coords = (xcm_real, ycm_real)
     

     print 'Real Coordinates : ', real_coords
     #print 'Intensity : ', array[(real_coords)] #this is the intensity at the re-imposed centroid coordinate. it should be the same as before

     xdiff = window - centroid5[1] #trying to see if subtracting the difference in location from the orig starcoord would render a different answer. it didnt
     ydiff = window - centroid5[0]
     #print 'xdiff, ydiff : ', (xdiff, ydiff)

     realx = starcoordx - xdiff
     realy = starcoordy - ydiff
     real_coords2 = (realx, realy)
     
     #print 'Alternate Method of Real Coords :' , real_coords2 
     #print 'Intensity : ' , array[(real_coords2)]

     plt.imshow(array, origin='lower', vmin=-.2, vmax=1)
     plt.annotate('.  star', xy=(xcm_real, ycm_real), xytext = (xcm_real, ycm_real)) #writes text                                                                                               \
     plt.colorbar()
     plt.show()
     
'''     
     #trying to index a similar box around the real centroid coordinate and see how that compares to a graph of an indexed box around the orig starcoord
     xstart = realx - window - 1500
     xstop = realx + window + 1500
     ystart = realy - window - 1500
     ystop = realy + window + 1500

     box1 = array[ystart:ystop , xstart:xstop]
     plt.imshow(box1, origin='lower', vmin=-.2, vmax=1)
     plt.annotate('.  star', xy=(centroid5[1] + 1500, centroid5[0] + 1500), xytext = (centroid5[1] + 1500, centroid5[0] + 1500))
     plt.colorbar()
     plt.show()

     xstart = len(array[1])/2 -1500
     xstop = len(array[1])/2 + 1500
     ystart = len(array[0])/2 -1500
     ystop = len(array[0])/2 + 1500

     box2 = array[ystart:ystop , xstart:xstop]
     plt.imshow(box2, origin='lower', vmin=-.2, vmax=1)
     plt.annotate('.  star', xy=(centroid5[1] + 1500, centroid5[0] + 1500), xytext = (centroid5[1] + 1500, centroid5[0] + 1500))
     plt.colorbar()
     plt.show()
#honestly dont know what im doing here
'''
