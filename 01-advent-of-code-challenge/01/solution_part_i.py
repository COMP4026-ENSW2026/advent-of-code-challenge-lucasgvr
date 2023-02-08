with open('sample.in') as file:
    data = [i for i in file.read().strip().split("\n")]
    
maxCal = 0
count = 0

for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
        
    if count > maxCal:
        maxCal = count
        
print(maxCal)
    
highest = []
sums = 0

for item in data:
    if item == '':
        highest.append(sums)
        sums = 0
    else:
        sums += int(item)
    
finalSum = 0

for i in range(3):
    finalSum += max(highest)
    highest.remove(max(highest))