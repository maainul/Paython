
```
1.Variables,expressions and statements
2.Conditional Execution
3.Function
4.Iteration
5.String
6.Files
7.List
8.Dictonaries
9.Tuples
10.Regular Expressions

```
# ##Largest and smallest value
```.py
largest=None
print('Before:',largest)
for num in [3,41,12,9,74,15]:
	if largest is None or num >largest:
		largest=num
		#print('Loop:',num,largest)
print('largest:',largest)

```
```.py
smallest=None
print('Before:',smallest)
for num in [3,41,12,9,74,15]:
	if smallest is None or num <smallest:
		smallest=num
print('largest:',smallest)
```

# ##FUNCTIONS
```.py

	type(32)
	<class 'int'>
	type('32')
	<class 'string'>
	max('mainul')
	'u'
	min(mainul)
	'a'
	len('mainul')
	6
	int(3.999)
	3
	int(-9.098)
	9
	float(32)
	32.0
	float('3.1416')
	3.1416
	str(32)
	'32'
	str(3.14)
	'3.14'
	random.randint(5,10)
	5
	random.randint(5,10)
	6
	random.randint(5,10)
	9
```
## Random Number
```.py
for i in range(10)
	x=random.random()
	print(x)
```
```.py
	t=[1,2,3,4]
	random.choice(t)
	3
	random.choice(t)
	2
	random.choice(t)
	1
```
## Adding new functions
```.py
def print_lyrics():
print("I'm a lumberjack, and I'm okay.")
print('I sleep all night and I work all day.')
```	
```.py
	def addtwo(a,b)
	added=a+b
	return added
	x=addtwo(3,5
	print(x)
```
# ##STRINGS

A string is a sequence of characters

1.Sting decleration:
```.py
	fruit='banana'
	print(fruit)
```
2.Index of strings:
```.py	
	print(fruit[0])
	b
	print(fruit[1])
	a
```
3.Length of strings:
```.py
	length=len(fruit) #Declear length variable 
			   for store result of len function
	print(length)
```
4.Last alphabet of String:
```.py
	last=fruit[len(fruit)-1]
	print(last)
```
5.Traversal through a string with while loop:
```.py
	fruit='banana'
	print(fruit)
	index=0
	while index<len(fruit):
    	letter=fruit[index]
    	print(letter)
    	index=index+1
```
```
    banana
    b
    a
    n
    a
    n
    a
```
```.py
fruit = 'banana is banana'
for char in fruit:
	print(char)
```
### String are immutable
```.py
greeting = 'Hello,World'
greeting[0]='j'
greeting = 'Hello,World'
new_greeting='j'+greeting[1:]
print(new_greeting)
```
```
#TypeError: 'str' object does not support item assignment
jello,World
```
### Looping and Counting
Count the number of times letter appears in a string
```.py
word='banana'
count=0
for letter in word:
	if letter == 'n':
		count=count+1
print(count)
```
### The in Operator
Search the value if the first operator is substring in the second
```.py
	fruit='banana'
	s1='a' in fruit
	print(s1)
	s2='seed' in fruit
	print(s2)
```
```	True
	False
```
### Comparing Two string 
```.py
word='pineapple'
if word =='banana':
	print('banana')
else:
	print('pineapple')

	word='pineapple'
if word <'banana':
	print('Your word, '+word+ ' come before banana')
elif word>'banana':
	print('your word '+word+ ' come after banana')
else:
	print('all right banana')
```
### String Methods
```.py
	stuff='Hello world'
	print(type(stuff))
	print(dir(stuff))
```
```
<class 'str'>

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
```.py
	stuff='Hello world'
	print(stuff.upper()) #Upper case letter:
	print(stuff.lower()) #Lowler case letter:
```
	HELLO WORLD
	hello world
```.py
	word='banana'
	index=word.find('na') #Find index number:
	print(index)
```
```.py
	line=' Here we go'
	print(line.strip()) #Remove whitespace from the beginning and end of a string
	print(line.startswith('h'))#Check stars with lower case h or not.
```
```
Here we go
False
```
# ##FILES
## Opening a file
```.py
	fhand=open('mbox.txt')
	printf(fhand)
```
## Reading files
```.py
	fhand=open('mbox-short.txt')
	count=o
	for line in fhand:
		count=count+1
	print('line count',count)
```
```.py
	fhand=open('mbox-short.txt')
	inp=fhand.read()
	print(len(inp))
	print(inp[:20])
```
## Searcing through a file
```.py
	fhand=open('mbox-short.txt')
	for line in fhand:
		line=line.rstrip()
		if line.startswith('From:')
	print(line)
```
```
	When this program runs, we get the following output:
	From: stephen.marquard@uct.ac.za

	From: louis@media.berkeley.edu
	
	From: zqian@umich.edu
	
	From: rjlowe@iupui.edu
```
```.py
	fhand=open('mbox-short.txt')
	for line in fhand:
		line=line.rstrip() #For rstrip() function no space will not be printed
		if line.startswith('From:')
		print(line)
```
```
	When this program runs, we get the following output:
	From: stephen.marquard@uct.ac.za
	From: louis@media.berkeley.edu
	From: zqian@umich.edu
	From: rjlowe@iupui.edu
```
```.py
	fhand=open('mbox-short.txt')
	for line in fhand:
		line=line.rstrip()
		#skip uninteresting lines
		if not line.startswith('From:')
			continue
		#process intersting lines
		print(line)
```
## Find method
```.py
	fhand=open('mbox-short.txt')
	for line in fhand:
		line=line.rstrip()
		if line.find('@uct.ac.za')==-1:
			continue
		print(line)
```
```
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
X-Authentication-Warning: set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan 4 07:02:32 2008
X-Authentication-Warning: set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
```
## Letting the user choose the file name
```.py
	fname=input('Enter the file name')
	fhand=open(fname)
	count=0
	for line in fhand:
	if line.startswith('Subject:')
		count=count+1
	print('There were' ,count,'subjects in'fname)
```
```
	python search6.py
	Enter the file name: mbox.txt
	There were 1797 subject lines in mbox.txt

	python search6.py
	Enter the file name: mbox-short.txt
	There were 27 subject lines in mbox-short.txt
```
## Using try, except, and open
```.py
	fname=input('Enter the file name:')
	try:
		fhand=open(fanme)
	except:
		print('File cannot be opend',fname)
		exit()
	count=0
	for line in fhand:
		if line.startswith('Subject'):
			count=count+1
		print('There are ',count ,'subject line in',fanme)
```
```
python search6.py
Enter the file name: missing.txt
Traceback (most recent call last):
File "search6.py", line 2, in <module>
fhand = open(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```
## Writing files
```.py
	fout=open('output.txt')
	print(fout)
	line='This is a little water'
	print(fout.write(line))
	line1='This is a little'
	print(fout.write(line1))
	fout.close()
```


# ##LISTS
```
##A list is a sequence of values.
##List can be any type
##The values in list are called elements
	[10,20,30,40]
	[fog,dog,rat]
```
```.py
	cheeses=['dog','fog','not']
	numbers=[12,14]
	empty=[]
	print(cheeses,numbers,empty)
```
```
	'dog','fog','not',12,14,[]
```
## List operaton
```.py
	a=[1,2,3]
	b=[4,5,6]
	c=a+b
	print(c)
```
```
	[1,2,3,4,5,6]
```
## List slices
```.py
	t=['a','b','c','d','e']
	t=[1:3]
	['b','c']
	t=[:4]
	t=['a','b','c','d']
	t=[4:]
	t=['b','c','d','e']
	t=[:]
	t=['a','b','c','d','e']
	t=[1:3]=['x','y']
	print(t)
	t=['a','x','y','b','c','d','e']

```


## List methods
```.py
	t=['a,'b,'c']
	t.append('d')#append adds new element to the end of a list
	print(t)
```
```
	['a','b','c','d']

```
```.py
	t1=['a,'b,'c']
	t2=['d','e']

	t1.extend(t2)('d')#extend takes a list as an arguments and append all of the elements
	print(t)
```
```
	['a','b','c','d','e']

```
```.py
	t=['d,'f,'a','b']
	t.sort()#sort elements of the list list
	print(t)
```
```
	['a','b','d','f']

```
## Deleting elements
```
#Pop modified list
#Return the element that was removed
#If you don't provide an index,it delets and returns last element
```
```.py
	t=['a,'b,'c']
	t.pop()

	print(t)
```
```
	['a','b']

```
```.py
	t=['a,'b,'c']
	t.pop(1)

	print(t)
```
```
	['a','c']

```
```.py
	t=['a,'b,'c']
	t.del t[1]
#if you don't remove value you can use del
	print(t)
```
```
	['a','c']

```
```.py
	t=['a,'b,'c']
	t.del('b')
#you can use elements name as well
	print(t)
```
```
	['a','c']

```
```.py
	t=['a,'b,'c','d']
	t.del[1:3]
#you can use slice index
	print(t)
```
```
	['a']
```
## Lists and Functions
```.py
	num=[3,41,12,9,74,15]
	print(len(num))#Find length of numbers#6
	print(max(num))#Find maximum numbers#74
	print(min(num))#Find minimum numbers#3
	print(sum(num))#Find sum of numbers#154
	print(sum(num)/len(num))#Find average of numbers#25
```
```.py
	total=0
	count=0
	while True:
		inp=input('Enter a number:')
		if inp=='done':
		break
		value=float(inp)
		total=toatl+value
		count=count+1
	average=total/count
	print('Average:',average)
```
```.py
	numlist=list()
	while True:
		inp=input('Enter a number:')
		if inp=='done':
		break
		value=float(inp)
		numlist.append(value)
	average=sum(numlist)/len(numlist)
	print('Average:',average)
```
## List and String
```.py
	s='spam'
	t=list(s)
	print(t)
```
```
	['s','p','a','m']
```
```.py
	s='pining for the jord'
	t=s.split()
	print(t)
	print(t[2])
```
```
	['pining','for','the','jord']
	'the'
```
```.py
	s='spam-spam-spam'
	delimiter='-'
	s.split(delimiter)#Remove - from the string
	print(s.split(delimiter))
```
```
	['spam','spam','spam']
```
```.py
	t='spam','spam','spam'
	delimiter=' '
	delimiter.joint(t)#Remove - from the string
	print(delimiter.joint(t))
```
```
	'spam spam spam'
```


## Parsing lines
```.py
	fhand=open('mbox-short.txt')
	for line in fhand:
	line=line.rstrip()
	if not line.startswith('From'):
	continue
	words=line.split()
	print(word[2])
```
## List Arguments
```.py
	def delete_head(t)
		del t[0]
	letters=['a','b','c']
	delete_head(letters)
	print(letters)
```
['b','c']
```.py
	t1=[1,2]
	t2=t1.append(3)
	print(t1)
	print(t2)
	t3=t1+[3]

	print(t3)
	print(t2 is t3)
```
```
[1,2,3]
none
[1,2,3]
False
```
# ##DICTONARIES
```
	A dictonary like  a list
	It can be integer,string both
	The key(),values(),and items() Methods.
	There are 3 dictionary methods:keys(),values() and items().
	The values returned by these methods are not true lists.
	They can not be modified and do not have append() method
```
```.py
	spam={'color':'red','age':42}
		for v in spam.values():
	print(v)
	for k in spam.keys():
		print(k)
	for i in spam.items():
	print(i)
```
```
red
42
	
color
age

('color','red')
('age',42)
```
```.py
	spam={'color':'red','age':42}
	for k,v in spam.items():
		print('Key:'+k+'value:'+str(v))
```
```
key:age value:42
key:color value:red
```
## Checking wheter a key or value is exists in a Dictonary
```.py
	spam={'name':'zophine','age':7}
	name' in spam.keys()
	True
	'Zophine' in spam.keys()
	True
	'color' in spam.keys()
	True
	'color' not in spam.keys()
	True
	'color' in spam
	False
```
## The get() Method
```.py
	picnicItems={'apple':5,'cups':2}
	'I am bringing '+str(picnicItems.get('cup',0))+'cups'
	'I am bringing 2 cups'
	'I am bringing '+str(picnicItems.get('eggs',0))+'eggs'
	'I am bringing 0 eggs'
```
```.py
	counts={'chuck':1,'annie':42,'jan':100}
	print(counts.get('jan',0))
	print(counts.get('tim',0))
```
```
	100
	0
```
## Dictonaries and files
```.py
	fname=input('Enter the file name')
	try:
		fhand=open(fname)
	except:
		print('File cannot be opened',fname)
		exit()
	counts=dict()
	for line in fhand:
		words=line.split()
		for word in words:
			if word not in counts:
				counts[word]+=1
				else:
				count[word]+=1
		print(counts)
```
the romeo.txt file is available at www.py4e.com/code3/romeo.txt
```
python count1.py
Enter the file name: romeo.txt
{'and': 3, 'envious': 1, 'already': 1, 'fair': 1,
'is': 3, 'through': 1, 'pale': 1, 'yonder': 1,
'what': 1, 'sun': 2, 'Who': 1, 'But': 1, 'moon': 1,
'window': 1, 'sick': 1, 'east': 1, 'breaks': 1,
'grief': 1, 'with': 1, 'light': 1, 'It': 1, 'Arise': 1,
'kill': 1, 'the': 3, 'soft': 1, 'Juliet': 1}
```
 ## Looping and dictonaries
 ```.py
 	counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
	for key in counts:
	print(key, counts[key])
```
```
jan 100
chuck 1
annie 42
```
```.py
	counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
	for key in counts:
	if counts[key] > 10 :
	print(key, counts[key])
```
```
jan 100
annie 42
```
```.py
	counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
	lst = list(counts.keys())
	print(lst)
	lst.sort()
	for key in lst:
	print(key, counts[key])

```
```
['jan', 'chuck', 'annie']
annie 42
chu
```
```.py
	import string
	fname = input('Enter the file name: ')
	try:
		fhand = open(fname)
	except:
		print('File cannot be opened:', fname)
		exit()
	counts = dict()
	for line in fhand:
		line = line.rstrip()
			line = line.translate(line.maketrans('', '', string.punctuation))
		line = line.lower()
		words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
	print(counts)
```
```
Enter the file name: romeo-full.txt
{'swearst': 1, 'all': 6, 'afeard': 1, 'leave': 2, 'these': 2,
'kinsmen': 2, 'what': 11, 'thinkst': 1, 'love': 24, 'cloak': 1,
a': 24, 'orchard': 2, 'light': 5, 'lovers': 2, 'romeo': 40,
'maiden': 1, 'whiteupturned': 1, 'juliet': 32, 'gentleman': 1,
'it': 22, 'leans': 1, 'canst': 1, 'having': 1, ...}
```
# TUPLES
```
	A tuples is sequence of value much like list.
	The value stored in tuples can be any tupe.
	Indexed by integer
	Tuples are immutable
	Tuples are comparable and hashable
	A tuples is a comma seperated list of values
	t='a','b','c','d','e'
	t=('a','b','c','d','e')
```
To create single element,you have to include comma
```.py
	t=('a',)
	type=(t)
	print(type)

```
```
	<Type 'tuple'>
```
```.py
	t=('a')
	type=(t)
	print(type)

```
```
	<Type 'str'>
```
```.py
	t=('lupins')

	print(t)

```
```
	('l','u','p','i','n','s')
```
We can use indexing on tuples
```.py
	t=('a','b','c','d','e')
	print(t[0])
```
```
	'a'
```
We can use slice on tuples
```.py
	t=('a','b','c','d','e')
	print(t[1:3])
```
```
	('b','c')
```
We cann't modify the tuples but we can replace the tuple emlements
```.py
t=('a','b','c','d','e')
	t=('A',)+t[1:]
	print(t)
```
```
	t=('A','b','c','d','e')
```
## Tuple assignment
```.py
	m=['have','fun']
	(x,y)=m
	print(x)
	print(y)
```
```
	have
	fun
```
```.py
	m=['have','fun']
	x=m[0]
	y=m[1]
	print(x)
	print(y)
```
```
	have
	fun
```
To split an email address and username and domain name:
```.py
	addr='mainul@gmail.com'
	uname,domain=addr.split('@')
	print(uname)
	print(domain)
```
```
	mainul
	gmail.com
```
## Dictonaries and tuples
```.py
	d={'a':10,'b':20,'c':3}
	t=list(d.item())#item is a method to return a list of tuple
	print(t)
```
```
	[('b',1),('a',1),('c',1)]#No particular order
```
To give particular order use can use sort
```.py
	d={'a':10,'b':20,'c':4}
	t=list(d.item())
	print(t)
	print(t.sort)
```
```
	[('b',1),('a',1),('c',1)]
	[('a',10),('b',20),('c',1)]
```
## Multiple assignment with dictonaries
```.py
	for key,val in list(d.items()):
		print(val,key)
```
```
10 a
22 c
1 b
```
```.py	
	d={'a':10,'b':1,'c':22}
	l=list()
	for key,val in d.items():
		l.append(val,key)
	print(l)
	[(10,'a'),(22,'c'),(1,'b')]
	l.sort(reverse=True)
	print(l)
	[(22,'c'),(10,'a'),(1,'b')]
```
```.py
import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
#Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key, val)
```
```
61 i 
42 and
40 romeo
34 to
34 the
32 thou 
32 juliet
30 that
29 my
24 thee
```

# ##REGULAR EXRESSION
```.py

	import re
	hand=open('mox-short.txt')
	for line in hand:
	line=line.rstrip()
		if re.search('From:',line):
		print(line)
```

```.py

	import re
	hand=open('mox-short.txt')
	for line in hand:
	line=line.rstrip()
		if re.search('`From:',line):
		print(line)
```
## Character matching in regular expressions
```.py
	# Search for lines that start with 'F', followed by
	# 2 characters, followed by 'm:'
	import re
	hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
		if re.search('^F..m:', line):
	print(line)
```
```.py
	import re
	hand=open('mbox-short.txt')
	for line in hand:
	line =line.rstrip()
		if re.search('^From:..+@',line)
	print(line)
```
## Extrcting data using regular expressions
```.py
	import re
	a='A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
	lst=re.findall('\S+@\S',a)
	print(lst)
```
```.py
	import re
	hand=open('mbox-short.txt')
	for line in hand:
		line=line.rstrip()
		x=re.findall('\S+@\S',line)
		if len(x)>0
		print(x)
```
```.py
# Search for lines that have an at sign between characters
# The characters must be a letter or number
	import re
	hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
	x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
		if len(x) > 0:
	print(x)
# Code: http://www.py4e.com/code3/re07.py
```
## Combining Searching and extracting
```.py
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
	import re
	hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
		if re.search('^X\S*: [0-9.]+', line):
	print(line)
# Code: http://www.py4e.com/code3/re10.py

```
```
X-DSPAM-Confidence: 0.8475
X-DSPAM-Probability: 0.0000
X-DSPAM-Confidence: 0.6178
X-DSPAM-Probability: 0.0000

```
```.py
# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
	import re
	hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
	x = re.findall('^X\S*: ([0-9.]+)', line)
		if len(x) > 0:
	print(x)
# Code: http://www.py4e.com/code3/re11.py	

```
```
The output from this program is as follows:
['0.8475']
['0.0000']
['0.6178']
['0.0000']
['0.6961']
['0.0000']
..
```
```.py

# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
	import re
	hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
	x = re.findall('^Details:.*rev=([0-9.]+)', line)
	if len(x) > 0:
	print(x)
# Code: http://www.py4e.com/code3/re12.py
```
```
When we run the program, we get the following output:
['39772']
['39771']
['39770']
['39769']
...
```
```.py

# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
	import re
	hand = open('mbox-short.txt')
	for line in hand:
	line = line.rstrip()
	x = re.findall('^From .* ([0-9][0-9]):', line)
	if len(x) > 0: print(x)
# Code: http://www.py4e.com/code3/re13.py
```
```
When the program runs, it produces the following output:
['09']
['18']
['16']
['15']
...

```
## Escape Character
```.py
	import re
	x = 'We just received $10.00 for cookies.'
	y = re.findall('\$[0-9.]+',x)
```
## Summary
```
ˆ Matches the beginning of the line.
$ Matches the end of the line.
. Matches any character (a wildcard).
\s Matches a whitespace character.
\S Matches a non-whitespace character (opposite of \s).
* Applies to the immediately preceding character and indicates to match zero or
more of the preceding character(s).
*? Applies to the immediately preceding character and indicates to match zero or
more of the preceding character(s) in “non-greedy mode”.
+ Applies to the immediately preceding character and indicates to match one or
more of the preceding character(s).
+? Applies to the immediately preceding character and indicates to match one or
more of the preceding character(s) in “non-greedy mode”.
[aeiou] Matches a single character as long as that character is in the specified set.
In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
[a-z0-9] You can specify ranges of characters using the minus sign. This example
is a single character that must be a lowercase letter or a digit.
[ˆA-Za-z] When the first character in the set notation is a caret, it inverts the logic.
This example matches a single character that is anything other than an uppercase
or lowercase letter.
( ) When parentheses are added to a regular expression, they are ignored for the
purpose of matching, but allow you to extract a particular subset of the matched
string rather than the whole string when using findall().
\b Matches the empty string, but only at the start or end of a word.
\B Matches the empty string, but not at the start or end of a word.
\d Matches any decimal digit; equivalent to the set [0-9].
\D Matches any non-digit character; equivalent to the set [ˆ0-9]
````
# ##NETWORKED PROGRAMS
## Retrive data from web
```.py
import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
    mysock.close()
```
```
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already s

```





