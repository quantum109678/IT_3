#include<stdio.h>

void main()
{
int n,i,j,a[100];
printf("Enter the size of the array");
scanf("%d",&n);
printf("Enter the elements");
for(i=0;i<n;i++)
scanf("%d",&a[i]);

int temp,max,min,pos1=0,pos2=0;
max=a[0];
min=a[0];
for(i=1;i<n;i++)
{if(max<a[i])
pos1=i;
}

for(j=1;j<n;j++)
{if(min>a[i])
pos2=j;
}

temp=a[pos1];
a[pos1]=a[pos2];
a[pos2]=temp;

printf("Array after interchanging largest and smallest element:");
for(i=0;i<n;i++)
{printf("%d ",a[i]);}
}
