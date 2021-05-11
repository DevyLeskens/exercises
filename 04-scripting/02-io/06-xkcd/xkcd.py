import json
import urllib.request
import sys


if len(sys.argv) > 1:
    url = f"http://xkcd.com/{sys.argv[1]}/info.0.json"
else:
    url = "http://xkcd.com/info.0.json"


with urllib.request.urlopen(url) as input:
    data = input.read().decode('UTF-8')
    data = json.loads(data)

for key, value in data.items():
    print(f'{key}: {value}')