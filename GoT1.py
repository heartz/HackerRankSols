theString=input()
characters=list(theString)
dictionary={a:characters.count(a) for a in characters} #creates dictionary for char and frequency of each char
oddCharFrequency=0
flag=0
for x in dictionary.values():
	if(x%2!=0):
		oddCharFrequency=oddCharFrequency+1
		if(oddCharFrequency>1):
			flag=1
			break
if(flag==1):
	print("NO")
else:
	print("YES")