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
# ##Files
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


# ##Lists
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



