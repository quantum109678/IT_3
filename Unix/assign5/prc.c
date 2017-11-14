#include <stdio.h>
#include <sys/wait.h>

void main()
{
	int pid;
	int status;
	printf("Before forking\n");
	pid=fork();
	if (pid==-1)
	{
		printf("Bad fork\n");
		exit(1);
	}
	if (pid==0){
		printf("This is the child process with pid %d\n",pid);
	}
	else 
		{printf("This is the parent process with pid%d\n",pid);
exit(0);}
}