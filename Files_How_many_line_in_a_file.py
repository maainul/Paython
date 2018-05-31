#print how many lines in a file
import re
file=open('mbox-short.txt')
count=0
for line in file:
    count=count+1
print(count)

#OUTPUT
#132044
