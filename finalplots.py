'''
I want this program to take an average of the intensity along a 5px horizontal stretch and graph those intensity points vs position. Make overlaying plots for each wavelength, with the y axis is Jansky, and the x axis is in arcseconds
'''


from astropy.convolution import convolve, Box1DKernel
import matplotlib.pyplot as plt
import astropy.io.fits as pf
import numpy as np
import pylab
from math import log
import scipy

F606W_jansky = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F606W_jansky.fits")
F475W_jansky = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F475W_jansky.fits")
F814W1_jansky = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W1_jansky.fits")
F814W2_jansky = pf.open("/Users/CEE/Desktop/new_objects/tau042021/F814W2_jansky.fits")

F606W = F606W_jansky[0].data
F475W = F475W_jansky[0].data
F814W1 = F814W1_jansky[0].data
F814W2 = F814W2_jansky[0].data

fig = plt.figure()
ax = plt.gca()


#print "If you would like to look at intensity cuts along the x axis, type xavg( [refpix, window] ). For y axis, use yavg"

print "To run, type avg( [refpix] , [window] , ['axis'])"

def avg(refpix, window, axis):  
    F606W_avg =[]
    F475W_avg = []
    F814W1_avg = []
    F814W2_avg = []



    half  = window/2
    ystart = refpix - half
    ystop = refpix + half

    
    if axis == 'x':
        diskstart = np.int(raw_input("Left endpoint of disk: "))
        diskstop = np.int(raw_input("Right endpoint of disk: "))
        
        for i in range(diskstart,diskstop):
            avglen = F606W[ystart:ystop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1
            F606W_avg.append(avg)

        for i in range(diskstart,diskstop):

            avglen = F475W[ystart:ystop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1
            F475W_avg.append(avg)


        for i in range(diskstart,diskstop):

            avglen = F814W1[ystart:ystop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1
            F814W1_avg.append(avg)
            
        for i in range(diskstart,diskstop):

            avglen = F814W2[ystart:ystop, i:i+1]
            add = sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1
            F814W2_avg.append(avg)


            
    xstart = refpix - half
    xstop = refpix + half 
          
    if axis == 'y':        
        diskbottom = np.int(raw_input("Bottom pixel of the disk/jet: "))
        disktop = np.int(raw_input("Top pixel of the disk/jet: "))
        
        for i in range(diskbottom,disktop):
        
            avglen = F606W[ i:i+1 , xstart:xstop] #y , x
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1
            F606W_avg.append(avg)

        for i in range(diskbottom,disktop):
  
            avglen = F475W[i:i+1 , xstart:xstop]
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
	    avg = avg1
            F475W_avg.append(avg)


        for i in range(diskbottom,disktop):

            avglen = F814W1[i:i+1 , xstart:xstop]
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1
            F814W1_avg.append(avg)
            
        for i in range(diskbottom,disktop):

            avglen = F814W2[i:i+1 , xstart:xstop]
            add = np.sum(avglen)
            avg1 = (add/float(len(avglen)))
 	    avg = avg1
            F814W2_avg.append(avg)


    box_kernel = Box1DKernel(3)
    F606W_avg = convolve(F606W_avg, box_kernel)
    F475W_avg = convolve(F475W_avg, box_kernel)
    F814W1_avg = convolve(F814W1_avg, box_kernel)
    F814W2_avg = convolve(F814W2_avg, box_kernel)
    
    
   
    graph = raw_input("Which plot would you like to graph? 1. Normalized or 2. Raw Data ? ")
    if graph == '1':
        normal(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg, refpix, window, axis)
    elif graph == '2':
        plot(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg, refpix, window, axis)
        
	

def normal(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg, refpix, window, axis):

           F606W_avg = F606W_avg/np.amax(F606W_avg)
           F475W_avg = F475W_avg/np.amax(F475W_avg)
           F814W1_avg = F814W1_avg/np.amax(F814W1_avg) 
           F814W2_avg = F814W2_avg/np.amax(F814W2_avg) 
           
           print np.amax(F606W_avg)
           print np.amax(F475W_avg)
           print np.amax(F814W1_avg) 
           print np.amax(F814W2_avg) 
   
               
           pixscale_475 = 0.03962306984   #arcseconds
           
           #locate the y position for the peak of each wavelength
           y_peak_606 = np.argmax(F606W_avg)
           y_peak_475 = np.argmax(F475W_avg)
           y_peak_814W1 = np.argmax(F814W1_avg)
           y_peak_814W2 = np.argmax(F814W2_avg)
           
           x = np.arange(len(F606W_avg)) * pixscale_475  
           
                     
           #locate the x position of the peak for each wavelength
           x_peak_606 = x[y_peak_606]
           x_peak_475 = x[y_peak_475]
           x_peak_814W1 = x[y_peak_814W1]
           x_peak_814W2 = x[y_peak_814W2]
        
           #this uses the x position of the peaks of each wavelength to subtract from the total array, setting each peak postion to zero

           pylab.plot(x - x_peak_475, F475W_avg, 'b', label = 'F475W') 
           #pylab.plot(x - x_peak_814W2, F814W2_avg, 'y', label = 'F814W2') 
           
           if refpix == 773:                                     
                pylab.plot(x - x_peak_606+ 1.783, F606W_avg, 'g', label = 'F606W')
                pylab.plot(x - x_peak_814W1+ 1.5056, F814W1_avg, 'r', label = 'F814W')                                         
                
           else:
                pylab.plot(x - x_peak_606, F606W_avg, 'g', label = 'F606W')
                pylab.plot(x - x_peak_814W1, F814W1_avg, 'r', label = 'F814W')                                         
                
           
           
           #plt.yscale('log')
           print " " 
           direction = raw_input("Left or Right? ")
           fraction = raw_input("1/3 or 2/3? ")
           if axis == 'x':
               diskslice = 'Horizontal slice'
           elif axis =='y':
               diskslice = 'Vertical slice'
	   plt.title(direction + ' ' +  fraction + ' ' + "of Disk " + '(' + str(refpix) + ')'  + ' ' + diskslice + '. ' + 'Window size:' + str(window) )
	   plt.xlabel('Distance From Midplane (arcseconds)')
	   plt.ylabel('Normalized Surface Brightness ')
	   plt.axis([-3.25, 4, -0.05, 1.05])

	   handles, labels = ax.get_legend_handles_labels()  #legend
	   plt.legend(handles, labels, loc=1) 

	   plt.show()  
      
           save = raw_input("Save image? ")
	   if save == 'y':
	       fig.savefig('normalized_final_plot_' + str(refpix) + '_' + str(window)+'.jpg')  #saving  
               print "Your file may have been saved!"
        


   
def plot(F606W_avg, F475W_avg, F814W1_avg, F814W2_avg,  refpix, window, axis):
           #locate the y position for the peak of each wavelength
           y_peak_606 = np.argmax(F606W_avg)
           y_peak_475 = np.argmax(F475W_avg)
           y_peak_814W1 = np.argmax(F814W1_avg)
           y_peak_814W2 = np.argmax(F814W2_avg)

           pixscale_475 = 0.03962306984   #arcseconds
           
           x = np.arange(len(F606W_avg)) * pixscale_475 
           
        
           #locate the x position of the peak for each wavelength
           x_peak_606 = x[y_peak_606]
           x_peak_475 = x[y_peak_475]
           x_peak_814W1 = x[y_peak_814W1]
           x_peak_814W2 = x[y_peak_814W2]
                     
           #this uses the x position of the peaks of each wavelength to subtract from the total array, setting each peak postion to zero

           pylab.plot(x - x_peak_475, F475W_avg, 'b', label = 'F475W') 
 
           pylab.plot(x - x_peak_814W2, F814W2_avg, 'y', label = 'F814W2')
                                                                     
           if refpix == 773:                                     
                pylab.plot(x - x_peak_814W1+ 1.5056, F814W1_avg, 'r', label = 'F814W')                                         
                pylab.plot(x - x_peak_606+ 1.783, F606W_avg, 'g', label = 'F606W')
           else:
                pylab.plot(x - x_peak_814W1, F814W1_avg, 'r', label = 'F814W')                                         
                pylab.plot(x - x_peak_606, F606W_avg, 'g', label = 'F606W')
                                                         
          
           plt.yscale('log')
           
           print " " 
           direction = raw_input("Left or Right? ")
           fraction = raw_input("1/3 or 2/3? ")
           if axis == 'x':
               diskslice = 'Horizontal slice'
           elif axis =='y':
               diskslice = 'Vertical slice'
	   plt.title(direction + ' ' +  fraction + ' ' + "of Disk " + '(' + str(refpix) + ')'  + ' ' + diskslice + '. ' + 'Window size:' + str(window) )
	   
	   plt.xlabel('Position along Disk [arcseconds]')
	   plt.ylabel('Log of Intensity   [Jansky/pixel]')
	   

	   handles, labels = ax.get_legend_handles_labels()  #legend
	   plt.legend(handles, labels, loc=4) 

	   plt.show()  
	   
	   
	   save = raw_input("Save image? ")
	   if save == 'y':
	       fig.savefig('raw_final_plot_' + str(refpix) + '_' + str(window)+'.jpg')  #saving  
               print "Your file may have been saved!"