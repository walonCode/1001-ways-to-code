#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isPalindrome(char* word);

int main(){
    printf("Welcome to panlindrome checker!!!\n");

    printf("Enter the word to be checked: ");
    char word[256];
    scanf("%s", &word);

    bool ispalindrome = isPalindrome(word);

    printf("The word is %s is a palindrome: %d\n",word, ispalindrome);
}

bool isPalindrome(char* word){
    size_t len = strlen(word);
    if (len <= 1) {
        return true;
    }

    char reversed[256];
    for (size_t i = 0; i < len; i++) {
        reversed[i] = word[len - 1 - i];
    }
    reversed[len] = '\0';

    printf("Test word is %s\n", reversed);

    if (strcmp(word, reversed) != 0) {
        return false;
    }
    return true;
}