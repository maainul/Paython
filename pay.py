Hours=input('Enter Hours:')
print(Hours)
Rates=input('Enter Rates:')
print(Hours)
if int(Hours)>40:
  pay=int(Hours)*int(Rates)+(int(Rates)*1.5)
  print(pay)
else:
  pay=int(Hours)*int(Rates)
print(pay)
print(type(pay))
