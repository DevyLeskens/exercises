import csv


with open('solutions.csv') as f:
    solutions = f.read().strip().split(',')

with open('answers.csv') as f:
    reader = csv.reader(f)
    with open('output.txt', 'w') as out:
        for student, *answers in reader:
            score = sum(1 for solution, answer in zip(solutions, answers) if solution == answer)
            out.write(f'{student} {score}\n')
