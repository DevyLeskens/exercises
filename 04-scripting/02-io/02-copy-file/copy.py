import sys

from shutil import copyfile
copyfile(sys.argv[1], sys.argv[2])

# with open(sys.argv[1], 'r') as input:
#     with open(sys.argv[2], 'w') as output:
#         output.write(input.read())
