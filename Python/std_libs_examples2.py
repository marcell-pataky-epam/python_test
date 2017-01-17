import reprlib
import pprint
import textwrap
from string import Template

print(reprlib.repr(set('supercalifragilisticexpialidocious')))

print('-' * 40)

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=50)

print('-' * 40)

doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with
newlines to separate the wrapped lines."""

print(textwrap.fill(doc, width=40))

print('-' * 40)

t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))
