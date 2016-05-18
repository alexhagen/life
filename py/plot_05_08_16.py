import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PolyCollection
from mpl_toolkits.basemap import Basemap, shiftgrid, cm
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
import gpxpy
import gpxpy.gpx
import cPickle as pickle
import os.path
from scipy.interpolate import *

# Parsing an existing file:
# -------------------------

gpx_file = open('hike_05_08_16.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

lon = []
lat = []
ele = []
dist = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            lon = np.append(lon, point.longitude)
            lat = np.append(lat, point.latitude)
            # dist = np.append(dist, np.sqrt(point.longitude))
            ele = np.append(ele, point.elevation)
'''
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
m = Basemap(projection='lcc', llcrnrlon=-88., llcrnrlat=37.5, urcrnrlon=-84.,
            urcrnrlat=42., resolution='h', lat_0=40.,
            lon_0=-86.)
m.etopo()
m.drawcounties()
m.drawrivers(linewidth=1.5, color="#7299C6")
m.drawstates()
m.plot(lon, lat, 'r-', latlon=True)
plt.show()
'''

if not os.path.isfile('plot_05_08_16.pkl'):
    # read in etopo5 topography/bathymetry.
    url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'
    etopodata = Dataset(url)

    topoin = etopodata.variables['ROSE'][:]
    lons = etopodata.variables['ETOPO05_X'][:]
    lats = etopodata.variables['ETOPO05_Y'][:]
    # shift data so lons go from -180 to 180 instead of 20 to 380.
    topoin,lons = shiftgrid(180.,topoin,lons,start=False)

    # plot topography/bathymetry as an image.
    fig = plt.figure()
    ax = plt.gca()
    # create the figure and axes instances.
    # setup of basemap ('lcc' = lambert conformal conic).
    # use major and minor sphere radii from WGS84 ellipsoid.
    m = Basemap(llcrnrlon=-87.5,llcrnrlat=40.,urcrnrlon=-86.5,urcrnrlat=41.0,\
                resolution='h',projection='lcc',\
                lat_0=39.7910,lon_0=-86.1480)
    # transform to nx x ny regularly spaced 5km native projection grid
    nx = int((m.xmax-m.xmin)/50.)+1; ny = int((m.ymax-m.ymin)/50.)+1
    topodat, x, y = m.transform_scalar(topoin, lons, lats, nx, ny, returnxy=True)
    with open('plot_05_08_16.pkl', 'wb') as output:
        pickle.dump(m, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(topodat, output, -1)
        pickle.dump(lons, output, -1)
        pickle.dump(lats, output, -1)
        pickle.dump(interp, output, -1)
else:
    with open('plot_05_08_16.pkl', 'rb') as input:
        fig = plt.figure()
        ax=plt.gca()
        m = pickle.load(input)
        topodat = pickle.load(input)
        lons = pickle.load(input)
        lats = pickle.load(input)

# lafayette
plt.plot(*m(-86.8786,40.4172), marker='d')

m.drawstates()
m.plot(lon, lat, 'r-', latlon=True)

m.ax = ax
m.drawstates(linewidth=0.1, color="#A7A9AC")
m.drawrivers(linewidth=1.5, color="#7299C6")
m.fillcontinents(color='white', lake_color='#7299C6')
m.drawcoastlines(linewidth=0.1, color="#A7A9AC")
m.drawcounties(linewidth=0.1, color="#A7A9AC")

ax.contour(x, y, topodat, 15, cmap=cm.terrain,  vmin=-800.0, vmax=2000.,
           linewidth=0.3)

ax.axis("off")

plt.show()
