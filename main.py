import numpy as np
from wxglade_out import MyFrame
import wx
import osa

#the instance that abstract the physical OSA
the_osa = osa.Osa()
class MyApp(wx.App):
    # trivial stuff
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MainFrame(MyFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.save_path= ''

    def on_refresh(self,event):
        #the callback for the `Refresh' button.
        #The binding is done in wxglade_out.py. Same as below
        self.plot_panel.plot(the_osa.data)
    def on_browse(self,event):
        with wx.FileDialog(self, "Save XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            self.save_path= fileDialog.GetPath()
            self.text_ctrl_savepath.SetValue(self.save_path)

    def on_save(self,event):
        #the callback for the save button
        try:
            with open(self.save_path, 'wb') as f:
                #the_osa instance is saved
                the_osa.save(f)
        except IOError:
            wx.LogError("Cannot save current data in file {}.".format(self.save_path))

    def on_path_text_change(self, event):  # wxGlade: MyFrame.<event_handler>
        #whenever the path text is changed it will be updated
        self.save_path = self.text_ctrl_savepath.Value
        print(self.save_path)

    def on_gen_data(self,event):
        #the callback for the `acquire date' button. For now the_osa just generat some radom data
        the_osa.gen_random_data()


    def on_saveas(self,event):
        #the callback function that create a saveas file dialog
        with wx.FileDialog(self, "Save XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                with open(pathname,'wb') as f:
                    #the_osa instance is saved
                    the_osa.save(f)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)


    def on_open(self,event):
        #the callback function that create a open file dialog
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
        #the callback for the  quit button
        self.Close()

if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
