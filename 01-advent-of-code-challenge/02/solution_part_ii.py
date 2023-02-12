with open('sample.in') as file:
    rounds = [i for i in file.read().strip().split('\n')]

outcomes = {
    'A X':4, 'A Y':8, 'A Z': 3,
    'B X':1, 'B Y':5, 'B Z': 9,
    'C X':7, 'C Y':2, 'C Z': 6
}

totalPointsPart1 = 0

for round in rounds:
    totalPointsPart1 += outcomes[round]

outcomesPart2 = {
    'A X':3, 'A Y':4, 'A Z': 8,
    'B X':1, 'B Y':5, 'B Z': 9,
    'C X':2, 'C Y':6, 'C Z': 7
}

totalPointsPart2 = 0

for round in rounds:
    totalPointsPart2 += outcomesPart2[round]

print(totalPointsPart2)