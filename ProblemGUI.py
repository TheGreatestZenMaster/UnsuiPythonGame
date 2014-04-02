import wx
import os
import sys
from wx.py.shell import Shell as PyShell

class UnsuiGUI(wx.App):
    def OnInit(self):
        self.frame = MapFrame(None, title="MapFrame")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MapFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=(900, 500), style=wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX, name="Frame"):
        super(MapFrame, self).__init__(parent, id, title, pos, size, style, name)

        # Attributes
        self.panel = wx.Panel(self, id=wx.ID_ANY, pos=wx.DefaultPosition,
                              size=(900, 500), style=wx.EXPAND, name="")

        vsizer = wx.BoxSizer(wx.HORIZONTAL)
        mapsizer = wx.BoxSizer(wx.VERTICAL)
        textsizer = wx.BoxSizer(wx.VERTICAL)

        img_path = os.path.abspath("./apartmentdesign.jpg")
        bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_JPEG)
        img = wx.StaticBitmap(self.panel, wx.ID_ANY, bitmap=bitmap)

        start_button = wx.Button(self.panel, label="Start")
        end_button = wx.Button(self.panel, label="Quit")
        start_button.Bind(wx.EVT_BUTTON, self.OnStart)
        end_button.Bind(wx.EVT_BUTTON, self.QuitButton)

        self.shell = PyShell(self.panel, -1, size=(400, -1))
        self.shell.clear()
        self.shell.redirectStdin(True)
        self.shell.redirectStdout(True)

        textsizer.Add(self.shell, 5, wx.EXPAND | wx.TE_MULTILINE, 5)
        mapsizer.Add(img, 5, wx.EXPAND | wx.ALIGN_CENTER, 5)

        mapsizerbuttonsizer = wx.BoxSizer(wx.HORIZONTAL)
        mapsizerbuttonsizer.Add(start_button, 5, wx.ALIGN_LEFT, 5)
        mapsizerbuttonsizer.Add(end_button, 5, wx.ALIGN_LEFT, 5)

        mapsizer.Add(mapsizerbuttonsizer, 0, wx.EXPAND|wx.ALIGN_CENTER, 5)
        vsizer.Add(mapsizer, 0, wx.EXPAND | wx.ALIGN_LEFT, 5)
        vsizer.Add(textsizer, 0, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        self.panel.SetSizer(vsizer)

    def OnStart(self, evt):
        self.shell.execStartupScript("Unsui.py")

    def QuitButton(self, evt):
        sys.exit()


app = UnsuiGUI(0)
app.MainLoop()

