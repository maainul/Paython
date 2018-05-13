Hours=input('Enter Hours:')
Rates=input('Enter Rates:')
if int(Hours)>40:
  pay=40*int(Rates)+(int(Hours)-40)*(int(Rates)*1.5)
  print(pay)
else:
  pay=int(Hours)*int(Rates)
print(pay)
