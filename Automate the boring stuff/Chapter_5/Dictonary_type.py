stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
#print key from the dictonary
for k in stuff.keys():
    print(k)
    #Print value from the dictonary
for v in stuff.values():
    print(v)
# print items from the dictonary
for i in stuff.items():
    print(i)

#seperate value and key
for k, v in stuff.items():
    print('Key: '+k+' value:'+str(v))
