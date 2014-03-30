__author__ = 'Jake'

import wx
import os
import sys

class UnsuiGUI(wx.App):
    def OnInit(self):
        self.frame = MapFrame(None, title="MapFrame")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True


class RedirectText:
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)


class MapFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=(700, 500), style=wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX, name="Frame"):
        super(MapFrame, self).__init__(parent, id, title, pos, size, style, name)

        # Attributes
        self.panel = wx.Panel(self, id=wx.ID_ANY, pos=wx.DefaultPosition,
                              size=(500, 500), style=wx.NO_BORDER|wx.EXPAND, name="")

        vsizer = wx.BoxSizer(wx.HORIZONTAL)
        mapsizer = wx.BoxSizer(wx.VERTICAL)
        textsizer = wx.BoxSizer(wx.VERTICAL)

        img_path = os.path.abspath("./apartmentdesign.jpg")
        bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_JPEG)
        img = wx.StaticBitmap(self.panel, wx.ID_ANY, bitmap=bitmap)

        start_button = wx.Button(self.panel, label="Start")
        start_button.Bind(wx.EVT_BUTTON, self.StartButton)
        end_button = wx.Button(self.panel, label="Quit")
        end_button.Bind(wx.EVT_BUTTON, self.QuitButton)

        self.txtctrl = wx.TextCtrl(self.panel)
        self.statictext = wx.TextCtrl(self.panel, style=wx.TE_READONLY|wx.TE_MULTILINE)

        self.txtctrl.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)

        textsizer.Add(self.statictext, 5, wx.EXPAND, 5)
        textsizer.Add(self.txtctrl, 5, wx.EXPAND, 5)
        mapsizer.Add(img, 5, wx.EXPAND | wx.ALIGN_CENTER, 5)

        mapsizerbuttonsizer = wx.BoxSizer(wx.HORIZONTAL)
        mapsizerbuttonsizer.Add(start_button, 5, wx.ALIGN_LEFT, 5)
        mapsizerbuttonsizer.Add(end_button, 5, wx.ALIGN_LEFT, 5)

        mapsizer.Add(mapsizerbuttonsizer, 0, wx.EXPAND|wx.ALIGN_CENTER, 5)
        vsizer.Add(mapsizer, 0, wx.EXPAND|wx.ALIGN_LEFT, 5)
        vsizer.Add(textsizer, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5)

        self.panel.SetSizer(vsizer)

        self.redir=RedirectText(self.statictext)
        sys.stdout=self.redir

    def OnEnter(self, evt):
        self.txtctrl.GetValue()


    def RunGame(self):
        os.system("Unsui.py")


    def StartButton(self, evt):
        self.RunGame()

    def QuitButton(self, evt):
        sys.exit()


app = UnsuiGUI(0)
app.MainLoop()