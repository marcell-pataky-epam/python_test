tel = {'jack': 1234, 'brigitte': 3452}

print(tel)

print('-' * 40)

print(sorted(tel.keys()))

print('-' * 40)

tel['guido'] = 4127

print('guido' in tel)

print('-' * 40)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print('-' * 40)

squares = {x: x**2 for x in range(1, 10, 1)}

print(squares)

print('-' * 40)

for n, sq in squares.items():
    print(n, sq)

print('-' * 40)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print('-' * 40)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print('-' * 40)

for i in reversed(range(1, 10, 2)):
    print(i)

print('-' * 40)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

