Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Hello, python world!")
Hello, python world!
>>> print("hello")
hello
>>> hello, python world!print("hello, python world!")
SyntaxError: invalid syntax
>>> 
>>> print("hello')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> hello
...       
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> no
...       
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    no
NameError: name 'no' is not defined
>>> Hello
...       
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Hello
NameError: name 'Hello' is not defined
>>> print('Marty's book')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("marty's books")
...       
marty's books
>>> print('marty\'s book')
...       
marty's book
