from datetime import datetime
import sys


def isValid(string):
    try:
        datetime.strptime(string, '%d-%m-%Y')
        return True
    except ValueError:
        return False


with open('input.txt') as input:
    with open('output.txt', 'w') as output:
        for line in input:
            line = line.strip()
            if isValid(line):
                output.write(f'{line}\n')
