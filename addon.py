import xbmcaddon
import xbmcgui
addon       = xbmcaddon.Addon()

# Read nfo file for episodes
file = open('disc.nfo', 'r')
print file.read()

# Map episodes to file disc1.iso\BDMV\PLAYLIST\00051.mpls > S01E01 
#todo

# Play file (click S01E01 then play disc1.iso\BDMV\PLAYLIST\00051.mpls)
#todo

#xbmcgui.Dialog().ok.print file.read()
