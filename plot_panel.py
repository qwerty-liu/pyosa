import matplotlib
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

import wx
import wx.xrc as xrc

ERR_TOL = 1e-5  # floating point slop for peak-detection


matplotlib.rc('image', origin='lower')

class PlotPanel(wx.Panel):
    def __init__(self,*args,**kwargs ):
        wx.Panel.__init__(self, *args,**kwargs)

        self.fig = Figure((0,0),70)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.fig)
        self.toolbar = NavigationToolbar(self.canvas)  # matplotlib toolbar
        self.toolbar.Realize()
        # self.toolbar.set_active([0,1])

        # Now put all into a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        # This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        # Best to allow the toolbar to resize!
        sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(sizer)
#        self.Fit()

    def plot(self,*args,**kwargs):
        self.ax.cla()
        self.ax.plot(*args,**kwargs)
        self.canvas.draw()
