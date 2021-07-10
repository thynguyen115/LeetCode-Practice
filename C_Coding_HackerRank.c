#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define MAX_HEIGHT 41

// ================= Chap: Intro to C ================= //
/*
    Find max of 4 integers
*/
int max_of_four(int a, int b, int c, int d) {
    int max1 = a;
    int max2 = c;
    if (a < b) {
        max1 = b;
    }
    if (c < d) {
        max2 = d;
    }
    if (max1 < max2) {
        return max2;
    }
    return max1;
}
/*
    Update values of *a and *b
    such that *a = *a + *b and *b = |*a - *b|
*/
void update(int *a,int *b) {
    int temp = *a;
    *a = *a + *b;
    if (temp > *b) {
        *b = temp - *b;
    } else {
        *b = *b - temp;
    }
}

/* ============= Chap: STRUCT =============  */
struct box
{
	/**
	* Define three fields of type int: length, width and height
	*/
    int length;
    int width;
    int height;
};

typedef struct box box;

int get_volume(box b) {
	/**
	* Return the volume of the box
	*/
    return b.length * b.width * b.height;
}

int is_lower_than_max_height(box b) {
	/**
	* Return 1 if the box's height is lower than MAX_HEIGHT and 0 otherwise
	*/
    if (b.height < MAX_HEIGHT) {
        return 1;
    } else {
        return 0;
    }
}


int main() 
{
    /* =========== Learn to Print Output =========== */
    char s[100];
    scanf("%[^\n]%*c", &s);
  	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    printf("Hello, World!\n"); // Print Hello, World!
    printf(s); // then print user input
    // return 0;
    
    /* Read and Print a char, a string, a sentence */
    char chr; // C
    char s1[100]; // Language
    char sen[100]; // Welcome To C!!!
    scanf("%c", &chr);
    scanf("%s", &s1);
    scanf("\n"); // new line from previous string
    scanf("%[^\n]%*c", sen);
    printf("%c\n", chr);
    printf("%s\n", s1);
    printf("%s", sen);
    // return 0;
    
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    // return 0;
    
    /* ================ Learn to Work with Struct ================ */
    int n;
	scanf("%d", &n);
	box *boxes = malloc(n * sizeof(box));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &boxes[i].length, &boxes[i].width, &boxes[i].height);
	}
	for (int i = 0; i < n; i++) {
		if (is_lower_than_max_height(boxes[i])) {
			printf("%d\n", get_volume(boxes[i]));
		}
	}
	return 0;
}
