def palindrome():
	word=raw_input("Enter a word: ")
	wordlist1=[]
	wordlist2=[]
	for i in word:
		wordlist2.insert(0,i)
		wordlist1.append(i)
	if wordlist2[0]==wordlist1[0]:
		print "Palindrome!"
	else:
		print "Not Palindrome!"
palindrome()
