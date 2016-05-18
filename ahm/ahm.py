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

# sans: "Source Sans Pro", "Open Sans", "Helvetica Neue", "Arial", sans-serif
# serif: "Calendas Plus","Crimson Text", "Hoefler Text", "Georgia", serif
# monospace: "Lucida Console", monospace


class ahm:
    black = '#142735'
    blue = '#285668'
    white = '#f9f9f9'
    grey_dark = '#285668'
    grey_medium = '#999999'
    grey_light = '#d9d9d9'
    grey_light_2 = '#ececec'
    grey_light_3 = '#f1f3f5'
    hilite = '#fffbd7'
    link = '#919789'
    accent = '#FC8D82'

    def __init__(self, threed=False,
                 center=None, aspect_ratio=1.0, width=None,
                 llcorner=None, urcorner=None,
                 contour=False):
        ''' something '''

    def add_gpx(self, filename=None, color=self.hilite):
        print 'adding gpx'

    def add_text(self):
        print 'adding text'

    def add_circle(self):
        print 'adding circle'
