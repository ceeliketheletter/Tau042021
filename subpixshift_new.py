

'''
This code takes your picture name, and how much you want to shift in x, and in y. It will automatically plot it for you, but you must uncomment and rename the file in order to save.
'''



import numpy as np
import astropy.io.fits as pf
import matplotlib.pyplot as plt



F606W = pf.open("/Users/CEE/Desktop/cleaned/F606W_cut_corners.fits")
F814W1 = pf.open("/Users/CEE/Desktop/cleaned/F814W1_cut_corners.fits")
F814W2 = pf.open("/Users/CEE/Desktop/cleaned/F814W2_cut_corners.fits")
F475W = pf.open("/Users/CEE/Desktop/cleaned/F475W_cut_corners.fits")
final_img_kp = pf.open("/Users/CEE/Desktop/cleaned/final_img_kp_cut_corners.fits")
final_img_j_pad = pf.open("/Users/CEE/Desktop/cleaned/final_img_j_pad_cut_corners.fits")




def shift(pic, phase=0, nthreads=1):          

    data = pic[0].data
    
    
    #Find the center of the left triangle star for each image, insert here
    jp_x = 328.777
    jp_y = 243.75
    
    kp_x = 330.927
    kp_y = 244.287
    
    x_606 = 330.927
    y_606 = 245.362
    
    x_8141 = 331.464
    y_8141 = 244.824
    
    x_8142 = 330.927
    y_8142 = 243.212
    
    x_475 = 331.464
    y_475 = 244.824
    
    
    #This part takes the difference between centers of different images and 475 to conduct the shift so all the centers align to the 475 center
    
    if pic == F606W:
        deltax = x_475 - x_606
        deltay = y_475 - y_606
    elif pic == F814W1:
        deltax = (x_475 - x_8141)
        deltay = (y_475 - y_8141)
    elif pic == F814W2:
        deltax = (x_475 - x_8142)
        deltay = (y_475 - y_8142)
    elif pic == final_img_kp:
        deltax = (x_475 - kp_x)
        deltay = (y_475 - kp_y)
    elif pic == final_img_j_pad:
        deltax = (x_475 - jp_x)
        deltay = (y_475 - jp_y)
    elif pic == F475W:
        print "This is the reference!"
        return
     
    
    
    """
    FFT-based sub-pixel image shift
    http://www.mathworks.com/matlabcentral/fileexchange/18401-efficient-subpixel-image-registration-by-cross-correlation/content/html/efficient_subpixel_registration.html

    Will turn NaNs into zeros
    """

    fftn = np.fft.fftn
    ifftn = np.fft.ifftn
    if np.any(np.isnan(data)):
        data = np.nan_to_num(data)
    ny,nx = data.shape
    Nx = np.fft.ifftshift(np.linspace(-np.fix(nx/2),np.ceil(nx/2)-1,nx))
    Ny = np.fft.ifftshift(np.linspace(-np.fix(ny/2),np.ceil(ny/2)-1,ny))
    Nx,Ny = np.meshgrid(Nx,Ny)
    gg = ifftn( fftn(data)* np.exp(1j*2*np.pi*(-deltax*Nx/nx-deltay*Ny/ny)) * np.exp(-1j*phase) )
    new = abs(gg)
    plt.imshow(new, origin = 'lower', vmin = 0, vmax = .5)

    plt.show()


  
    #pf.writeto('F606W_shifted.fits', new)
  





# IDK why it hated me for trying to do this part. Well, have fun manually switching the file name every time you run this!

    if pic == F606W:
        pf.writeto('F606W_shifted.fits', new)
    elif pic == F814W1:
        pf.writeto('F814W1_shifted.fits', new)
    elif pic == F814W2:
        pf.writeto('F814W2_shifted.fits', new)
    #elif pic == F475W:
    #    pf.writeto('F475W_shifted.fits', new)
    elif pic == final_img_j_pad:
        pf.writeto('final_img_j_pad_shifted.fits', new)
    elif pic == final_img_kp:
        pf.writeto('final_img_kp_shifted.fits', new)
