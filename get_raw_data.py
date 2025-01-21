from astroquery.simbad import Simbad 
from astropy.coordinates import SkyCoord 
import astropy.units as u 
import numpy as np
import time 

Simbad.ROW_LIMIT = 0

file = open('output2.txt', 'a')

ra_lower = 0
ra_upper = 0.2
while(ra_lower < 360):
    file  = open('output2.txt', 'a')
 
    query = """
        SELECT ra, dec, main_id, rvz_redshift, otype
        FROM basic
        WHERE otype NOT IN ('planet', 'asteroid', 'moon', 'comet')
        AND ra BETWEEN {} AND {}   -- RA is between 0.5 and 1.5 degrees
        AND dec BETWEEN -90 AND 90    -- DEC is between -90 and +90 degrees
        AND rvz_redshift IS NOT NULL
            """.format(ra_lower, ra_upper)
    
    failed = True
    retry_num = 0
    while(failed == True):
        try:
            print("try number: {}".format(retry_num), flush=True)
            result_table = Simbad.query_tap(query)
            failed = False
        
        except:
            retry_num +=1
            print("time out. Trying again in 1 second")
            time.sleep(1)
        
    
    # get all the data 
    ra_values       = result_table['ra']
    dec_values      = result_table['dec']
    id_values       = result_table['main_id']
    redshift_values = result_table["rvz_redshift"]
    type_values     = result_table['otype']
    
    # put all data into the text file 
    for i in range(len(result_table)):
        file.write("{},{},{},{},{}\n".format(ra_values[i], dec_values[i], id_values[i], redshift_values[i], type_values[i]))
    
    # save raw data file 
    file.write("\n")
    file.write("\n")
    file.close()
    

    print("saved {} data points for ra {}:{} \n".format(len(result_table), ra_lower, ra_upper), flush=True)
    
    ra_lower = ra_upper
    ra_upper += 0.2
    
    # don't spam the database or else we will get kicked out 
    time.sleep(0.3)
    
        

file.close()
#print(result_table)





