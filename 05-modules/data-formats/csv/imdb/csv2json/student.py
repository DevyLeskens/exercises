import csv, json, sys

data = list(csv.DictReader(sys.stdin))

print(json.dumps(data))