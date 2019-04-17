'''
this is a function where you can put in the picture name and the coordinates of a reference star, and it will crop a new shape using that star as a reference for the left-most side. 
'''
import numpy as np
import astropy.io.fits as pf
import matplotlib.pyplot as plt


#F606W_larger1 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_larger1.fits")
#F475W_turned4 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_turned4.fits")
#F814W1_larger1 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_larger1.fits")
#F814W2_larger1 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_larger1.fits")


#F606W_cropped = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_cropped.fits")
#F814W1_cropped = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_cropped.fits")
#F475W_cropped = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_cropped.fits")
#F814W2_cropped = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_cropped.fits")


#F475W_cut_corners = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_cut_corners.fits")
#F814W1_shifted = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_shifted.fits")
#F814W2_shifted = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_shifted.fits")
#F606W_shifted= pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_shifted.fits")

F475W_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_horizontal_final.fits")
F814W1_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_horizontal_final.fits")
F814W2_horizontal_final = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_horizontal_final.fits")
F606W_horizontal_final= pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal_final.fits")

F475W_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_horizontal.fits")
F814W1_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_horizontal.fits")
F814W2_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_horizontal.fits")
F606W_horizontal = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_horizontal.fits")

F475W_rotated2 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_rotated2.fits")
F814W1_rotated2 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_rotated2.fits")
F814W2_rotated2 = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_rotated2.fits")
F606W_rotated2= pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_rotated2.fits")



print " "

print "Greetings! This code has three seperate functions."
print "a.) To be applied to _larger1 to create _cropped, using a reference star you need to determine"
print "b.) To crop an arbitrary amount of pixels off the edges of the image"
#print "c.) To be applied when choosing the final dimensions of the disk"
print " "

option = raw_input("How will you apply this code? (a, b, c) : ")


if option == 'a':
    
    print " "
    print " "
    print "You will need to locate a star that is visible in all the images you wish to crop."
    print " "
    
    print "When you are ready, please type: cropapic( [filename_larger1/turned4] , starcoord x, starcoord y). **Note that the coordinates of the star will be specific to the filter you are using.** "
    


    def cropapic(pic, starcoordx, starcoordy):                             
      
        if pic == F606W_larger1:
            name = 'F606W'
        if pic == F814W1_larger1:
            name = 'F814W1'
        if pic == F475W_turned4:
            name = 'F475W'
        if pic == F814W2_larger1:
            name = 'F814W2'
        
        image  = pic[0].data
        
    
        print "The answers to the following questions you should repeat for every filter!"
        print " "
        d1 = raw_input("Distance, from the star to the leftmost edge of the new window: ")
        d2 = raw_input("Desired width of the entire new window: ")
        d3 = raw_input("Distance from the star to bottom edge of the new window: ")
        d4 = raw_input("Desired height of the entire new window: ")
    
        xstart = starcoordx - np.int(d1)
        xstop = xstart + np.int(d2)
        ystart = starcoordy - np.int(d3)
        ystop = ystart + np.int(d4)
        
        print " "
        print "Your new array will have the following dimensions:"
        
    
        print "xstart = ", xstart
        print "xstop = ", xstop
        print "ystart = ", ystart
        print "ystop = ", ystop
    
        print " "
        
        
        correct = raw_input("Ready to crop? (y/n) : ")
        if correct == 'y':
            
            print "Cropping Image..."
    
            new = image[ystart:ystop, xstart:xstop] 
            plt.imshow(new, origin='lower', vmin=-.2, vmax=.2)
            plt.colorbar()
            plt.show()
    
            print " "
            print "Saving file..."
            title = name + '_cropped.fits'
            pf.writeto(title, new) 
            print "Your file may have been saved!"
            
        if correct == 'n':
            print "Please edit your values to continue"
            return
    
    
    #for gbsj, the starcoords were: 
    #F606W & F814W1: 3360, 4525
    #F475W & F814W2: 1843, 1203
    #dimensions: 
    
    #for c2dj163131 the starcoords are: 
    #F606W & F814W1: 6850.7, 3040.7
    #F475W & 814W2: 3535.1, 3815.4
    #dimensions: 300 x 310
    
    #for 2massj1116 the starcoords are:
    #F606W & F814W1: 2903.6, 3724.4
    #F475W & 814W2: 3593.6, 1773.3
    #dimensions: 830 x 790
    
    #for 2massj1628 the starcoords are:
    #F110W: 380.84848852455394, 637.42744130363553
    #F160W: 379.24079824845921, 637.16766332963243
    #F205W: 
    #F475W: 3876, 3991 // 3874.8737005044427, 3990.4867347458539
    #F555W: 748.5, 960 // 748.04105425152363, 958.8917475049078
    #F814W1: 749, 961  // 747.39826819817858, 958.72119564589514
    #F814W2: 3877, 3991 // 3876.226466930425, 3991.1184646817701
    #F110, F160, F205 avg: 380, 638//  380.05, 637.3
    #F555, F814W1 avg:  749, 961 // 747.72, 958.8
    #F475, F814W2 avg:  3876, 3991  // 3875.6, 3990.8
    #dimensions: 620 x 680
    #cropping: 260, 300, 388, 230
    

    
#for hktau the starcoords are: 
        #F606W: 1956.3, 2397.8    using the picking function   1956.17, 2396.7                  // 1955.58236723, 2397.80278137
        #F475W: 3534.6, 3854.7    using the picking function    3534.43840794, 3854.72802481    //  3534.48290492, 3855.03497281
        #F814W1: 1957.6, 2392     using the picking function    1957.32459999, 2398.39123589    //  1957.34634113, 2398.88900431
        #F814W2: 3536, 3856.2     using the picking function     3534.80453523, 3855.55785442   //  3535.75773939, 3856.02555161
    #F606 & F814W1 avg: 1956.747299995 , 2397.5456179450002
    #F475 & F814W2 avg: 3534.621471585, 3855.142939614999
    #dimensions: 221 x 204
    #cropping: 111, 221, 114, 204
    
    
    
    #for HH30 the starcoords are:
    #F439W:
    #F555W1 : 2408.8, 2815.6
    #F675W1: 2408.7, 2814.6 
    #F814W1:  2409.5, 2814.5
    #F439W, F555W1, F675W1, F814W1 average: 2409.0, 2814.9
    #F555W2: 505.75, 735.08
    #F675W2: 506.25, 734.81
    #F814W2: 506.44, 735.34
    #F555W2, F675W2, F814W2 average: 506.15, 735.08
    #dimensions: (573, 597)
    #cropping: 403, 597, 466, 573
    
    
if option == 'b':
    print " "
    print "To run, type: cropapic(wavelength_extension)"
    
    def cropapic(pic):                             
      
        if pic == F606W_horizontal or pic == F606W_horizontal_final or pic == F606W_rotated2:
            name = 'F606W'
        elif pic == F814W1_horizontal  or pic == F814W1_horizontal_final or pic == F814W1_rotated2:
            name = 'F814W1'
        elif pic == F475W_horizontal or pic == F475W_horizontal_final or pic == F475W_rotated2:
            name = 'F475W'
        elif pic == F814W2_horizontal  or pic == F814W2_horizontal_final or pic == F814W2_rotated2 :
            name = 'F814W2'
        
        image  = pic[0].data
    
        xstart = np.int(raw_input("xstart: "))
        xstop = np.int(raw_input("xstop: "))
        ystart = np.int(raw_input("ystart: "))
        ystop = np.int(raw_input("ystop: "))
        
    
        correct = raw_input("Ready to crop? (y/n) : ")
        if correct == 'y':
            
            print "Cropping Image..."
    
            new = image[ystart:ystop, xstart:xstop] 
            plt.imshow(new, origin='lower', vmin=-.2, vmax=.2)
            plt.colorbar()
            plt.show()
    
            print " "

            extension = raw_input( "What extension is this? ")
            title = name + extension + '.fits'
            pf.writeto(title, new) 
            print " " 
            print "Your file may have been saved!"
    
    
if option == 'c':
    
    print " This code is unfinished, sorry" 
    
    #to be applied when choosing the final dimensions of the disk
    '''
    print "Please confirm that these cropping dimensions are correct"
    
    xstart = 460
    xstop = 870
    ystart = 580
    ystop = 900
    
    print "xstart = ", xstart
    print "xstop = ", xstop
    print "ystart = ", ystart
    print "ystop = ", ystop
    
    print "Cropping Image..."
    
    new = array[ystart:ystop, xstart:xstop] 
    plt.imshow(new, origin='lower', vmin=-.2, vmax=.2)
    plt.colorbar()
    plt.show()
    
    #to move from _horizontal to _cropped2
    print "Saving file..."
    title = pic + '_cropped2.fits'
    pf.writeto(title, m) #uncomment when want to save
    print "Your file may have been saved!"
    
    
    '''
    



    


        



