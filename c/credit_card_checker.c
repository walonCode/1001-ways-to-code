#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool checkCard(char card[], int size);

int main(){
    char card[] = "4567567845353456";
    int size = sizeof(card)/sizeof(card[0]);

    bool cardValid = checkCard(card, size);
    printf("--------Key------- \n 1 == Valid\n 0 == inValid\n");
    printf("Card is valid %d\n",cardValid);
    return EXIT_SUCCESS;
}


bool checkCard(char card[], int size){
    if(strlen(card) < 16){
        return false;
    }

    int total = 0;

    for(int i = 0; i < size; i++){
        int n = atoi(&card[i]);
        if (i % 2 == 1){
            n *= 2;
            if (n > 9){
                n -= 9;
            }
        }
        total += n;
    }

    return total % 10 == 0;
}
