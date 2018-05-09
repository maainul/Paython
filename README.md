# Paython
## Automate The boring Stuff
### Chapter 5 (Dictionaries and Structuring data)

### The dictionary Data Type:
```
A dictionary is collection of many values.
Dictionary can use many data type
Index of dictionaries is called keys
A key with its associated value is called key-value pair.
```
#### 1.Insert value in dictionaries:
```
>>mycat={'size':'fat','color':'gray',disposition:'loud'}
2.Access these values through their keys:
>>mycat['size']
'fat'
>>'My cat has '+ mycat['color']+ ' fur.'
My cat has gray fur.
```
### Dictionaries vs Lists
```
Items in dictionaries are unordered.
There is no first item in dictionary.
The order of key value does not matter in dictionary.
```
### List 
```
>>spam=['cat','dog','moose']
>>bacon=['dogs',moose,'cat']
spam==bacon
```
### Dictionaries
```
>>eggs={'name':'Zophie','species':'cat','age':'8'}
>>ham={'species':'cat','name':'Zophie','age':'8'}
>>eggs=ham
True

Try to access a key that does not exist in dictonary will result an a KEYERROR
>>spam ={'name':'Zophie','age':'7'}
>>spam['color']
KeyError:'color'
```
### The key(),values(),and items() Methods
```
There are 3 dictionary methods that will return list-like values of the dictionary's keys,values or both keys and values:keys(),values() and items().
The values returned by these methods are not true lists.
They can not be modified and do not have append() method

>>>spam={'color':'red','age':42}
>>>for v in spam.values():
	print(v)
red
42

>>> for k in spam.keys():
	print(k)
color
age

>>> for i in spam.items():
	print(i)
('color','red')
('age',42)

>>> spam={'color':'red','age':42}
>>> for k,v in spam.items():
	print('Key:'+k+'value:'+str(v))
key:age value:42
key:color value:red
```
### Checking wheter a key or value is exists in a Dictonary
```
>>>spam={'name':'zophine','age':7}
>>>'name' in spam.keys()
	True
>>>'Zophine' in spam.keys()
	True
>>>'color' in spam.keys()
	True
>>>'color' not in spam.keys()
	True
>>>'color' in spam
	False
```
### The get() Method
```
>>>picnicItems={'apple':5,'cups':2}
>>>'I am bringing '+str(picnicItems.get('cup',0))+'cups'
'I am bringing 2 cups'
>>>'I am bringing '+str(picnicItems.get('eggs',0))+'eggs'
'I am bringing 0 eggs'
```
### The setdefault() Method
```
spam={'name':'pooka','age':7}
spam.setdefault('color','black')
'black'
>>spam
{'color':'black',age':5,'name':'pooka'}
>>>spam.setdefault('color':'white')
'black'
>>>spam
{'color':'black','age':5,'name':'pooka'}
```


# STRINGS
```
A string is a sequence of characters

1.Sting decleration:

	fruit='banana'
	print(fruit)

2.Index of strings:
	
	print(fruit[0])
	b
	print(fruit[1])
	a

3.Length of strings:

	length=len(fruit) #Declear length variable 
			   for store result of len function
	print(length)

4.Last alphabet of String:

	last=fruit[len(fruit)-1]
	print(last)

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
    banana
    b
    a
    n
    a
    n
    a
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

'Here we go'
False


