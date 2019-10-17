import numpy as np
from wxglade_out import MyFrame
import wx
import osa
the_osa = osa.Osa()
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MainFrame(MyFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #self.Bind(wx.EVT_BUTTON, lambda event:self.on_btn_refresh(event), self.btn_refresh)

    def on_refresh(self,event):
        self.plot_panel.plot(the_osa.data)

    def on_gen_data(self,event):
        the_osa.gen_random_data()

    def on_save(self,event):
        with wx.FileDialog(self, "Save XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                with open(pathname,'wb') as f:
                    the_osa.save(f)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

    def on_open(self,event):
        with wx.FileDialog(self, "Open XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'rb') as file:
                    the_osa.load_from_file(file)
            except IOError:
                wx.LogError("Cannot open file '%s'." %  pathname)

    def on_close(self,event):
        self.Close()

if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
