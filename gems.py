n = int(input())
n=n-1
str1=input()
str1="".join(set(str1)) #Removes repeated chars
while(n):	
	str2=input()
	str2="".join(set(str2))
	str1="".join([e for e in str1 if e in str2])
	n=n-1
print(len(str1))

	
