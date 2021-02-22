# Write your code here
def nth_longest_string(n, strings):
    result = sorted(strings, key=len)
    return result[-n]
