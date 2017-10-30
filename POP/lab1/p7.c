#include<stdio.h>
#include<string.h>
 void main()
{
char str[100];
printf("Enter the string:");
gets(str);

char x;
printf("Enter the character to be searched for:");
scanf("%c",&x);
 int len=strlen(str);
int k=0,c=0,arr[20];

for(int i=0;i<len;i++)
{if(str[i]==x)
{c++;
arr[k]=i;
k++;}
}
arr[k]='\0';

printf("Number of repititions of %c in string=%d\n",x,c);
printf("Positions where %c occurs=",x);
for(int i=0;i<k;i++)
printf("%d,",++arr[i]);

}
