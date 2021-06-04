import re

authors = set()

with open('input.txt') as f:
    for line in f:
        x = re.search(r'Author: (.*) <', line)
        if x:
            author = x.group(1)
            authors.add(author)

authors = sorted(authors)

with open('output.txt', 'w') as output:
    for author in authors:
        output.write(f'{author}\n')