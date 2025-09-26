#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//function declarations
int count(char sentence[], int size);
bool hasVowel(char sentence[], int size);

//const
 const char vowels[] = {'a','e','i', 'o','u'};
 const int size_of_vowel = sizeof(vowels) / sizeof(vowels[0]);

int main(){
    printf(".....................Welcome to vowel counter......................\n ");

    char vowels[] = {'a', 'e', 'i', 'o', 'u'};
    char sentences[] = "the quick brown fox jumps over the lazy dog";

    int size = sizeof(sentences) / sizeof(sentences[2]);

    int total = count(sentences, size);
    printf("The vowel count is: %d\n",total);

    //checking if it has vowel
    bool isVowel = hasVowel(sentences, size);
    printf("This sentence has a vowel: %d\n",isVowel);
    return EXIT_SUCCESS;
}


int count(char sentence[], int size){
    int count = 0;
     for (int i = 0; i < size; i++){
        for(int j = 0; j < size_of_vowel; j++){
            if(vowels[j] == sentence[i]){
                count ++;
            }
        }
    }

    return count;
}

bool hasVowel(char sentence[], int size){
    int count = 0;
    for (int i = 0; i < size; i++){
        for(int j = 0; j < size_of_vowel; j++){
            if(vowels[j] == sentence[i]){
                count++;
            }
        }
    }

    if(count < 1){
        return false;
    }

    return true;
}
