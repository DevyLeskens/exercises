with open('input.txt') as input:
    with open('output.txt', 'w') as output:
        for line in input:
            for id in line.strip().split(','):
                output.write(f'{id}\n')