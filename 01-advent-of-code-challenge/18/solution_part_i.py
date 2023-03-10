from collections import deque

Cubes = []
with open('sample.in', 'r') as file:
    for ll in file:
        Line = ll.strip()
        x, y, z = list(map(int, Line.split(",")))
        coord_tuple = (x, y, z)
        Cubes.append(coord_tuple)

CubesSet = set(Cubes)

AdjCoords = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

total_sa = 0
for x, y, z in Cubes:
    default_sa = 6
    for dx, dy, dz in AdjCoords:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) in CubesSet: 
            default_sa -= 1
    total_sa += default_sa

print(str(total_sa))

minx, miny, minz = 50, 50, 50
maxx, maxy, maxz = 0, 0, 0
for x, y, z in Cubes: 
    if x > maxx:
        maxx = x
    if x < minx:
        minx = x
    if y > maxy:
        maxy = y
    if y < miny:
        miny = y
    if z > maxz:
        maxz = z
    if z < minz:
        minz = z

Cube1 = (minx - 1, miny - 1, minz - 1)
ExtCubes = []
ExtCubesSet = set()
ExtCubesSet.add(Cube1)

QueueCubes = deque()
QueueCubes.append(Cube1)
while QueueCubes:
    NextCube = QueueCubes.popleft()
    x, y, z = NextCube

    ExtCubes.append(NextCube)

    for dx, dy, dz in AdjCoords:
        nx, ny, nz = x + dx, y + dy, z + dz
        if nx < minx - 1 or nx > maxx + 1 or ny < miny - 1 or ny > maxy + 1 or nz < minz - 1 or nz > maxz + 1:
            continue
        ThisCube = (nx, ny, nz)
        if ThisCube in CubesSet or ThisCube in ExtCubesSet:
            continue
        QueueCubes.append(ThisCube)
        ExtCubesSet.add(ThisCube)

total_ext_sa = 0
for x, y, z in ExtCubes:
    default_sa = 0
    for dx, dy, dz in AdjCoords:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) in CubesSet:
            default_sa += 1
    total_ext_sa += default_sa