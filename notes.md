**BD path**
`bluray://udf%3a%2f%2fC%253a%255cetc%255cdisc1.iso%2f/BDMV/PLAYLIST/00000.mpls`

**play file**

import xbmc

link='bluray://udf%3a%2f%2fC%253a%255cetc%255cdisc1.iso%2f/BDMV/PLAYLIST/00000.mpls'

xbmc.Player().play(item=link)

**read nfo file**

import xbmcaddon
import xbmcgui
file = open('disc.nfo', 'r')
print file.read()
