# Write your code here
def coins(one, two, five, goal):
    for a in range(0,one+1):
        for b in range(0,two+1):
            for c in range(0,five+1):
                if a + b * 2 + c * 5 == goal:
                    return True
    return False