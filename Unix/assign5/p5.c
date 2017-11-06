#include <stdio.h>
#include <sys/wait.h>  /* contains prototype for wait */
void main()
{
int pid,pid2;
int status;
printf("Before forking\n");
pid=fork();

if(pid!=0)
        {

                pid2=fork();
                
        }
if(pid == -1) /* check for error in fork */
{
perror("bad fork");
exit(1);
}
if (pid == 0||pid2==0){
if(pid==0)
	printf("%d\n",pid);
else
	printf("%d\n",pid2);

printf("I am the child process.\n");
}else
{
wait(&status);
printf("%d\n",pid);
printf("%d\n",pid2);
printf("I am the parent process.\n");
}
}
