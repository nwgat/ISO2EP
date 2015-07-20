import xbmcaddon
import xbmcgui
addon       = xbmcaddon.Addon()

# Read nfo file for episodes
file = open('disc.nfo', 'r')
print file.read()

# Map episodes to file S01E01 > disc1.iso\BDMV\PLAYLIST\00051.mpls
#todo

# Play file (click S01E01 then play disc1.iso\BDMV\PLAYLIST\00051.mpls)
#todo

#xbmcgui.Dialog().ok.print file.read()
