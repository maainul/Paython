# Paython
# Automate The boring Stuff
# Chapter 5 (Dictionaries and Structuring data)

## The dictionary Data Type:

### A dictionary is collection of many values.
### Dictionary can use many data type
### Index of dictionaries is called keys
### A key with its associated value is called key-value pair.
```
1.Insert value in dictionaries:
>>mycat={'size':'fat','color':'gray',disposition:'loud'}
2.Access these values through their keys:
>>mycat['size']
'fat'
>>'My cat has '+ mycat['color']+ ' fur.'
My cat has gray fur.
```
## Dictionaries vs Lists
### Items in dictionaries are unordered.
### There is no first item in dictionary.
### The order of key value does not matter in dictionary.
```
## List 
```
>>spam=['cat','dog','moose']
>>bacon=['dogs',moose,'cat']
spam==bacon
```
## Dictionaries
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
