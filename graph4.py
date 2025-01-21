import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy

# how many divisions there are in the longitude and latitude
# ex. LAT_RESOLUTION 10 means total latitude divided by 10... so only
# latitudes 0, 18, 36... degrees can be set 
LAT_RESOLUTION = 198
LON_RESOLUTION = 396

def add_data_point(lat: int, lon: int, redshift: float):
    """Add data to the graph.

    @param lat : latitude, between 0 and 180 inclusive 
    @param lon : longitude, between 0 and 359 inclusive 
    """
    try:
        lat_index = int(lat / (180 / LAT_RESOLUTION)) - 1
        lon_index = int(lon / (360 / LON_RESOLUTION)) - 1

        if lat_index < 0:
            lat_index = 0
        if lon_index < 0:
            lon_index = 0

        #print("latitude or longitude are {},{}".format(lat, lon))
        #print("lat and lon index are {},{}\n".format(lat_index, lon_index))

        heights[lon_index, lat_index] = redshift

    except Exception as e:
        print("Error: {}".format(e))
        print("latitude or longitude specified cannot be placed in array\n")
        print("latitude or longitude are {},{}\n".format(lat, lon))
        exit()

def lat_lon_to_cartesian(lat, lon, radius):
    """Convert latitude and longitude to Cartesian coordinates"""
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    x = radius * np.cos(lat_rad) * np.cos(lon_rad)
    y = radius * np.cos(lat_rad) * np.sin(lon_rad)
    z = radius * np.sin(lat_rad)
    return np.array([x, y, z])

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the radius of the celestial sphere when redshift = 0
r = 1  # Radius of the Earth

# Define a high-resolution grid that will model redshifts > 0
latitudes = np.linspace(-90, 90, LAT_RESOLUTION) 
longitudes = np.linspace(-180, 180, LON_RESOLUTION)  
latitudes, longitudes = np.meshgrid(latitudes, longitudes)

# Array that will represent redshifts as heights above the celestial sphere defined previously
heights = np.zeros_like(latitudes)

# Load the data 
data_file = open("data/try_1/processed_data.txt", 'r')

data = []

for line in data_file:
    theta, phi, redshift = line.split(',')

    dec = np.degrees(float(theta))
    ra = np.degrees(float(phi))

    add_data_point(dec, ra, redshift)

# Convert the high-res grid to Cartesian coordinates
lat_rad = np.radians(latitudes)
lon_rad = np.radians(longitudes)
x_cloth = (r + heights) * np.cos(lat_rad) * np.cos(lon_rad)
y_cloth = (r + heights) * np.cos(lat_rad) * np.sin(lon_rad)
z_cloth = (r + heights) * np.sin(lat_rad)

# Calculate distance from the sphere's center
distances = np.sqrt(x_cloth**2 + y_cloth**2 + z_cloth**2)

# Normalize distances for coloring
normalized_distances = (distances - r / 10) / (distances.max() - r / 10)

# Apply a power-law transformation to enhance contrast
dramatic_distances = normalized_distances**2  # Squaring emphasizes extremes

# Apply a colormap
colors = cm.coolwarm(dramatic_distances)

# Plot the smooth cloth with transition coloring
ax.plot_surface(x_cloth, y_cloth, z_cloth, facecolors=colors, rstride=1, cstride=1, linewidth=0, antialiased=False)

# Add a arrow pointing north
arrow_length = 4  # Length of the arrow
north_pole = lat_lon_to_cartesian(90, 0, arrow_length)  # North pole coordinates

# add arrow for East 
east_pole = lat_lon_to_cartesian(0, 0, arrow_length)  # North pole coordinates

ax.quiver(0, 0, r, north_pole[0], north_pole[1], north_pole[2], color='red', linewidth=2, arrow_length_ratio=0.1)
ax.quiver(r, 0, 0, east_pole[0], east_pole[1], east_pole[2], color='green', linewidth=2, arrow_length_ratio=0.1)

# Set aspect ratio and view
ax.set_box_aspect([1, 1, 1])
ax.view_init(elev=0, azim=180)

plt.show()
