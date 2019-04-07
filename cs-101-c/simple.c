#include <stdio.h>
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
        for( i = 0; i <= end - start; i++) { //For word length
            newStr[newStringLength + i] = str[start + i];
        }

        //3. Store the empty space
        newStringLength = newStringLength + i;
        newStr[newStringLength] = ' ';
        newStringLength++;

        //4. Move to the next word
        end = start - 2;
    }
    
    //Terminate the string properly
    newStr[newStringLength] = '\0';

    return newStr;
}

void test(char * testStr) {
    char * revStr = reverse(testStr);
    printf("%s\n", revStr);
    free(revStr);
}

int main()
{
    test("Please reverse me");
    test("This is just a longer test");
    test("This is");
    test("This");
    test("");
}