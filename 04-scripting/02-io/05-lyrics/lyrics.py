import json
import urllib.request
import sys

artist = sys.argv[1]
artist = artist.replace(" ", "%20")

title = sys.argv[2]
title = title.replace(" ", "%20")

url = "https://api.lyrics.ovh/v1/"+artist+"/"+title

with urllib.request.urlopen(url) as lyrics:
    page = json.loads(lyrics.read())
    print(page['lyrics'])