#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

char* mergeAlternately(char* word1, char* word2) {
    int read = 0;
    int write = 0;

    char* word = (char*)malloc(sizeof(char) * (strlen(word1) + strlen(word2) + 1));

    while (word1[read] != '\0' && word2[read] != '\0') {
        word[write++] = word1[read];
        word[write++] = word2[read];
        read++;
    }

    if (word1[read] == '\0') {
        while (word2[read] != '\0') {
            word[write++] = word2[read++];
        }
    } else {
        while (word1[read] != '\0') {
            word[write++] = word1[read++];
        }
    }
    word[write] = '\0';
    return word;
}


int main() {
    // First case.
    char word1[] = "abc";
    char word2[] = "pqr";

    // Second case.
    char word3[] = "ab";
    char word4[] = "pqrs";

    // Third case.
    char word5[] = "abcd";
    char word6[] = "pq";

    char* word = mergeAlternately(word1, word2);
    assert(strcmp(word, "apbqcr") == 0);
    
    word = mergeAlternately(word3, word4);
    assert(strcmp(word, "apbqrs") == 0);

    word = mergeAlternately(word5, word6);
    assert(strcmp(word, "apbqcd") == 0);
    free(word);
    return 0;
}