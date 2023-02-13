with open('sample.in', 'r') as file:
    data = file.read().splitlines()

monkeys = {} 

while 'root' not in monkeys:
    for ll in data:
        m = ll[:4]
        if len(ll) > 8: m1, m2 = ll[6:10], ll[13:]
        try:
            if '+' in ll: monkeys[m] = monkeys[m1] + monkeys[m2] 
            elif '-' in ll: monkeys[m] = monkeys[m1] - monkeys[m2] 
            elif '*' in ll: monkeys[m] = monkeys[m1] * monkeys[m2] 
            elif '/' in ll: monkeys[m] = monkeys[m1] // monkeys[m2] 
            else: monkeys[m] = int(ll[6:])
        except (KeyError, TypeError): pass

for ll in data: monkeys[ll[:4]] = ll[6:]
del monkeys['humn']
equation = monkeys.pop('root').replace("+", "=")
while any([k in equation for k in monkeys]):
    for m in monkeys:
        if m in equation:
            equation = equation.replace(m, '(' + monkeys[m] + ')')

equation = equation.replace('=', '- (') + ')'
c = eval(equation.replace('humn', '-1j'))
r2 = round(c.real / c.imag)

print(str(r2))