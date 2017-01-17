words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w)

print('-----------------------')

words.append('door')

for w in words:
    print(w)

print('-----------------------')

new_words = ['fork', 'knife', 'spoon']
words.extend(new_words)

for w in words:
    print(w)

print('-----------------------')

words.insert(0, 'dog')

for w in words:
    print(w)

print('-----------------------')

words.remove('window')

for w in words:
    print(w)

print('-----------------------')

print(words.pop())

print('-----------------------')

for w in words:
    print(w)

print('-----------------------')

print(words.count('nothing'))

print('-----------------------')

words.sort(key=str.upper, reverse=False)

for w in words:
    print(w)

print('-----------------------')

words.reverse()

for w in words:
    print(w)

print('-----------------------')

del words[0:2]

for w in words:
    print(w)

print('-----------------------')

