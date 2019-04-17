
#create a table of values

import numpy as np
from astropy.io.votable import parse
from astropy.table import Table

votable = parse(input('Enter .vot filename (in quotations): '))   #ex: "vizier_hvtauc.vot"

for table in votable.iter_tables():   #view table as listed in the vot file
    table= table

data = table.array    #convert the large table into an array

#create a new table with only the columns we want
    
a =  data['sed_freq']    #frequency in GHz
flux =  data['sed_flux']
c = data['sed_eflux']    #flux error
telescope = data['sed_filter']
source = data['_tabname']

#convert frequency from GHz to micron
freq =  1e-3 *  299792458.0 / a  

#convert flux error to a percent of flux
c1 = np.ma.filled(c, 0.0)  #first zero the masked '--' elements from array
error = c1/flux * 100

#create new table
t = Table([freq, flux, error, telescope, source], names=('Frequency (um)', 'Flux (Jy)', 'Percent Error', 'Telescope', 'Reference'))




#Sort elements in table by frequency

data1= np.array(t)   #convert our new table into an array

def getKey(item):
        return item[0]
        
data2 = np.array(sorted(data1, key=getKey))  #sort rows by the 0th element (frequency)

#create a new table to put our sorted array into

table1 = Table(names=('Frequency (um) ','Flux (Jy) ','Percent Error', 'Telescope','Reference'), dtype = ('f8', 'f4', 'f4', 'S32', 'S32')) #final table

#append array rows into the new table
for i in range(len(data2)):
    table1.add_row(data2[i])

table1.pprint(max_lines=1000, max_width = 1000) #print all the rows in the table

#now copy the output into the object sed file