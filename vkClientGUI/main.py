import vk
import config
import wx

passw = config.vkPassw
login = config.vkLogin
appId = config.appId
myId = config.myId

##vkAuthSession = vk.AuthSession(appId, login, passw, scope='wall, messages')
##api = vk.API(vkAuthSession, v='5.69')


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Bring Back The Wall") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()



