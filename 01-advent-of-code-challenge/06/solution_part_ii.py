with open('sample.in') as file:
    input = file.read()

for i in range(14, len(input)):
    s = set(input[(i-14):i])
    if len(s) == 14:
        print(i)
        break