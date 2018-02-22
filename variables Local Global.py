spam = 42 # global variable

def eggs():
    spam = 42 # loacal variable

print('Some code here')
print('Some code here')


#######

def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
