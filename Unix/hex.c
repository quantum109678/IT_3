#include<stdio.h>
#include<string.h>

void main(){
int n,c,i=0,arr[100];

printf("Enter the number");
scanf("%d",&n);

while(n>0)
{arr[i]=n%16;
n/=16;
i++;
}

arr[i]=n;

for(i=0; ;i++)
{if (arr[i]=='\0')
break;

else
c++;}

for(i=c-1;i>=0;i--)
{if(arr[i]==10)
printf("A");
if(arr[i]==11)
printf("B");
if(arr[i]==12)
printf("C");
if(arr[i]==13)
printf("D");
if(arr[i]==14)
printf("E");
if(arr[i]==15)
printf("F");
if(arr[i]<10)
printf("%d",arr[i]);
}
}






