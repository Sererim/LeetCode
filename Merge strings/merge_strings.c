// 1768 Merge Strings Alternately
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Funciton prototypes.
char* mergeAlternately(char*, char*);


int main(void) {
    char word1[] = {'a', 'b', 'c', 'd', '\0'};
    char word2[] = {'p', 'q', '\0'};
    char* result = mergeAlternately(word1, word2);

    printf("%s", result);
    
    free(result);
    return 0;
}

char* mergeAlternately(char* word1, char* word2){
    char* str = (char*)malloc((strlen(word1) + strlen(word2) + 1));
    unsigned short j = 0;

    for (unsigned short i = 0; i < strlen(word1) || i < strlen(word2); i++) {
        if (i < strlen(word1)) {
            str[j] = word1[i];
            j++;
        }

        if (i < strlen(word2)) {
            str[j] = word2[i];
            j++;
        }
    } 

    str[j] = '\0';

    return str;
}
