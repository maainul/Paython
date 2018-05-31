import re
file=open('mbox-short.txt')
count=0
for line in file:
    #line=line.strip()
    count+=1
    if re.search('F..m',line):
        print(line)
print(count)
