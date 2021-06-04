from datetime import datetime
import re
import sys

def sortByDate(x):
    y = re.search(r'Date:.*(.*)', x)
    if not y:
        sys.exit(-1)
    date = y.group(1)
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')


with open('input.txt') as f:
    input = f.read()

commits = re.findall(r'commit.*?Closed \#\d+', input, re.DOTALL | re.MULTILINE)

commits.sort(key=sortByDate, reverse=True)

with open('output.txt', 'w') as output:
    output.write("\n\n".join(commits))
