#include<stdio.h>
#include<string.h>
void Push(char);
void POP();
int top=-1;

void Push(char x)
{top++;
char ar[20];
ar[top]=x;
}

void POP()
{top--;}

void main()
{ char str[50];

printf("Enter the if expression");
gets(str);

int len=strlen(str);

for(int i=0;i<len;i++)
{if(str[i]=='(')
Push(str[i]);
else if(str[i]==')')
POP();
}

}
