>>> supplies = ['pens', 'flame-throwers', 'binders', 'staplers']
	      
>>> for i in range(len(supplies)):
	      print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

	      
Index 0 in supplies is: pens
Index 1 in supplies is: flame-throwers
Index 2 in supplies is: binders
Index 3 in supplies is: staplers
>>>



### Multiple assigment

>>> cat = ['fat' , 'orange', 'loud']
	      
>>> size = cat[0]
	      
>>> color = cat[1]
	      
>>> disposition = cat[2]
	      
>>> ### the same
	      
>>> size, color, disposition = cat
	      
>>> size
	      
'fat'
>>>

>>> ### Swapping Varibles
	      
>>> 
	      
>>> a = 'AAA'
	      
>>> b = 'BBB'
	      
>>> a, b = b, a
	      
>>> a
	      
'BBB'
>>> b
	      
'AAA'

>>> ### Augmented Assigment operators
	      
>>> spam = 42
	      
>>> spam += 1
	      
>>> spam
	      
43
>>> 
