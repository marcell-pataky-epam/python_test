import json

f = open('example.json', 'w')

print(json.dumps([1, 'simple', 'list']))

json.dump([1, 'simple', 'list'], f)

f.close()

f = open('example.json', 'r')

x = json.load(f)

print(x)

f.close()
