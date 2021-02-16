# Write your code here
def median(ns):
    ns = sorted(ns)
    x = len(ns) // 2

    if len(ns) % 2 != 0:
        return ns[len(ns)//2]
    else:
        return (ns[x-1] + ns[x]) / 2
