Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s=set()
>>> s={1,2,3,4,5,6}
>>> s
{1, 2, 3, 4, 5, 6}
>>> s={1,2,3,"Venky".capitalize(1,2,3),3+8j}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s={1,2,3,"Venky".capitalize(1,2,3),3+8j}
TypeError: str.capitalize() takes no arguments (3 given)
>>> s={1,2,3,"Venky",(1,2,3),3+8j}
>>> class={"arun","gopal","sumith","venky","shivani","rasmitha"}
SyntaxError: invalid syntax
>>> class30={"arun","gopal","sumith","venky","shivani","rasmitha"}
>>> class30
{'venky', 'gopal', 'arun', 'shivani', 'sumith', 'rasmitha'}
>>> arun in class30
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    arun in class30
NameError: name 'arun' is not defined
>>> "arun" in class30
True
>>> "sahas" not in class30
True
