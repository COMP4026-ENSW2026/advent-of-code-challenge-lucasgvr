with open('sample.in', 'r') as file:
    data = file.read()

def can_go(g, p1, p2):
    return(p2 in g and 
    ((g[p1] == 'E' and g[p2] in 'yz') or 
    (g[p2] == 'S' and g[p1] in 'ab') or 
    (g[p2] != "S" and g[p1] != "E" and ord(g[p1]) - ord(g[p2]) <= 1)))

grid = {x + y * 1j: h for y, line in enumerate(data.split('\n'))
                        for x, h in enumerate(line)}

start = [p for p, h in grid.items() if h == 'S'][0]
end = [p for p, h in grid.items() if h == 'E'][0]

distance = {end: 0}
queue = [end]
while queue:
    p1 = queue.pop(0)
    for p2 in [p1 - 1, p1 + 1, p1 + 1j, p1 - 1j]:
        if p2 not in distance and can_go(grid, p1, p2):
            distance[p2] = distance[p1] + 1 
            queue.append(p2) 

short_dist = sorted(distance[p] for p in distance if grid[p] in "Sa")[0]            

print(str(short_dist))