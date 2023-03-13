123 + 222
#345
1.5 * 4
#6.0
2 ** 100
#1267650600228229401496703205376
len(893)
#TypeError: object of type 'int' has no len()
len("893")
#3
len([2, 3, 4, 5])
#4
len(str(2 ** 1000000))
#301030
import math
#
Math.pi
#NameError: name 'Math' is not defined
math.sqrt(85)
#9.219544457292887
import random
#
random.random()
0.991242077379264
random.choice([1, 2, 3, 4])
#NameError: name 'random' is not defined
st = 'Spam'
#
len(st)
#4
st[0]
#'S'
st[-1]
#'m'
st[1:3]
#'pa'
st[1:]
#'pam'
st[:]
#'Spam'
st + "Hola"
#'SpamHola'
st * 5
#'SpamSpamSpamSpamSpam'
st[0] = 'z'
''' inmutabilidad los strings no cambian de valor como las # listas
TypeError: 'str' object does not support item assignment'''
st = 'z' + st[1:]
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'st' is not defined'''
print(st)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'st' is not defined
'''

S = 'shrubbery'
#
L = list(S)
#
L
#['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
L[1] = 'c'
''.join(L)
#'scrubbery'
B = bytearray(b'spam')
B.extend(b'eggs')
B
#bytearray(b'spameggs')
B.decode()
#'spameggs'

S = 'Spam'
#
S.find('pa')
#1
S
#'Spam'
S.replace('pa', 'XYZ')
#'SXYZm'
S
#'Spam'

line = 'aaa,bbb,ccccc,dd'
line.split(',')
# ['aaa', 'bbb', 'ccccc', 'dd']
S = 'spam'
S.upper()
#'SPAM'
S.isalpha() # Content tests: isalpha, isdigit, etc.
#True
line = 'aaa,bbb,ccccc,dd\n'
line.rstrip()
line.rstrip().split(',')
# 'aaa,bbb,ccccc,dd'
# ['aaa', 'bbb', 'ccccc', 'dd']
'%s, eggs, and %s' % ('spam', 'SPAM!')
#'spam, eggs, and SPAM!'
'{0}, eggs, and {1}'.format('spam', 'SPAM!')
#'spam, eggs, and SPAM!'
'{}, eggs, and {}'.format('spam', 'SPAM!')
#'spam, eggs, and SPAM!'
f'{S}, eggs, and {line}'
#NameError: name 'S' is not defined
dir(S) # S es un string
#NameError: name 'S' is not defined
help(S.replace)
#NameError: name 'S' is not defined
S = 'A\nB\tC'
#
len(S)
#5
ord('\n')
#10
S = 'A\0B\0C'
#
len(S)
#5
S
#'A\x00B\x00C'
msg = """
aaaaaaaaaaaaa
Strings | 105bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc
"""
msg
#'\naaaaaaaaaaaaa\nStrings | 105bbb\'\'\'bbbbbbbbbb""bbbbbbb\'bbbb\ncccccccccccccc\n'
color = input("Introduce el color de tu camisa?: ")
print(color)
#Introduce el color de tu camisa?: AZul
#AZul
n = int(input("Cuantas camisas tienes?: "))
print(n)
#Cuantas camisas tienes?: 2
#2
price = float(input("Cuanto costo la mas bonita?: "))
print(price)
#Cuanto costo la mas bonita?: 100
#100.0

import re
match = re.match('Hello[ \t]*(.*)world', 'Hello')
match.group(1)
#AttributeError: 'NoneType' object has no attribute 'group'

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
match.groups()
re.split('[/:]', '/usr/home/lumberjack')
#NameError: name 're' is not defined

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('My number is 415-555-4242.')
print(f'Phone number found: {mo.group()}')
#NameError: name 're' is not defined

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
mo.group()
#NameError: name 're' is not defined

hero_regex = re.compile (r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
mo1.group()
mo2 = hero_regex.search('Tina Fey and Batman.')
mo2.group()
#NameError: name 're' is not defined