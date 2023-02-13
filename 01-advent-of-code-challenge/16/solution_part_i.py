import collections as c, itertools, re, functools

r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

V, F, D = set(), dict(), c.defaultdict(lambda: 1000)

for v, f, us, in re.findall(r, open('sample.in').read()):
    V.add(v)
    if f != '0': F[v] = int(f) 
    for u in us.split(', ') : D[u, v] = 1

for k, i, j in itertools.product(V, V, V):
    D[i, j] = min(D[i, j], D[i, k] + D[k, j])

def search(t, u = 'AA', vs = frozenset(F), e = False):
    tt = max([F[v] * (t - D[u, v] - 1) + search(t - D[u, v] - 1, v, vs - {v}, e)
    for v in vs if D[u, v] < t] + [search(26, vs = vs) if e else 0])
    return tt

print(str(search(30)))