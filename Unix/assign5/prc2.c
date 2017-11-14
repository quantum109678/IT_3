#include <stdio.h>
#include <sys/wait.h>

void main()
{
	int pid1,pid2,status;

	printf("Before forking\n");

	pid1=fork();

	if (pid1!=0){

		pid2=fork();
	}
	if (pid1==-1){
		printf("Bad fork");
		exit(1);
	}
	if(pid1==0 || pid2==0)
	{
		if(pid1==0)
			{printf("This is the first child with pid%d\n",pid1);}
		else
			{printf("This is the second child with pid%d\n",pid2);}

	}
	else{
		wait(&status);
		printf("This is the parent process");
		printf("%d\n",pid1);
		printf("%d\n",pid2 );
	}
}