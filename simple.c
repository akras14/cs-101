#include<stdio.h>
#include <stdlib.h>

int stringLength(char * str) {
    int count = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        count++;
    }
    return count;
}

char * reverse(char * str) {
    char * newStr = (char *) malloc(sizeof(str));
    int strLength = stringLength(str);

    int end = strLength - 1;
    int newStringLength = 0;

    while(end > 0) {

        int start = end;
        int i;

        //1. Find first letter
        while(str[start] != ' ' && start != 0) {
            if(start > 0) {
                start--;
            }
        }
        if(start > 0) {
            start = start + 1;
        }

        //2. Copy every letter in the word
        for( i = 0; i <= end - start; i++) {
            newStr[newStringLength + i] = str[start + i];
            printf("Storing %c in %i\n", str[start + i], newStringLength + i);
        }
        //3. Store the space
        newStringLength = newStringLength + i;
        printf("New string length %i \n", newStringLength);
        newStr[newStringLength] = ' ';
        newStringLength++;
        printf("New string length %i \n", newStringLength);
        printf("string is: %s\n\n", newStr);

        //4. Move to the next word
        end = start - 2;
    }
    return newStr;
}

int main()
{
    char str[] = "Please reverse me";
    printf("%s\n", reverse(str));
}