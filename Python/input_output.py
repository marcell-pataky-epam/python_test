for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).center(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x * x * x).ljust(4))

print('-' * 40)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('-' * 40)

print('12'.zfill(10))

print('-' * 40)

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

print('-' * 40)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
