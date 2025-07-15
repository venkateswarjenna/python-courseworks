Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
n='venky'
'e' in n
True
'i' in n
False
'o' in n
False
'o' in n
False
names=['venky','sangee','ritu','rushi']
'venky' in name
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    'venky' in name
NameError: name 'name' is not defined. Did you mean: 'names'?
>>> 'venky' in names
True
>>> 'rajani' in names
False
>>> 'rushi' in names
True
>>> s={1,2,3,4,5}
>>> 2 in s
True
>>> 6 in s
False
>>> 3 in s
True
>>> t=(1,2,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> t=(1,2,3)
>>> 4 in t
False
>>> data={'name':'sandy','batch':30,'domain':'py'}
>>> 'age' in data
False
>>> 
>>> 'name' in data
True
>>> names
['venky', 'sangee', 'ritu', 'rushi']
>>> 'tarak' not in names
True
>>> 'sandy' not in names
True
>>> v='aeiou'
>>> n
'venky'
>>> 'v' in v
False
>>> 'e' in v
True
>>> 'n' not in v
True
