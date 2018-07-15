### upper() lower()

spam = 'hello world'

spam.upper()

###

answer = input()
yes

###

if answer == 'yes':
    print('Play again')

answer == 'yes'
False

answer.lower() == 'yes':
    print('Play again')
    
Play again

### isupper() islower()  boolean value

spam = 'Hello world'
spam.islower()
False

###

12345.islower()
False

'Hello'.upper().isupper()
True

###

isalpha() - letters only
isalnum() - letters and numbers only
isdecimal() - numbers only
isspace() - whitespace only
istitle() - titlecase only

'Hello world'.isspace()
False
'Hello world'[5].isspace()
True
'Hello world'[5]
' '


'This Is Title Case'.istitle()
True

###

startwith()
endswith()


'Hello world'.startwith('Hello')
True

'Hello world'.endswith('d')
True

###

join() 

','.join(['cats', 'rats', 'bats'])
'cats,rats,bats'


print('\n\n'.join(['cats', 'rats', 'bats'])
cats

rats

bats

###

      
split()

'My name is Simon'.split()
['My', 'Name', 'is', 'Simon']


'My name is Simon'.split('m')
['My na', 'e is Si', 'on']


###

ljust()
rjust()

'Hello'.rjust(10)
'     Hello'

len('     Hello')
10

'Hello'.ljust(10)
'Hello     '


'Hello'.rjust(20,%)
'%%%%%%%%%%%%%%%Hello'  

###     

center()

'Hello'.center(20)
'       Hello        '
'Hello'.center(20,'-')
'-------Hello--------'


###
      
strip()
rtrip()
lstrip()

'Hello'.rjust(10)
'     Hello'
    spam = 'Hello'.rjust(10)
    spam.strip()
'Hello'
Spam
'     Hello'
Spam = spam.strip()
'Hello'

###

replace()

spam = 'Hello there!'
spam.replace('e', 'XYZ')

'HXYZllo thXYZrXYZ!'

      
### The pyperclip Module

win+r > cmd > "\Program Files\Python 3.5\Scipts" pip.exe install pyperclip

pyperclip.copy()
pyperclip.paste()















      


















