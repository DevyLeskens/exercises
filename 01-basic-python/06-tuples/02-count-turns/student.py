# Write your code here
def count_turns(ns):
    result = 0

    for (x, y, z) in zip(ns, ns[1:], ns[2:]):
        if x < y > z or x > y < z:
            result += 1

    return result
