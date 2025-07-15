Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t=tuple()
t=(1,2,3,"venky")
t
(1, 2, 3, 'venky')
t[4]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
t[3]
'venky'
t[:5]
(1, 2, 3, 'venky')
t[:4]
(1, 2, 3, 'venky')
t[3]
'venky'
t[:3]
(1, 2, 3)
t=(1,2)
t1=(4,5)
t+t1
(1, 2, 4, 5)
t
(1, 2)
t*3
(1, 2, 1, 2, 1, 2)
t[0:2]*2
(1, 2, 1, 2)
t=(1,2,3,4)
t
(1, 2, 3, 4)
4 in t
True
6 not in t
True
7 in t
False
t
(1, 2, 3, 4)
a,b,c=a
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a,b,c=a
NameError: name 'a' is not defined
a,b,c=t
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a,b,c=t
ValueError: too many values to unpack (expected 3)
t=(1,2,3,4)
a,b,c=t
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a,b,c=t
ValueError: too many values to unpack (expected 3)
>>> t=(1,2,3,4)
>>> a,b,c,d=t
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> res=('venky','vjenna@gmail','venk123')
>>> name,gmail,pwd=res
>>> name
'venky'
>>> gmail
'vjenna@gmail'
>>> pwb
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    pwb
NameError: name 'pwb' is not defined. Did you mean: 'pwd'?
>>> pwd
'venk123'
>>> r=(1,13,6,7,5,4,8,6,9,7)
>>> r.count(6)
2
>>> r
(1, 13, 6, 7, 5, 4, 8, 6, 9, 7)
>>> lrn(r)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    lrn(r)
NameError: name 'lrn' is not defined. Did you mean: 'len'?
>>> len(r)
10
>>> max(t)
4
>>> min(t)
1
>>> sum(r)
66
t[5].append930
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[5].append930
IndexError: tuple index out of range
t
(1, 2, 3, 4)
t.append[3]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t.append[3]
AttributeError: 'tuple' object has no attribute 'append'
r.append930
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    r.append930
AttributeError: 'tuple' object has no attribute 'append930'
t.append(3)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    t.append(3)
AttributeError: 'tuple' object has no attribute 'append'
r.append(3)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    r.append(3)
AttributeError: 'tuple' object has no attribute 'append'
r[5].append(3)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    r[5].append(3)
AttributeError: 'int' object has no attribute 'append'
d=[('name','venky',),('mail','venky@gmail'),('pwd','venky123')]
dict(d)
{'name': 'venky', 'mail': 'venky@gmail', 'pwd': 'venky123'}
(2025,03,07)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers



d=dict()
d={}
d={'name':'Venky','mail':'venky@gmail.com','batch':'30','phone':,'7032176972'}
SyntaxError: expression expected after dictionary key and ':'
d={'name':'Venky','mail':'venky@gmail.com','batch':'30','phone':'7032176972'}
d{name}
SyntaxError: invalid syntax
d['name']
'Venky'
d.get('age')
d.get('batch')
'30'
d.get('age','Age is not heare')
'Age is not heare'
d.get('batch','batch is not heare')
'30'
AttributeError: 'int' object has no attribute 'append'
SyntaxError: invalid syntax
d
{'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972'}
d['gender']='male'
d
{'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972', 'gender': 'male'}
d['course']='pfs'
d
{'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972', 'gender': 'male', 'course': 'pfs'}
age=d['pop']='age'
d
{'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972', 'gender': 'male', 'course': 'pfs', 'pop': 'age'}
d.popiteam()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    d.popiteam()
AttributeError: 'dict' object has no attribute 'popiteam'. Did you mean: 'popitem'?
d.popitam()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    d.popitam()
AttributeError: 'dict' object has no attribute 'popitam'. Did you mean: 'popitem'?
d.popitem()
('pop', 'age')
d
{'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972', 'gender': 'male', 'course': 'pfs'}
d.clear()
d
{}
d={'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972', 'gender': 'male'}
d.get('name','name is not heare')
'Venky'
d.key()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
d.keys()
dict_keys(['name', 'mail', 'batch', 'phone', 'gender'])
d.values()
dict_values(['Venky', 'venky@gmail.com', '30', '7032176972', 'male'])
d.items()
dict_items([('name', 'Venky'), ('mail', 'venky@gmail.com'), ('batch', '30'), ('phone', '7032176972'), ('gender', 'male')])
d.update(('key1':123,'key2':456))
SyntaxError: invalid syntax

d
{'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972', 'gender': 'male'}
d.update({'key1':123,'key2':456})
d
{'name': 'Venky', 'mail': 'venky@gmail.com', 'batch': '30', 'phone': '7032176972', 'gender': 'male', 'key1': 123, 'key2': 456}
d.get('batch','batch is not here')
'30'
