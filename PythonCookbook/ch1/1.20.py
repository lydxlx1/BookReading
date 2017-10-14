"""
1.20. Combining Multiple Mappings into a Single Mapping

Problem
YOu have multiple dictionaries or mappings that you want to logically combine into a
single mapping to perform certain operations, such as looking up values or checking
for the existence of keys.

Solution
Suppose you have two dictionaries:
"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

"""
Now suppose you want to perform lookups where you have to check both dictionaries
(e.g., first checking in a and then in b if not found). An easy way to do this is to use the
ChainMap class from the collections module. For example:
"""

c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])

"""
Disscusion

A ChainMap takes multiple mappings and makes them logically appear as one. However,
the mappings are not literally merged together. Instead, a ChainMap simply keeps a list
of the underlying mappings and redefines common dictionary operations to scan the
list. Most operations will work. For example:
"""
print(len(c))
print(list(c.keys()))
print(list(c.values()))

"""
If there are duplicate keys, the value from the first mapping get used. Thus, the entry
c['z'] in the example would always refer to the value in dictionary a, not the value in
dictionary b.

Operations that mutate the mapping always affect the first mapping listed. For example:
"""
c['z'] = 10
c['w'] = 40
del c['x']
print(a)

try:
    del c['y']
except Exception as err:
    print(err)

"""
A ChainMap is particularly useful when workign with scoped values such as variables in
a programming language (i.e., globals, locals, etc.). In fact, there are methods that make
this easy:
"""
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)

# Discard last mapping
values = values.parents
print(values['x'])

# Discard last mapping
values = values.parents
print(values['x'])

print(values)

"""
As an alternative to ChainMap, you might consider merging dictionaries together using
the update() method. For example:
"""
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
print(merged)

"""
This works, but it requires you to make a completely separate dictionary object (or
destructively alter one of the existing dictionaries). Also, if any of the original dictionaries
mutate, the changes don't get reflected in the merged dictionary. For example:
"""
a['x'] = 13
print(a)
print(merged)

"""
A ChainMap uses the original dictionaries, so it doesn't have this behavior. For example:
"""
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = ChainMap(a, b)
print('merged = {merged}'.format_map(vars()))
a['x'] = 42
print('a = {a}, merged = {merged}'.format_map(vars()))
