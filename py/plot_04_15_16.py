import json
import numpy as np
import datetime
import sys
import numpy as np
import os
sys.path.append(os.path.expanduser('~') + "/code/")
from pym import func as ahf
import matplotlib.dates as mdate

data = np.loadtxt('runs_05_15_to_04_16.csv', usecols=(0, 1, 3),
                  dtype=np.str, delimiter=',')


x = []
y = []
toty = 0.

for row in data:
    if row[1] == 'Running':
        t = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        dt = (t - datetime.datetime(2015, 5, 1, 12, 0)).total_seconds()
        x = np.append(x, -dt)
        toty = toty + float(row[2])
        y = np.append(y, toty)


print x
print y

mileage = ahf.curve(x, y, name=r'$s$')
plot = mileage.plot(linestyle='-', linecolor='#285668')
plot.fill_between(x, np.zeros_like(x), y, fc='#285668')
plot.lines_on()
plot.markers_off()
plot.ax.tick_params(axis="x", colors='#285668')
plot.ax.tick_params(axis="y", colors='#285668')
plot.ax.yaxis.label.set_color('#285668')
plot.ax.xaxis.label.set_color('#285668')
plot.ax.spines['bottom'].set_visible(False)
plot.ax.spines['left'].set_visible(False)


plot.xticks([-(datetime.datetime(2015, 6, 1, 12, 0) -
             datetime.datetime(2015, 5, 1, 12, 0)).total_seconds(),
             -(datetime.datetime(2015, 9, 1, 12, 0) -
               datetime.datetime(2015, 5, 1, 12, 0)).total_seconds(),
             -(datetime.datetime(2015, 12, 1, 12, 0) -
               datetime.datetime(2015, 5, 1, 12, 0)).total_seconds(),
             -(datetime.datetime(2016, 3, 1, 12, 0) -
               datetime.datetime(2015, 5, 1, 12, 0)).total_seconds()],
            ["6/15", "9/15", "12/15", "3/16"])
plot.ylabel(r'Mileage ($s$) [$\mathrm{mi}$]')
#plot.ylim(25., 45.)

plot.export('../img/plot_04_15_16', formats=['pdf', 'pgf'], sizes=['cs'],
            customsize=(6, 1.5*2.5))
plot.show()
