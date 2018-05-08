try:
  Hours=input('Enter Hours:')
  Rates=input('Enter Rates:')
  if int(Hours)>40:
    pay=int(Hours)*int(Rates)+(int(Rates)*1.5)
    print(pay)
  else:
    pay=int(Hours)*int(Rates)
    print(pay)
except:
  print('Error,Please enter numeric input.')
