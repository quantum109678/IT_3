#include <stdio.h>
#include <sys/wait.h> 
void main()
{
int pid;
int status;
//printf("Hello World!\n");
pid = fork( );
if(pid == -1) /* check for error in fork */
{
perror("bad fork");
exit(1);
}
if (pid == 0)
printf("I am the child process,with pid %d\n",pid);
else
{
wait(&status); /* parent waits for child to finish */
printf("I am the parent process,with pid %d\n",pid);
}
}
