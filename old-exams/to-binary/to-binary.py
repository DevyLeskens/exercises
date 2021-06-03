with open('input.txt') as input:
    with open('output.txt', 'w') as output:
        for line in input:
            print(bin(int(line))[2:], file=output)
