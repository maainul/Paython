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
