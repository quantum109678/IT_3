#include<stdio.h>
void func();

struct list{
char n[50];
int pr;
int qty;
}l[5];

void func(){
l[0].n="Product1";
l[1].n="Product2";
l[2].n="Product3";
l[3].n="Product4";
l[4].n="Product5";
l[0].pr=10;
l[1].pr=20;
l[2].pr=30;
l[3].pr=40;
l[4].pr=50;

printf("Product name:     Price per unit:\n");
for(int i=0;i<5;i++)
printf("%s     %d",l[i].n,l[i].pr);

printf("Enter the quantity of each product");
for(int i=0;i<5;i++)
{printf("Product%d:",i+1);
scanf("%d",&l[i].qty);}
int sum=0;

printf("Total cost=");
for(int i=0;i<5;i++)
{sum=l[i].pr*l[i].qty;}
printf("%d",sum);
}

void main()
{func();}
