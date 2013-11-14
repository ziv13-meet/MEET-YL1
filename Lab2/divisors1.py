def divisors():	
	try:
		n=int(raw_input("Enter a number: "))
	except ValueError:
		print "Only numbers are acceptable!"
		return divisors()
	list1=[]
	for x in range(n):
		list1.append(x+1)
	print list1
		 
	
