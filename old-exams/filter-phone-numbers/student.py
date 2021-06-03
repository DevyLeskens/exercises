import re

with open('input.txt') as input:
    with open('output.txt', 'w') as output:
        for line in input:
            if re.fullmatch(r'(0|\+32-)4[56789][0-9]-\d{2}-\d{2}-\d{2}', line.strip()):
                output.write(line)
