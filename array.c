#include <stdio.h>
#include <string.h>
 
int main(void) {
    int t; scanf("%d",&t);
    while(t--)
    {
        unsigned int n,i;scanf("%u",&n);
        unsigned int a[n],min=100001;
        for(i=0;i<n;i++)
        {
            scanf("%u",&a[i]);
            if(min>a[i]) min=a[i];
        }
        printf("%u\n",min*(n-1));
    }
	// your code goes here
	return 0;
}
