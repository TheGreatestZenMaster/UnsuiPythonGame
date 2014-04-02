import wx
import os
import sys
import threading
import Queue
import time
from subprocess import Popen, PIPE
import wx.py

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

class BashProcessThread(threading.Thread):
    def __init__(self, readlineFunc):
        threading.Thread.__init__(self)

        self.readlineFunc = readlineFunc
        self.outputQueue = Queue.Queue()
        self.setDaemon(True)

    def run(self):
        while True:
            line = self.readlineFunc()
            self.outputQueue.put(line)

    def getOutput(self):
        """ called from other thread """
        lines = []
        while True:
            try:
                line = self.outputQueue.get_nowait()
                lines.append(line)
            except Queue.Empty:
                break
        return ''.join(lines)

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
        end_button = wx.Button(self.panel, label="Quit")
        start_button.Bind(wx.EVT_BUTTON, self.OnStart)
        end_button.Bind(wx.EVT_BUTTON, self.QuitButton)

        self.txtctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        self.txtctrl.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)

        textsizer.Add(self.txtctrl, 5, wx.EXPAND, 5)
        mapsizer.Add(img, 5, wx.EXPAND | wx.ALIGN_CENTER, 5)

        mapsizerbuttonsizer = wx.BoxSizer(wx.HORIZONTAL)
        mapsizerbuttonsizer.Add(start_button, 5, wx.ALIGN_LEFT, 5)
        mapsizerbuttonsizer.Add(end_button, 5, wx.ALIGN_LEFT, 5)

        mapsizer.Add(mapsizerbuttonsizer, 0, wx.EXPAND|wx.ALIGN_CENTER, 5)
        vsizer.Add(mapsizer, 0, wx.EXPAND|wx.ALIGN_LEFT, 5)
        vsizer.Add(textsizer, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5)

        self.panel.SetSizer(vsizer)

        self.redir=RedirectText(self.txtctrl)
        sys.stdout=self.redir


    def OnEnter(self, evt):
        self.txtctrl.GetValue()

    def OnStart(self, evt):
        self.frame = wx.py.shell.ShellFrame(InterpClass=MyInterpretor)
        self.frame.Show()

    def QuitButton(self, evt):
        sys.exit()

class MyInterpretor(object):
    def __init__(self, locals, rawin, stdin, stdout, stderr):
        self.introText = "Welcome to stackoverflow bash shell"
        self.locals = locals
        self.revision = 1.0
        self.rawin = rawin
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

        self.more = False

        # bash process
        self.bp = Popen("Unsui.py", shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)

        # start output grab thread
        self.outputThread = BashProcessThread(self.bp.stdout.readline)
        self.outputThread.start()

        # start err grab thread
        self.errorThread = BashProcessThread(self.bp.stderr.readline)
        self.errorThread.start()

    def getAutoCompleteKeys(self):
        return [ord('\t')]

    def getAutoCompleteList(self, *args, **kwargs):
        return []

    def getCallTip(self, command):
        return ""

    def push(self, command):
        command = command.strip()
        if not command: return

        self.bp.stdin.write(command+"\n")
        # wait a bit
        time.sleep(.1)

        # print output
        self.stdout.write(self.outputThread.getOutput())

        # print error
        self.stderr.write(self.errorThread.getOutput())

app = UnsuiGUI(0)
app.MainLoop()

