'''
I want this program to take an average of the intensity along a 5px horizontal stretch and graph those intensity points vs position. Make overlaying plots for each wavelength, with the y axis is Jansky, and the x axis is in arcseconds
'''



import matplotlib.pyplot as plt
import astropy.io.fits as pf
import numpy as np
import pylab
from math import log
import scipy.ndimage.filters


F606W = pf.open("/Users/CEE/Desktop/cleaned/F606W_jansky.fits")
F814W1 = pf.open("/Users/CEE/Desktop/cleaned/F814W1_jansky.fits")
F814W2 = pf.open("/Users/CEE/Desktop/cleaned/F814W2_jansky.fits")
F475W = pf.open("/Users/CEE/Desktop/cleaned/F475W_jansky.fits")
final_img_kp = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_jansky.fits")
final_img_j_pad = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_jansky.fits")

F606W = F606W[0].data
F475W = F475W[0].data
F814W1 = F814W1[0].data
F814W2 = F814W2[0].data
final_img_kp = final_img_kp[0].data
final_img_j_pad = final_img_j_pad[0].data

imagelist = ['F606W', 'F475W', 'F814W1', 'F814W2', 'final_img_kp', 'final_img_j_pad']

fig = plt.figure()
ax = plt.gca()

#print "If you would like to look at intensity cuts along the x axis, type xavg( [refpix, window] ). For y axis, use yavg"

print "To run, type avg( [refpix] , [window] , [axis (can be x or y) ])"

def avg(refpix, window, axis):  
    F606W_avg =[]
    F475W_avg = []
    F814W1_avg = []
    F814W2_avg = []
    final_img_j_pad_avg = []
    final_img_kp_avg = []


    half  = window/2
    xstart = refpix - half
    xstop = refpix + half

    pixscale_475 = 0.03962306984   #arcseconds
    sq_arcseconds = (pixscale_475)**2
    
    if axis == 'x':
                    
        for i in range(len(F606W)):
            avglen = F606W[xstart:xstop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1 * sq_arcseconds
            F606W_avg.append(avg)

        for i in range(len(F475W)):

            avglen = F475W[xstart:xstop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1 * sq_arcseconds
            F475W_avg.append(avg)


        for i in range(len(F814W1)):

            avglen = F814W1[xstart:xstop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1 * sq_arcseconds
            F814W1_avg.append(avg)
            
        for i in range(len(F814W2)):

            avglen = F814W2[xstart:xstop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1 * sq_arcseconds
            F814W2_avg.append(avg)

        for i in range(len(final_img_kp)):

            avglen = final_img_kp[xstart:xstop, i:i+1]
            
            add = sum(avglen)
            avg1 = add/float(len(avglen))
	    avg = avg1 * sq_arcseconds
            final_img_kp_avg.append(avg)
            
        for i in range(len(final_img_j_pad)):

            avglen = final_img_j_pad[xstart:xstop, i:i+1]
            add = sum(avglen)
            avg1 = add/float(len(avglen))
	    avg = avg1 * sq_arcseconds
            final_img_j_pad_avg.append(avg)
            
            
    ystart = refpix - half
    ystop = refpix + half 
          
    if axis == 'y':        
        for i in range(len(F606W[1])):
        
            avglen = F606W[ i:i+1 , ystart:ystop]
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1 * sq_arcseconds
            F606W_avg.append(avg)

        for i in range(len(F475W[1])):
  
            avglen = F475W[i:i+1 , ystart:ystop]
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1 * sq_arcseconds
            F475W_avg.append(avg)


        for i in range(len(F814W1[1])):

            avglen = F814W1[i:i+1 , ystart:ystop]
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1 * sq_arcseconds
            F814W1_avg.append(avg)
            
        for i in range(len(F814W2[1])):

            avglen = F814W2[i:i+1 , ystart:ystop]
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1 * sq_arcseconds
            F814W2_avg.append(avg)

        for i in range(len(final_img_kp[1])):

            avglen = final_img_kp[i:i+1 , ystart:ystop]
            add = np.sum(avglen)
            avg1 = add/float(len(avglen))
	    avg = avg1 * sq_arcseconds
            final_img_kp_avg.append(avg)
            
        for i in range(len(final_img_j_pad[1])):

            avglen = final_img_j_pad[i:i+1 , ystart:ystop]
            add = np.sum(avglen)
            avg1 = add/float(len(avglen))
	    avg = avg1 * sq_arcseconds
            final_img_j_pad_avg.append(avg)
          
    F606W_avg = scipy.ndimage.filters.median_filter(F606W_avg,3)
    F475W_avg = scipy.ndimage.filters.median_filter(F475W_avg,3)
    F814W1_avg = scipy.ndimage.filters.median_filter(F814W1_avg,3)
    F814W2_avg = scipy.ndimage.filters.median_filter(F814W2_avg,3)
    final_img_j_pad_avg= scipy.ndimage.filters.median_filter(final_img_j_pad_avg,3)
    final_img_kp_avg = scipy.ndimage.filters.median_filter(final_img_kp_avg,3)
    
    
   
    graph = raw_input("Which plot would you like to graph? 1. Normalized or 2. Raw Data ? ")
    if graph == '1':
        normal(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg, final_img_kp_avg, final_img_j_pad_avg, refpix, window, axis)
    elif graph == '2':
        plot(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg, final_img_kp_avg, final_img_j_pad_avg, refpix, window, axis)
        
def normal(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg, final_img_kp_avg, final_img_j_pad_avg, refpix, window, axis):

           F606W_avg = F606W_avg/np.amax(F606W_avg)
           F475W_avg = F475W_avg/np.amax(F475W_avg)
           F814W1_avg = F814W1_avg/np.amax(F814W1_avg) 
           F814W2_avg = F814W2_avg/np.amax(F814W2_avg) 
           final_img_kp_avg = final_img_kp_avg/np.amax(final_img_kp_avg) 
           final_img_j_pad_avg = final_img_j_pad_avg/np.amax(final_img_j_pad_avg)     
               
           pixscale_475 = 0.03962306984   #arcseconds
           

           
           x = np.arange(len(F606W_avg)) * pixscale_475  -7 
           
           
           pylab.plot(x, final_img_kp_avg, 'r', label = "K' ")           
           #pylab.plot(x, final_img_j_pad_avg, 'm', label = 'J')
           pylab.plot(x, F814W1_avg, 'y', label = 'F814W')  
           #pylab.plot(x, F814W2_avg, 'k', label = 'F814W2') 
           pylab.plot(x, F606W_avg, 'c', label = 'F606W')
           pylab.plot(x, F475W_avg, 'b', label = 'F475W')
                                                                     
                                                         
          
           #plt.yscale('log')
          
	  
	   plt.xlabel('Distance From Midplane (arcseconds)')
	   plt.ylabel('Normalized Surface Brightness ')
	   plt.axis([-2.75, 2.75, 0, 1.05])

	   handles, labels = ax.get_legend_handles_labels()  #legend
	   plt.legend(handles, labels, loc=1) 

	   plt.show()  
      
           save = raw_input("Save image? ")
	   if save == 'y':
	       fig.savefig('final_plot_' + str(refpix) + '_' + str(window)+'.jpg')  #saving  
               print "Your file may have been saved!"
               
def plot(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg, final_img_kp_avg, final_img_j_pad_avg, refpix, window, axis):
           

           pixscale_475 = 0.03962306984   #arcseconds
           

           
           x = np.arange(len(F606W_avg)) * pixscale_475
           
           
           pylab.plot(x, final_img_kp_avg, 'r', label = 'final_img_kp')           
           pylab.plot(x, final_img_j_pad_avg, 'm', label = 'final_img_j_pad')
           pylab.plot(x, F814W1_avg, 'y', label = 'F814W1')  
           pylab.plot(x, F814W2_avg, 'k', label = 'F814W2') 
           pylab.plot(x, F606W_avg, 'c', label = 'F606W')
           pylab.plot(x, F475W_avg, 'b', label = 'F475W')
                                                                     
                                                         
          
           plt.yscale('log')
          
	   title = "Intensity Cuts Along  '" + axis + "'  Axis of Disk \n Reference Pixel: " + str(refpix) + ' Window size: ' + str(window)

	   plt.title(title)
	   plt.xlabel('Position along Disk [arcseconds]')
	   plt.ylabel('Log of Intensity   [Jansky/arcseconds^2]')
	   

	   handles, labels = ax.get_legend_handles_labels()  #legend
	   plt.legend(handles, labels, loc=4) 

	   plt.show()  
	   
	   save = raw_input("Save image? ")
	   if save == 'y':
	       fig.savefig('final_plot_' + str(refpix) + '_' + str(window)+'.jpg')  #saving  
               print "Your file may have been saved!"