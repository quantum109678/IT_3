#include<stdio.h>

void main()
{int a[100][100];
int n;
printf("Enter the size of the array:");
scanf("%d",&n);

printf("Enter the elements of the array");

for(int i=0;i<n;i++)
{for(int j=0;j<n;j++)
{scanf("%d",&a[i][j]);
}
}
printf("Lower triangle of the matrix:\n");

for(int i=0;i<n;i++)
{for(int j=0;j<n;j++)
{if(i>=j)
printf("%d",a[i][j]);
else
printf(" ");
}
printf("\n");
}
}
