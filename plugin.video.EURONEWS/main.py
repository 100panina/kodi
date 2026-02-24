import requests
from bs4 import BeautifulSoup
import re
import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

def get_links():
#    flinks_list = []
    url = "https://euronews.bg/euronews-na-zhivo/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    iframe_src = soup.find_all("iframe")
    for iframe in iframe_src:
        src=iframe['src']
        if "live" in iframe['src']:
#            print(src.replace(src, "https:" + src, 3))
            r = requests.get(src.replace(src, "https:" + src, 3))
            soup = BeautifulSoup(r.text, "html.parser")
            play_link = soup.find_all("source")
            for plink in play_link:
                src = plink['src']
#                print(src.replace(src, "https:" + src, 3))
                xbmc.Player().play(src.replace(src, "https:" + src, 3))

get_links()