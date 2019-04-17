'''This program will take a 10x10 region of space in an image, with user imput about the location, and take the median. The median will be subtracted from the intensity over the whole image. This will remove the background noise'''

import scipy 
import astropy.io.fits as pf
import numpy as np
import glob 

#import fits file

F606W = pf.open("/Users/CEE/Desktop/cleaned/F606W_cropped2.fits")
F814W1 = pf.open("/Users/CEE/Desktop/cleaned/F814W1_cropped2.fits")
F814W2 = pf.open("/Users/CEE/Desktop/cleaned/F814W2_cropped2.fits")
F475W = pf.open("/Users/CEE/Desktop/cleaned/F475W_cropped2.fits")
final_img_j_pad = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_cropped2.fits")
final_img_kp = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_cropped2.fits")

#make it all an array

F606W = np.array(F606W[0].data)
F475W =np.array(F475W[0].data)
F814W1 =np.array(F814W1[0].data)
F814W2 =np.array(F814W2[0].data)
final_img_j_pad =np.array(final_img_j_pad[0].data)
final_img_kp =np.array(final_img_kp[0].data)

files = [F606W, F475W, F814W1, final_img_kp, final_img_j_pad]

print "Open your chosen file in DS9, and choose a pixel with 10x10 distance around it, pretty close to the disk"


def noise(filename, xpix, ypix):

 if filename == 'F606W':
     image = F606W
     
 if filename == 'F475W':
     image = F475W
     
 if filename == 'F814W1':
     image = F814W1
     
 if filename == 'F814W2':
     image = F814W2
     
 if filename == 'final_img_kp':
     image = final_img_kp
     
 if filename == 'final_img_j_pad':
     image = final_img_j_pad
     

 #print "I'm sorry, but the code requires that you manually switch what object you want to manipulate right now. In the future, I will learn how a user input can refer to an array but until then..."

 



 ymin = int(ypix)-5
 ymax = int(ypix)+5
 xmin = int(xpix)-5
 xmax = int(xpix)+5



 region = image[ymin:ymax, xmin:xmax] #change filter name here!

 median = np.median(region)

 print 'The median of this 10x10 region is: ', median


 newfile = image - median #change filter name here!

 
 title = filename + '_lessnoise.fits' #change filter name here!

 pf.writeto(title, newfile)

 print "Your file has been saved!"
