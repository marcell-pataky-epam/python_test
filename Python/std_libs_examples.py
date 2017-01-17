import os
import glob
import re
import math
import random
import statistics
from urllib.request import urlopen
# import smtplib
from datetime import date

print(os.getcwd())
print(dir(os))

print('-' * 40)

print(glob.glob('*.py'))

print('-' * 40)

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print('tea for too'.replace('too', 'two'))

print('-' * 40)

print(math.cos(math.pi / 4))
print(math.log(1024, 2))

print('-' * 40)

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

print('-' * 40)

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

print('-' * 40)

with urlopen('http://index.hu') as response:
    for line in response:
        line = line.decode('utf-8')
        if '<div>' in line:
            print(line)

# server = smtplib.SMTP('localhost')
# server.sendmail('pythoncode@python.com', 'tamas_csako@epam.com', """Message.""")
# server.quit()

print('-' * 40)

now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1983, 3, 25)
age = now - birthday
print(age.days)
