#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverseString(char str[], int start, int end) {
    char temp;
    while(start < end) {
        temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        start++;
        end--;
    }
}

void reverse(char str[]) {
    int start = 0;
    int end = strlen(str) - 1;
    reverseString(str, 0, end);

    while(start < end) {
        int wordStart = start;
        int wordEnd = start;

        //1. Find the end of the word
        while(str[wordEnd] != ' ' && wordEnd != end) {
            wordEnd++;
        }
        if(wordEnd != end) {
            wordEnd--; //Found a space, back it up
        }

        //2. Reverse this word
        reverseString(str, wordStart, wordEnd);

        //3. Move to the next word
        if(wordEnd != end) {
            start = wordEnd + 2; //Account for empty space
        } else {
            start = end; //Done
        }
    }
}

void test(char * str){
    char * testStr = (char *) malloc(sizeof(str));
    strcpy(testStr, str);
    reverse(testStr);
    printf("%s\n", testStr);
    free(testStr);
}

int main()
{
    test("Please reverse me");
    test("This is just a longer test");
    test("This is");
    test("This");
    test("");
}