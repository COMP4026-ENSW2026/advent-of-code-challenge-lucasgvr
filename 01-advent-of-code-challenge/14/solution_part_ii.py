with open('sample.in', 'r') as file:
    data = file.read().strip()

def interpolate(start, end):
    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            yield x1, y

    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            yield x, y1

def parse(data): 
    grid = dict()
    bottom = 0

    for line in data.splitlines():
        coords = line.split(' -> ') 
        coords = [tuple(int(c) for c in coord.split(',')) for coord in coords] 

        for start, end in zip(coords, coords[1:]): 
            for pos in interpolate(start, end): 
                grid[pos] = '#'
                if pos[1] > bottom:
                    bottom = pos[1] 

    return grid, bottom

def drop_sand(grid, src, bottom):
    x, y = src

    while y < bottom:
        for move in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]: 
            if move not in grid: 
                x, y = move
                break
        else:
            return True, (x, y) 

    return False, (x, y)

def part1(grid):
    grid, bottom = grid
    grid = grid.copy()

    src = (500, 0)
    cnt = 0

    while True:
        has_stopped, pos = drop_sand(grid, src, bottom)
        if not has_stopped:
            break
        grid[pos] = 'o'
        cnt += 1

    return cnt

def part2(grid):
    grid, bottom = grid

    src = (500, 0)
    cnt = 0

    while True:
        _, pos = drop_sand(grid, src, bottom + 1)
        grid[pos] = 'o'
        cnt += 1
        if pos == src:
            break

    return cnt

print(str(part2(parse(data))))