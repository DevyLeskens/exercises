import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as page:
    print(page.read())