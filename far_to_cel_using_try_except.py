inp=input('Enter farenheit Temperatur')
try:
far=float(inp)
cel=(far-32.0)*5.0/9.0
print(cel)
except:
	print('Enter a number')
	
