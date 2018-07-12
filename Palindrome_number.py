n=int(input('Enter number: '))
t = n
rev=0
while(t>0):
    dig=t%10
    rev=rev*10+dig
    t=t//10
print('Reverse of the number:',rev)
if(rev == n):
  print('Palindrom number')
else:
  print('not Palindrom')
