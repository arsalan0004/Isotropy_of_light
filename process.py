import healpy as hp
import numpy as np

def hexagon_average_on_sphere(data, nside=32):
    """
    Averages values within hexagonal cells on a sphere.

    Parameters:
    - data: List of tuples (latitude, longitude, value).
    - nside: Healpix parameter determining resolution. Higher values mean finer cells.

    Returns:
    - hexagon_values: List of averaged values for each hexagonal cell.
    """
    # Convert latitude and longitude to Healpix pixel indices
    latitudes, longitudes, values = zip(*data)
    theta = np.radians(90 - np.array(latitudes))  # Convert latitude to colatitude
    phi = np.radians(np.array(longitudes))        # Convert longitude to radians
    
    # Healpix pixel indices
    npix = hp.nside2npix(nside)
    pixel_indices = hp.ang2pix(nside, theta, phi)

    # Initialize arrays to store sums and counts
    value_sums = np.zeros(npix)
    value_counts = np.zeros(npix)

    # Sum values and counts for each pixel
    for pix, val in zip(pixel_indices, values):
        value_sums[pix] += val
        value_counts[pix] += 1

    # Compute averages, avoiding division by zero
    hexagon_values = np.zeros(npix)
    nonzero_mask = value_counts > 0
    hexagon_values[nonzero_mask] = value_sums[nonzero_mask] / value_counts[nonzero_mask]

    return hexagon_values
    
    
def nside_to_npixel(nside):
    return 12 * nside * nside

# load the data
data_file = open("filtered_data.txt", 'r')
data = []
i = 0
for line in data_file:

    try:
         ra, dec, id, redshift, type = line.split(',')
         ra = float(ra)
         dec = float(dec)
         redshift = float(redshift)
         #print(f"{ra},{dec},{redshift}\n")
         data.append([dec, ra, redshift])
    except:
        print(line)
        print("something wrong at {}".format(i))
        continue 
    i+=1 
    
# data = [[-90, 0, -3], [-45, 0, -2], [0, 0, -1], [45, 0, 5], [90, 0, 10],
# [0, 0, -3], [0, 45, -2], [0, 0, -1], [0, 45, 5], [0, 90, 10], [0, 135, 20], [0, 270, 30]]

print(f"done loading {i} data ")
processed_file = open("processed_data.txt", 'a')

nside = 64 # Controls the resolution of hexagonal cells
hexagon_averages = hexagon_average_on_sphere(data, nside)
print(hexagon_averages)

# get the pixel centres 
pixel_indices = np.arange(nside_to_npixel(nside))
theta, phi = hp.pix2ang(nside, pixel_indices)

# get average redshift values 
for t, p, rs in zip(theta, phi, hexagon_averages):
    processed_file.write(f"{t},{p},{rs}\n")

processed_file.close()

# Visualize results (optional, requires matplotlib)
# import matplotlib.pyplot as plt
# hp.mollview(hexagon_averages, title="Hexagon Averages on Sphere", unit="Average Value")
# plt.show()
