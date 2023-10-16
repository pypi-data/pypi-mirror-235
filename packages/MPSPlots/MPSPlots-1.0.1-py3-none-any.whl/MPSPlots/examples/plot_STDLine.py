"""
STD line
========
"""

import numpy
from MPSPlots.render2D import SceneList


x = numpy.arange(100)
y = numpy.random.rand(10, 100)
y_mean = numpy.mean(y, axis=0)
y_std = numpy.std(y, axis=0)

figure = SceneList(
    unit_size=(8, 4),
    title='random data simple lines'
)

ax = figure.append_ax(
    x_label='x data',
    y_label='y data',
    show_legend=True
)

_ = ax.add_std_line(
    x=x,
    y_mean=y_mean,
    y_std=y_std,
    label='Fill between lines',
)

_ = figure.show()
