import json
import urllib
import numpy as np
import datetime
import sys
import numpy as np
import os
sys.path.append(os.path.expanduser('~') + "/code/")
from pym import func as ahf
import matplotlib.dates as mdate

url = "http://api.wunderground.com/api/" + \
    "91993adaa57d88ce/history_20160408/q/IN/47901.json"
response = urllib.urlopen(url)
data = json.loads(response.read())

x = []
y = []

for time in data['history']['observations']:
    t = datetime.datetime(int(time['date']['year']),
                          int(time['date']['mon']), int(time['date']['mday']),
                          int(time['date']['hour']), int(time['date']['min']))
    dt = (t - datetime.datetime(2016, 4, 8, 16, 0)).total_seconds()
    x = np.append(x, dt)
    y = np.append(y, float(time['tempi']))

url = "http://api.wunderground.com/api/" + \
    "91993adaa57d88ce/history_20160409/q/IN/47901.json"
response = urllib.urlopen(url)
data = json.loads(response.read())

for time in data['history']['observations']:
    t = datetime.datetime(int(time['date']['year']),
                          int(time['date']['mon']), int(time['date']['mday']),
                          int(time['date']['hour']), int(time['date']['min']))
    dt = (t - datetime.datetime(2016, 4, 8, 16, 0)).total_seconds()
    x = np.append(x, dt)
    y = np.append(y, float(time['tempi']))

arrival = (datetime.datetime(2016, 4, 8, 17, 0) -
           datetime.datetime(2016, 4, 8, 16, 0)).total_seconds()
departure = (datetime.datetime(2016, 4, 9, 5, 0) -
             datetime.datetime(2016, 4, 8, 16, 0)).total_seconds()
x1 = x[x > arrival]
y = y[x > arrival]
x = x1
x1 = x[x < departure]
y = y[x < departure]
x = x1

temp = ahf.curve(x, y, name=r'$T$')
plot = temp.plot(linestyle='-', linecolor='#D1D3D4')
plot.fill_between(x, np.zeros_like(x), y, fc='#D1D3D4')
plot.lines_on()
plot.markers_off()
plot.ax.tick_params(axis="x", colors='#D1D3D4')
plot.ax.tick_params(axis="y", colors='#D1D3D4')
plot.ax.yaxis.label.set_color('#D1D3D4')
plot.ax.xaxis.label.set_color('#D1D3D4')
plot.ax.spines['bottom'].set_visible(False)
plot.ax.spines['left'].set_visible(False)


plot.xticks([np.min(x), 1.0 * (np.max(x) - np.min(x)) / 3.0 + np.min(x),
             2.0 * (np.max(x) - np.min(x)) / 3.0 + np.min(x), np.max(x)],
            ["5pm", "9pm", "1am", "5am"])
plot.ylabel(r'Temperature ($T$) [$\mathrm{^{o}F}$]')
plot.ylim(25., 45.)

plot.export('../img/plot_04_08_16', formats=['pdf', 'pgf'], sizes=['cs'],
            customsize=(4, 2.5))
plot.show()
