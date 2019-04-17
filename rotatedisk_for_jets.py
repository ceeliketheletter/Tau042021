'''                                                                            
this function takes points along the disk, creates a line, determines angle from horizontal, and rotates the image that much.                                 '''


from scipy import stats
import numpy as np
import pylab
import matplotlib.pyplot as plt
import astropy.io.fits as pf
from math import  asin
from scipy import ndimage
from math import atan


F475W = pf.open("/Users/CEE/Desktop/cleaned/F475W_cut_corners.fits") 
F606W = pf.open("/Users/CEE/Desktop/cleaned/F606W_shifted.fits")
F814W1 = pf.open("/Users/CEE/Desktop/cleaned/F814W1_shifted.fits")
F814W2 = pf.open("/Users/CEE/Desktop/cleaned/F814W2_shifted.fits")
final_img_kp = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_shifted.fits")
final_img_j_pad = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_shifted.fits")




'''
def main(pic):
    pic = pic[0].data

    xcoords = []
    ycoords = []

    going = raw_input('Would you like to proceed? y/n ')
    while going == 'y':
    
        userimput =  raw_input('X coordinate: ')
        x_coord1 = userimput
        userimput = raw_input('Y coordinate: ')
        y_coord1 = userimput
        going = raw_input('Would you like to proceed? y/n ')
        xcoords.append(float(x_coord1))
        ycoords.append(float(y_coord1))
 
    points(xcoords, ycoords, pic)

def points(xcoords, ycoords, pic):
# Fit the model
 x = np.array(xcoords)

 y = np.array(ycoords)

 print 'x_points: ', x 
 print 'y_points: ', y

 slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
# Calculate some additional outputs
 predict_y = intercept + slope * x
 print 'm = ', slope, 'b = ' , intercept 
 pred_error = y - predict_y
 degrees_of_freedom = len(x) - 2
 residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
 pylab.plot(x, y, 'o')
 pylab.plot(x, predict_y, 'k-')
 pylab.show()

#yay all of the above works for sure!


#okay so we found that m =  -0.279505177009 b =  1027.91905928
 print 'y = ', slope,'x + ', intercept

 x = np.linspace(550.,900., 200)
 y = slope*x + intercept

 plt.imshow(pic, origin='lower', vmin=0, vmax=.5)
 plt.colorbar()
 plt.plot(x, y,  label=" y = -0.279505177009x + 1027.91905928 ", linestyle = '-', linewidth=4, color = 'k')
 plt.plot(x, y, linestyle = '-', linewidth=1, color = 'r')
 plt.show()


#recall tan(angle) = slope
 angle = atan(slope)
 print 'angle: ',angle, 'radians'
 degrees =  angle *  57.2957795 
 print degrees, 'degrees'
 
 apply(pic, degrees)
'''


def apply(pic, degrees):
 #degrees = -18.1650246487 # from before -16.2446900838 from before -15.615952957 
 #where pic needs to be pic = F--W[0].data 
 array = pic[0].data
  
 m = ndimage.interpolation.rotate(array, degrees, axes=(1,0), reshape=False, output=None,  order=3, mode='constant', cval=0.0, prefilter=True)

 plt.imshow(m, origin='lower', vmin=-0, vmax=.5) 
 plt.colorbar()
 plt.show()                                                                                         

            


 if pic == F606W:
    image = 'F606W'
 elif pic == F814W1:
    image = 'F814W1'
 elif pic == F814W2:
    image = 'F814W2'
 elif pic == F475W:
     image = 'F475W'
 elif pic == final_img_j_pad:
    image = 'final_img_j_pad'
 elif pic == final_img_kp:
    image = 'final_img_kp'
        
        
 title = image + '_horizontal.fits'            
 pf.writeto(title, m)



