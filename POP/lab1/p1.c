#include<stdio.h>
void space();
void num();
void space2();

void space2()
{static int k=1;
for(int i=0;i<k;i++)
printf(" ");
k++;}

void num(int i)
{int n=2*i-1;
for(int j=1;j<=n;j++)
printf("%d",j);
}

void space()
{static int k=4;
for(int i=0;i<k;i++)
printf(" ");
k--;}

void main(){
for(int i=1;i<=5;i++)
{space();
num(i);
printf("\n");}

for(int j=4;j>0;j--)
{space2();
num(j);
printf("\n");
}
}
