from functools import cmp_to_key

with open('sample.in', 'r') as file:
    data = file.read().split('\n\n')

I = lambda x:isinstance(x, int)
L = lambda x:isinstance(x, list)

def cmp(l, r):
    if I(l) and I(r):
        if l < r: return -1
        return l > r
    if L(l) and L(r):
        for ii in range(min(len(l), len(r))):
            c = cmp(l[ii], r[ii])
            if c: return c
        return cmp(len(l), len(r))
    if I(l) and L(r):
        return cmp([l], r)
    if L(l) and I(r): 
        return cmp(l, [r])

p = []
n = 0
for ii, ss in enumerate(data):
    l, r = [eval(x) for x in ss.split()]
    if cmp(l, r) <= 0: n += ii + 1
    p.append(l); p.append(r)

p.append([[2]]); p.append([[6]])

p.sort(key = cmp_to_key(cmp))

print(str(n))