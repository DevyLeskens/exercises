for number in range(0,10000+1):
    first = str(number).rjust(10)
    second = bin(number).rjust(20)
    third = hex(number).rjust(10)
    print(f'{first}{second}{third}')