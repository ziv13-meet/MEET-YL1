def cr():
	ui=raw_input("Enter something to continue: ")
	from random import randint
	num1=randint(1,2)
	if num1==1:
		print "H"
	else:
		print "T"

def cr2():	
	ui=float(raw_input("Enter the chances you want to get 'H': "))
	x = 10
	while ui%1!=0:
		ui=ui*10
		x = x*10
	from random import randint
	num1=randint(1,ui)
	num2=x-x/ui
	num3=x/ui
	if 
		print "H"
	elif:
		print "T"

