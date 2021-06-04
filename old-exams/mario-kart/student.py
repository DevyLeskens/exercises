""" with open('input.txt') as file:
    lines = [line.strip() for line in list(file)]

scores = {}
races = [lines[i:i+100] for i in range(0, len(lines), 100)]

for race in races:
    for name, score in zip(race, range(100, 0, -1)):
        if name not in scores:
            scores[name] = 0
        scores[name] += score

top10 = sorted(scores.items(), key=lambda p: p[1], reverse=True)[0:10]

with open('output.txt', 'w') as out:
    for name, score in top10:
        out.write(f'{name}\n') """

dict = {}
with open('input.txt') as file:
    game = list( line.strip() for line in file )
    for i in range(0,10000):
        punten = 100 - (i%100)
        if game[i] not in dict:
            dict[game[i]] = punten
        else:
            dict[game[i]] += punten
sorted_values = sorted(dict.items(), key = lambda x: x[1], reverse = True)
"""print(sorted_values)"""
for j in range(0,10):
    print(sorted_values[j][0])

