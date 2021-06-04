import re

result = {}

with open('input.txt') as f:
    for line in f:
        x = re.search(r'Author: (.*) <', line)
        if x:
            author = x.group(1)
            result[author] = result.get(author,0) + 1

result = sorted(result.items(), key=lambda p: p[1], reverse=True)

with open('output.txt', 'w') as output:
    for author, n in result:
        output.write(f'{author}: {n}\n')
