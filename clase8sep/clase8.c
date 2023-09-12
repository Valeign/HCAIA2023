#include <stdio.h>

#define SAD

int main()
{
#ifdef SAD
	printf("Hola mundo, soy estudiante de postgrado");
#else
	printf("Hola mundo c:");
#endif
	return 0;

}
