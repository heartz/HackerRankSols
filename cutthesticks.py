noOfSticks=int(input())
numbers=input().split()
numbers=[int(x) for x in numbers]
length=len(numbers)

while(length>0):
	print(length)
	minList=min(numbers)
	numbers=[(x-minList) for x in numbers]
	numbers=[x for x in numbers if x!=0]
	length=len(numbers)