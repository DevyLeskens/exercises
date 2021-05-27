import re
import argparse
from PIL import Image
import sys
from pathlib import Path

def parseSize(string):
    match = re.fullmatch(r'(\d+)x(\d+)',string)

    if not match:
        print("Foute invoer: grootte moet in het formaat BxH zijn.")
        sys.exit(-1)
    width, height = match.groups()
    return (int(width), int(height))

def haalExtensieUitNaam(pattern, input_file):
    path = Path(input_file)
    basename = path.stem
    extension = path.suffix
    return pattern.replace('%b', basename).replace('.%x', extension)

parser = argparse.ArgumentParser(description='Make thumbnail of image.')
parser.add_argument('--pattern', default='%b-thumbnail.%x', help='Patroon voor gegenereerde thumbnail.')
parser.add_argument('--size', default='64x64', help='Grootte van de thumbnail.')
parser.add_argument('files', nargs='+')

args = parser.parse_args()

size = parseSize(args.size)
inputFiles = args.files
pattern = args.pattern

for inputFile in inputFiles:
    outputFile = haalExtensieUitNaam(pattern, inputFile)

    image = Image.open(inputFile)
    image.thumbnail(size)
    image.save(outputFile)