#include <stdio.h>
#include <stdlib.h>

int fact(int num){
    if(num == 0 || num == 1){
        return num;
    }

    return num * fact(num - 1);
}

int main(){
    int value = fact(10);

    printf("The value is: %i\n", value);

    return EXIT_SUCCESS;
}
