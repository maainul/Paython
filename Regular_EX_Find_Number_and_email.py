import re
def phone():
    hand=open('t.txt')
    for line in hand:
        line = line.rstrip()
        x = re.findall('^\d.*-\d.*\d.*', line)
        if len(x) > 0:
            print(x)
def email():
    hand=open('t.txt')
    for line in hand:
        line=line.rstrip()
        x=re.findall('[a-zA-Z0-9]\S+@+\S+[a-zA-Z]', line)
        if len(x)>0:
            print(x)
phone()
email()

