#include <stdio.h>

int fibo(int num){
    if(num == 0 || num == 1){
        return num;
    }

    return fibo(num -1 ) + fibo(num -2);
}

int main(){
    int value = fibo(10);

    printf("value is: %i\n",value);
}