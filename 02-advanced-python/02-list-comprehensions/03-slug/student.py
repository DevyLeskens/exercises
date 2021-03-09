# Write your code here
def slug(name):
    splitname = name.split(' ')
    firstname = splitname[0]
    lastname = splitname[1:]

    return '-'.join(s.lower() for s in lastname + [firstname])
