#print how many words in a file
import re
file=open('mbox-short.txt')
count=0
for line in file:
    for word in line:
        count=count+1
print(count)

#OUTPUT
#6685024
