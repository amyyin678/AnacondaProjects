largest = None
smallest = None
while True:
	num=input('Enter a number: ')
	if num=='done':
		break
	try:
		val=int(num)
	except:
		print('Invalid input')
		continue
	if smallest is None:
		smallest = val
		largest = val
	elif val < smallest:
		smallest = val
	elif val > largest:
		largest = val

print('Maximum is', largest)
print('Minimum is', smallest)
