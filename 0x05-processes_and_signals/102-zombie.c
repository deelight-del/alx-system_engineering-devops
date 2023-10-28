#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * main - Function to create zombie processes
 *
 * Retturn: void
 */

int main(void)
{
	pid_t pid;
	int i;

	/*create a new chld process*/
	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %u\n", pid);
		}
	}
	return (0);
}
