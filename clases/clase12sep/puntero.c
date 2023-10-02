#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a;

	//inicializa
	a = 506;

	printf(a);
	printf(&a);

	int *pa;

	pa = &a; 

	printf(pa);
        printf(&pa);
	printf(*pa);

	return 0;
}
