#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int test,n,a,b,i,value,min,max,value2=0;
    scanf("%d",&test);
    while(test--)
    {
    	scanf("%d %d %d",&n,&a,&b);
    	min=(a<b)?a:b;
    	max=(a>b)?a:b;
    	for(i=0;i<n;i++)
    	{
    		value= (n-i-1)*min + i*max;
    		if(value!=value2)
    			printf("%d ",value);
    		value2=value;
    	}
    	
    	    printf("\n");
    }

    return 0;
}
