eggs = {'name': 'Zophie', 'spacies': 'cat', 'age', 8}
ham = {'spacies': 'cat', 'name': 'Zpophie', 'age', 8}

eggs == ham
### TRUE

'name' in eggs
### TRUE

'name' not in eggs
### FALSE

list(eggs.keys())
['name', 'spacies', 'age']

list(eggs.values())
['Zophie', 'cat', 'age']

list.(eggs.items())
[('name','Zophie'),('species','cat'),('age',8)]

### Fot loop

for k in eggs.keys():
    print(k)

name
species
age

for v in eggs.values():
    print(v)

Zophie
cat
8

for k, v in eggs.items():
    print(k,v)

name Zophie
species cat
age 8

for i in eggs.items():
    print(i)


### Tuples
('name', 'Zophie')
('species' 'cat')
('age', 8)
###


### if value of key 'age' does not exist return 0
eggs.get('age', 0)
8

eggs.get('color', '')
''


###

picnicItems = {'apples': 5, 'coups': 2}
print('I am brining ' +str(picnicItems.get('napkins', 0) + ' to the picnic.')
# I am brining 0 to the picnic.



### setdefault()

if 'color' not in egss:
      eggs['color'] = 'black'
...............................
eggs.setdefault('color', 'black') ### only if not exists


###

























###

