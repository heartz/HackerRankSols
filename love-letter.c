#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int test,i,j,len,total;
    char a[10000];
    scanf("%d",&test);
    while(test--)
    {
	total=0;
        scanf("%s",a);
        len = strlen(a);
        for(i=0;i<(len/2);i++)
        {
            total+= abs((a[len-i-1]-a[i]));
        }
	printf("%d\n",total);
    }
    return 0;
}
