testCases=int(input())
for i in range(0,testCases):
	string=input()
	flag=0
	chars=list(string)
	length=len(chars)
	start=-1
	for i in range(0,length-1):
		if(chars[i]<chars[i+1]): 
			start=i  #first char to be replaced
	end = -1
	for j in range(start + 1, len(chars)):
		if(chars[start] < chars[j]): 
			end = j #second char to be replaced

	chars[start], chars[end] = chars[end], chars[start] #swapping
	a = chars[start+1:]
	a.sort() # the last few need to be sorted for lowest lexi value
	for j in range(start + 1, len(chars)):
		chars[j] = a[j-start-1] #sorted alphabets added to the string
	if(start!=-1):
		print("".join(chars))
	else:
		print("no answer")
