#include <stdio.h>
#include <stdlib.h>

int main()
{
	int counter[10];

	for (int i=0; i<10; i++)
		counter[i] = i+13;
	
	for (int i=0; i<10; i++)
		printf('counter[%d] = %d\n', i, counter[i]);

	return 0;

}
