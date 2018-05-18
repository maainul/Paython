smallest=None
print('Before:',smallest)
for num in [3,41,12,9,74,15]:
	if smallest is None or num <smallest:
		smallest=num
print('largest:',smallest)

