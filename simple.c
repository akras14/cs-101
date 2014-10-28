#include<stdio.h>

char * test(char * str) {
    return str;
}

int main()
{
    char * what = test("Hello");
    printf("%s\n", what);
}