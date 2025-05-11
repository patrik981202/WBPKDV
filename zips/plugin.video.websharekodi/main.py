import xbmcplugin
import xbmcgui
import sys

handle = int(sys.argv[1])
xbmcplugin.setPluginCategory(handle, "Webshare")
xbmcplugin.setContent(handle, "videos")

li = xbmcgui.ListItem(label="Sample video")
li.setInfo('video', {'title': 'Sample video'})
xbmcplugin.addDirectoryItem(handle=handle, url="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", listitem=li)
xbmcplugin.endOfDirectory(handle)
