'''
this is a function where you can put in the picture name and the coordinates of a reference star, and it will crop a 1526 x 1528 shape using that star as a reference for the left-most side. Note: does require previously imputted picture into the program, for loading and saving purposes
'''

import astropy.io.fits as pf
import matplotlib.pyplot as plt



F606W_cropped = pf.open("/Users/CEE/Desktop/cleaned/F606W_cropped.fits")
F814W1_cropped = pf.open("/Users/CEE/Desktop/cleaned/F814W1_cropped.fits")
F475W_cropped = pf.open("/Users/CEE/Desktop/cleaned/F475W_cropped.fits")
F814W2_cropped = pf.open("/Users/CEE/Desktop/cleaned/F814W2_cropped.fits")

F606W_larger1 = pf.open("/Users/CEE/Desktop/cleaned/F606W_larger1.fits")
F475W_turned = pf.open("/Users/CEE/Desktop/cleaned/F475W_turned.fits")
F814W1_larger1 = pf.open("/Users/CEE/Desktop/cleaned/F814W1_larger1.fits")
F814W2_larger1 = pf.open("/Users/CEE/Desktop/cleaned/F814W2_larger1.fits")
final_img_kp_larger1 = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_larger1.fits")
final_img_j_pad_larger1 = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_larger1.fits")



F475W_horizontal = pf.open("/Users/CEE/Desktop/cleaned/F475W_horizontal.fits")
F814W1_horizontal = pf.open("/Users/CEE/Desktop/cleaned/F814W1_horizontal.fits")
F814W2_horizontal = pf.open("/Users/CEE/Desktop/cleaned/F814W2_horizontal.fits")
F606W_horizontal = pf.open("/Users/CEE/Desktop/cleaned/F606W_horizontal.fits")
final_img_kp_horizontal = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_horizontal.fits")
final_img_j_pad_horizontal = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_horizontal.fits")



def cropapic(pic):            #, starcoordx, starcoordy):                             
    array  = pic[0].data
    
    
    '''
    #activate starcoords
    #to be applied to _larger1 to create _cropped, using ref star as the left in the triangle
    xstart = starcoordx - 410.8 #this is the distance, in keck, from the star to the leftmost
    xstop = xstart + 1526 #this is the distance from the leftmost to the rightmost
    ystart = starcoordy - 324.04 #distance from star to bottom of page
    ystop = ystart + 1528 #distance from bottom to top
    '''
    
    '''
    #to be applied to _cropped to create _cut_corners; 80px chopped off all sides
    ystart = 80
    ystop = 1446
    xstart = 80
    xstop = 1446
    '''
    
    
    #this is for a version where the pixels line up and you can choose single coordinates to apply to all
    #maybe just disk?
    xstart = 460
    xstop = 870
    ystart = 580
    ystop = 900
    
    
    new = array[ystart:ystop, xstart:xstop] 
    plt.imshow(new, origin='lower', vmin=-.2, vmax=.2)
    plt.colorbar()
    plt.show()








    if pic == F606W_cropped:
        pf.writeto('F606W_cut_corners.fits', new)
    if pic == F814W1_cropped:
        pf.writeto('F814W1_cut_corners.fits', new)
    if pic == F814W2_cropped:
        pf.writeto('F814W2_cut_corners.fits', new)
    if pic == F475W_cropped:
        pf.writeto('F475W_cut_corners.fits', new)
    if pic == final_img_kp_larger1:
        pf.writeto('final_img_kp_cut_corners.fits', new)
    if pic == final_img_j_pad_larger1:
        pf.writeto('final_img_j_pad_cut_corners.fits', new)
        
        
    if pic == F606W_horizontal:
        pf.writeto('F606W_cropped2.fits', new)
    if pic == F814W1_horizontal:
        pf.writeto('F814W1_cropped2.fits', new)
    if pic == F814W2_horizontal:
        pf.writeto('F814W2_cropped2.fits', new)
    if pic == F475W_horizontal:
        pf.writeto('F475W_cropped2.fits', new)
    if pic == final_img_kp_horizontal:
        pf.writeto('final_img_kp_cropped2.fits', new)
    if pic == final_img_j_pad_horizontal:
        pf.writeto('final_img_j_pad_cropped2.fits', new)

