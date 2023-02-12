with open('sample.in') as file:
    input = file.read()

for i in range(4, len(input)):
    s = set(input[(i-4):i])
    if len(s) == 4:
        print(i)
        break