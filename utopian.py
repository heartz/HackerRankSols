test = int(input())
while(test):
    cycles=int(input())
    temp= int(cycles/2)
    temp= (2**(temp+1))-1
    if(cycles%2):
        print(2*temp)
    else:
        print(temp)
    test=test-1
