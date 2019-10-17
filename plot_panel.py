import matplotlib
import matplotlib.cm as cm
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure

import wx

ERR_TOL = 1e-5  # floating point slop for peak-detection


matplotlib.rc('image', origin='lower')
#to create a wxPanel that matplotlib can plot on
class PlotPanel(wx.Panel):
    def __init__(self,*args,**kwargs ):
        wx.Panel.__init__(self, *args,**kwargs)

        self.fig = Figure((0,0),70)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.fig)
        self.toolbar = NavigationToolbar(self.canvas)  # matplotlib toolbar
        self.toolbar.Realize()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(sizer)

    def plot(self,*args,**kwargs):
        self.ax.cla()
        self.ax.plot(*args,**kwargs)
        self.canvas.draw()
