with open('sample.in') as file:
    data = [i for i in file.read().strip().split('\n')]

pairs = 0

for entry in data:
    first, second = entry.split(',')
    
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    if first[0] <= second[0] and first[1] >= second[1]:
        pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs += 1

print(pairs)