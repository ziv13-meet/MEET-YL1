def divisors(n):	
	try:
		n=int(n)
	except ValueError:
		print "Only numbers are acceptable!"
		return 
	list1=[]
	for x in range(n):
		list1.append(x+1)
		if n%(x+1)==0:
			print x+1
	
	

