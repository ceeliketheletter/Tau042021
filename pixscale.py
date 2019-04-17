import astropy.io.fits as pf
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage



#F606W_turned = pf.open("/Users/CEE/Desktop/research/F606W_turned.fits")
#F814W1_turned = pf.open("/Users/CEE/Desktop/research/F814W1_turned.fits")
#F475W_turned = pf.open("/Users/CEE/Desktop/cleaned/F475W_turned.fits")


#final_img_j_pad = pf.open("/Users/CEE/Desktop/research/final_img_j_pad.fits")
#final_img_kp = pf.open("/Users/CEE/Desktop/research/final_img_kp.fits")


#F606W = np.array(F606W_turned[0].data)
#F475W = np.array(F475W_turned[0].data)
#F814W1 = np.array(F814W1_turned[0].data)

#final_img_kp = np.array(final_img_kp[0].data)
#final_img_j_pad = np.array(final_img_j_pad[0].data)


def scale(pic):
 
 #scaling factor = sqrt((CD1_1)^2+ (CD2_1)^2) * 3600 
 pixscale_475 = 0.03962306984   #arcseconds
 pixscale_606_8141 = 0.04999968396  #arcseconds    covers a larger area of sky, thus fewer pixels
 pixscale_keck = 0.039686
 pixscale_8242 = 0.03962366107
 
 '''
 if pic == 'F606W':
    pixscale_ratio = pixscale_606_8141/(float(pixscale_475))
 if pic == 'F814W1':
    pixscale_ratio = pixscale_606_8141/(float(pixscale_475))
 '''
 #if pic == 'F814W2':
 pixscale_ratio = pixscale_8242/(float(pixscale_475)) 
 whole = pf.open("/Users/CEE/Desktop/cleaned/" + pic + "_turned.fits")
 image = np.array(whole[0].data)
 '''
 if pic == 'F475W':
     print "Does not apply!"
     return
 if pic == 'final_img_j_pad':   
     pixscale_ratio = pixscale_keck/(float(pixscale_475))
 if pic == 'final_img_kp':   
     pixscale_ratio = pixscale_keck/(float(pixscale_475))
 else:
     print "Something went wrong!"
     return
 '''




 m = scipy.ndimage.interpolation.zoom(image, pixscale_ratio, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

 '''

 F606W_larger = scipy.ndimage.interpolation.zoom(F606W, (width_ratio, len_ratio), output=None, order=3, mode='constant', cval=0.0, prefilter=True) #scales 606x by the width ratio, scales y by len ratio #i think this means that pixels would no longer be square?  

 F606W_larger2 = scipy.ndimage.interpolation.zoom(F606W, width_ratio, output=None, order=3, mode='constant', cval=0.0, prefilter=True) # scales 606 by width ratio

 F606W_larger3 = scipy.ndimage.interpolation.zoom(F606W, (pixscale_ratio - 1), output=None, order=3, mode='constant', cval=0.0, prefilter=True)
 #this one is gonna be scaled by .26188314438, which is the ratio -1 , since the ratio is 79% but that means we only have 20% more to go, so we should be subtracting by something
 #what about pixscale_606 - pixscale_475 / pixscale_475? noooo thats the same
 #but what about pixscale_606 - pixscale_475 / pixscale_606? the 606 in the denom will cancel to have a final unit that is in terms of 475... but we are also working with a num <1
 '''

 plt.imshow(m, origin = 'lower', vmin=-74, vmax=545)
 plt.colorbar()
 plt.show()

 print m.shape
 
 title = pic + '_larger1.fits'
 pf.writeto(title, m) #uncomment when want to save





'''
IGNORE THIS MESS OF SADNESS

def dimensions(b, a):

    m = a.shape[0] #width of 475 array                                                            
    M = b.shape[0]
    array_ratio = float(m)/float(M)  

    new_width = array_ratio * b.shape[0]  
    new_height = array_ratio * b.shape[1]

    makelarger(new_width, new_height)

def makelarger():
    
    newshape = F606W.resize(6012, 6019)
    return newshape
    #plt.imshow(newshape)
    #plt.show()



def rebin( a, newshape):
            
            #Rebin an array to a new shape.
            
            
            assert len(a.shape) == len(newshape)
    
            slices = [ slice(0,old, float(old)/new) for old,new in zip(a.shape,newshape) ]
            coordinates = mgrid[slices]
            indices = coordinates.astype('i')   #choose the biggest smaller integer index
            return a[tuple(indices)]



m = F475W.shape[0] #width of 475 array
M = F606W.shape[0]

pixscale_ratio = pixscale_475/pixscale_606  #small pixel dimensions over large pix dim
array_ratio = float(m)/float(M)             #large array size over small arr size
print pixscale_ratio, array_ratio


new_array = array_ratio * F606W
print len(new_array)
print len(F606W)
print len(F475W)






#one method

def rebin_avg(a, b0):
    # NOTE: does not swap dimensions for IDL/Py style
    rebin ndarray data into a smaller ndarray of the same rank whose dimensions
    are factors of the original dimensions. eg. An array with 6 columns and 4 rows
    can be reduced to have 6,3,2 or 1 columns and 4,2 or 1 rows.
    example usages:
    >>> a=rand(6,4); b=rebin(a,3,2)
    >>> a=rand(6); b=rebin(a,2)



    # swap axes order to allow IDL convention in the newshape0 argument
    newshape = b0[::-1].shape
    

    shape = a.shape
    lenShape = len(shape)
    factor = np.asarray(shape)/np.asarray(newshape)
    evList = ['a.reshape('] + \
             ['newshape[%d],factor[%d],'%(i,i) for i in range(lenShape)] + \
             [')'] + ['.sum(%d)'%(i+1) for i in range(lenShape)] + \
             ['/factor[%d]'%i for i in range(lenShape)]
    print ''.join(evList)
    return eval(''.join(evList))



#another method
 
def rebin(a, b):

    M, N = a.shape
    m, n = b.shape

    print M, N, m, n
    if m<M: #making smaller

      new = a.reshape((m,M/m,n,N/n)).mean(3).mean(1)
      print new
        
      pf.writeto('check_this.fits', new)
      plt.imshow(m, origin='lower', vmin=-.2, vmax=1)
                                                                               
                                                                                
      plt.colorbar()
      plt.show()

    else: #making larger
  #      return np.repeat(np.repeat(a, m/M, axis=0), n/N, axis=1)




#len(F606W_turned[0].data)
#F606W_turned[0].header["NAXIS1"] instead ive been using F606.data[0].shape[0]

#a = np.arange(______).reshape(5575, 5560)







#another method
def congrid(a, newdims, method='linear', centre=False, minusone=False):
    Arbitrary resampling of source array to new dimension sizes.
    Currently only supports maintaining the same number of dimensions.
    To use 1-D arrays, first promote them to shape (x,1).
    
    Uses the same parameters and creates the same co-ordinate lookup points
    as IDL''s congrid routine, which apparently originally came from a VAX/VMS
    routine of the same name.
    method:
    neighbour - closest value from original data
    nearest and linear - uses n x 1-D interpolations using
                         scipy.interpolate.interp1d
    (see Numerical Recipes for validity of use of n 1-D interpolations)
    spline - uses ndimage.map_coordinates
    centre:
    True - interpolation points are at the centres of the bins
    False - points are at the front edge of the bin
    minusone:
    For example- inarray.shape = (i,j) & new dimensions = (x,y)
    False - inarray is resampled by factors of (i/x) * (j/y)
    True - inarray is resampled by(i-1)/(x-1) * (j-1)/(y-1)
    This prevents extrapolation one element beyond bounds of input array.
    
    if not a.dtype in [np.float64, np.float32]:
        a = np.cast[float](a)

    m1 = np.cast[int](minusone)
    ofs = np.cast[int](centre) * 0.5
    old = np.array( a.shape )
    ndims = len( a.shape )
    if len( newdims ) != ndims:
        print "[congrid] dimensions error. " \
              "This routine currently only support " \
              "rebinning to the same number of dimensions."
        return None
    newdims = np.asarray( newdims, dtype=float )
    dimlist = []

    if method == 'neighbour':
        for i in range( ndims ):
            base = np.indices(newdims)[i]
            dimlist.append( (old[i] - m1) / (newdims[i] - m1) \
                            * (base + ofs) - ofs )
        cd = np.array( dimlist ).round().astype(int)
        newa = a[list( cd )]
        return newa

    elif method in ['nearest','linear']:
        # calculate new dims
        for i in range( ndims ):
            base = np.arange( newdims[i] )
            dimlist.append( (old[i] - m1) / (newdims[i] - m1) \
                            * (base + ofs) - ofs )
        # specify old dims
        olddims = [np.arange(i, dtype = np.float) for i in list( a.shape )]

        # first interpolation - for ndims = any
        mint = scipy.interpolate.interp1d( olddims[-1], a, kind=method )
        newa = mint( dimlist[-1] )

        trorder = [ndims - 1] + range( ndims - 1 )
        for i in range( ndims - 2, -1, -1 ):
            newa = newa.transpose( trorder )

            mint = scipy.interpolate.interp1d( olddims[i], newa, kind=method )
            newa = mint( dimlist[i] )

        if ndims > 1:
            # need one more transpose to return to original dimensions
            newa = newa.transpose( trorder )

        return newa
    elif method in ['spline']:
        oslices = [ slice(0,j) for j in old ]
        oldcoords = np.ogrid[oslices]
        nslices = [ slice(0,j) for j in list(newdims) ]
        newcoords = np.mgrid[nslices]

        newcoords_dims = range(numpy.rank(newcoords))
        #make first index last
        newcoords_dims.append(newcoords_dims.pop(0))
        newcoords_tr = newcoords.transpose(newcoords_dims)
        # makes a view that affects newcoords

        newcoords_tr += ofs

        deltas = (np.asarray(old) - m1) / (newdims - m1)
        newcoords_tr *= deltas

        newcoords_tr -= ofs

        newa = scipy.ndimage.map_coordinates(a, newcoords)
        return newa
    else:
        print "Congrid error: Unrecognized interpolation type.\n", \
              "Currently only \'neighbour\', \'nearest\',\'linear\',", \
              "and \'spline\' are supported."
        return None





'''

