import re

y_spot = 2000000 
ys = set()
beacons_y = set()

with open("sample.in", 'r') as file:
    for ll in file.readlines():
        sx, sy, bx, by = map(int, re.findall(r'(?<=\=)(.*?)(?=,|\:|\n)', ll))

        if by == y_spot:
            beacons_y.add(bx)

        d = abs(bx - sx) + abs(by - sy)
        d -= abs(y_spot - sy)

        for x in range(sx - d, sx + d + 1):
            ys.add(x)

print(str(len(ys - beacons_y)))

mx = 4000000
y_ranges = [[] for _ in range(mx + 1)]
with open("sample.in", 'r') as file:
    for ll in file.readlines():
        sx, sy, bx, by = map(int, re.findall(r'(?<=\=)(.*?)(?=,|\:|\n)', ll))
        d = abs(bx - sx) + abs(by - sy)
        dy = 0
        while d > 0:
            xl = max(0, sx - d)
            xr = min(mx, sx + d)
            if (sy - dy >= 0):
                y_ranges[sy - dy].append([xl, xr])
            if (sy + dy <= mx and dy):
                y_ranges[sy + dy].append([xl, xr])
            dy += 1
            d -= 1

    for ans_y in range(mx + 1):
        xs = y_ranges[ans_y]
        if not xs:
            continue
        xs.sort()

        if xs[0][0] != 0:
            ans_x = 0
            break

        last_e = xs[0][1]
        for ii in range(1, len(xs)):
            if last_e >= xs[ii][0] - 1:
                last_e = max(last_e, xs[ii][1])
            else:
                break

        if last_e != mx:
            ans_x = last_e + 1
            break