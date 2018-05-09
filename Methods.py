Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> spam = ['hello','hi','howdy','heayh']
>>> spam.index('hello')
0
>>> spam.index('hi')
1
>>> spam.append('lol')
>>> spam
['hello', 'hi', 'howdy', 'heayh', 'lol']
>>> spam.insert(1,'hellow')
>>> spam
['hello', 'hellow', 'hi', 'howdy', 'heayh', 'lol']
>>> 

>>> del spam[1]
>>> spam
['hello', 'hi', 'howdy', 'heayh', 'lol']
>>> 

>>> spam.sort()
>>> spam
['heayh', 'hello', 'hi', 'howdy', 'lol']
>>> 
