""" import re


with open('input.txt') as input:
    with open('output.txt', 'w') as output:
        for line in input:
            for value in line.split():
                 if re.match(r'^\$', value):
                     number = value.split('(')
                     number = number[1]
                     number = number.replace(')', '')
                     print(line,hex(int(number)).upper(), file=output) 
 """

import re

with open('input.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            line = re.sub(r'\$HEX\((\d+)\)', lambda m: "0x" +
                          hex(int(m.group(1))).upper()[2:], line)
            out.write(line)
