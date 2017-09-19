words = [
    'look',
    'into',
    'my',
    'eyes',
    'look',
    'into',
    'my',
    'eyes',
    'the',
    'eyes',
    'the',
    'eyes',
    'the',
    'eyes',
    'not',
    'around',
    'the',
    'eyes',
    "don't",
    'look',
    'around',
    'the',
    'eyes',
    'look',
    'into',
    'my',
    'eyes',
    "you're",
    'under',
]

from collections import Counter

word_counts = Counter(words)
print(word_counts)
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})

top_three = word_counts.most_common(3)
print(top_three)
# [('eyes', 8), ('the', 5), ('look', 4)]

print(word_counts['not'])  # 1
print(word_counts['eyes'])  # 8

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])  # 9

word_counts.update(morewords)
print(word_counts)
# Counter({'eyes': 10, 'my': 5, 'the': 5, 'look': 4, 'into': 3, 'not': 3, 'around': 2, 'why': 2, 'are': 2, 'you': 2, 'looking': 2, 'in': 2, "don't": 1, "you're": 1, 'under': 1})



a = Counter(words)
b = Counter(morewords)
print("a = {}".format(a))
print("b = {}".format(b))

# Combine counts
c = a + b
print("c = a + b = {}".format(c))

# Subtract counts
d = a - b
print("d = a - b = {}".format(d))

print("{{'a':1, 'b':1}} - {{'c':1, 'd':1}} = {}".format(Counter({'a': 1, 'b': 1}) - Counter({'c': 1, 'd': 1})))
print("{{'a':1, 'b':1}} - {{'a':2, 'd':1}} = {}".format(Counter({'a': 1, 'b': 1}) - Counter({'a': 2, 'd': 1})))

e = Counter({'a': 2, 'b': 3})
print("e = {}".format(e))
e['a'] -= 10
print("e = {}".format(e))
print(list(e.elements()))

print(e - Counter({'a': 10}))
