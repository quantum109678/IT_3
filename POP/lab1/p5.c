#include<stdio.h>

void main()
{int a1[100],a2[100],a3[100];
int n1,n2;
printf("Enter size of array1:");
scanf("%d",&n1);
printf("Enter elements of array1:");
for(int i=0;i<n1;i++)
scanf("%d",&a1[i]);
printf("Enter size of array2:");
scanf("%d",&n2);
printf("Enter elements of array2:");
for(int i=0;i<n2;i++)
scanf("%d",&a2[i]);

for(int i=0;i<n1;i++)
a3[i]=a1[i];



for(int i=0;i<n2;i++)
{
a3[i+n1]=a2[i];
}

int n=n1+n2,t;
for(int i=0;i<n-1;i++)
{for(int j=0;j<n-i-1;j++)
{if(a3[j]>a3[j+1])
{t=a3[j];
a3[j]=a3[j+1];
a3[j+1]=t;
}
}
}

for(int i=n-1;i>=0;i--)
printf("%d ",a3[i]);
}
