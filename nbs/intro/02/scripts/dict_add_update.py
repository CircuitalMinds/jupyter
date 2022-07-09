d = {'k1': 1, 'k2': 2}

d['k3'] = 3
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}

d['k1'] = 100
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}

d1.update(d2)
print(d1)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}
d3 = {'k5': 5, 'k6': 6}

# d1.update(d2, d3)
# TypeError: update expected at most 1 arguments, got 2

d1.update(**d2, **d3)
print(d1)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}
d3 = {'k5': 5, 'k6': 6}

# d3.update(**d1, **d2)
# TypeError: dict.update() got multiple values for keyword argument 'k1'

d1 = {'k1': 1, 'k2': 2}
d2 = {'k3': 3, 'k4': 4}

print({**d1, **d2})
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

print(dict(**d1, **d2))
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

d1 = {'k1': 1, 'k2': 2}
d2 = {'k1': 100, 'k3': 3, 'k4': 4}

print({**d1, **d2})
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

# print(dict(**d1, **d2))
# TypeError: dict() got multiple values for keyword argument 'k1'

d = {'k1': 1, 'k2': 2}

d.update(k1=100, k3=3, k4=4)
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

d = {'k1': 1, 'k2': 2}

d.update([('k1', 100), ('k3', 3), ('k4', 4)])
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

d = {'k1': 1, 'k2': 2}

keys = ['k1', 'k3', 'k4']
values = [100, 3, 4]

d.update(zip(keys, values))
print(d)
# {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}

d = {'k1': 1, 'k2': 2}

# d.update(k3=3, k3=300)
# SyntaxError: keyword argument repeated: k3

d = {'k1': 1, 'k2': 2}

d.update([('k3', 3), ('k3', 300)])
print(d)
# {'k1': 1, 'k2': 2, 'k3': 300}

d = {'k1': 1, 'k2': 2}

keys = ['k3', 'k3']
values = [3, 300]

d.update(zip(keys, values))
print(d)
# {'k1': 1, 'k2': 2, 'k3': 300}
