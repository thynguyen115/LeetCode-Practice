#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

int main(void) {
    int num = 42;
    printf("The answer is %d.\n", num);
    char* greeting = "Hello";
    printf("%s", greeting);
    char greet[10] = "Hello!";
    printf("\n%c", greet[3]);
    float int_division = 9 / 4; // give 2.0 due to 9, 4 are integers
    float float_division = 9.0 / 4; // gives 2.25
    printf("\n%f", float_division);
    printf("\n%f", int_division);
}
