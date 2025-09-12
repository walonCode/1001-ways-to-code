#include <stdio.h>
#include <stdlib.h>

int sumOfEven(int array[], int size);
int sumOfOdd(int array[], int size);

int main(){
    int array[] = {1,2,3,4,5,6};
    int size = sizeof(array) / sizeof(array[0]);
    int evenValue = sumOfEven(array, size);
    int OddValue = sumOfOdd(array, size);

    //print the sum of the even
    printf("The sum of the even values in the array is: %i\n",evenValue);

    //print the sum of the odd
    printf("The sum of the odd values in the array is: %i\n",OddValue);

    return EXIT_SUCCESS;
}

int sumOfEven(int array[], int size){
    if(size <= 1){
        return array[0];
    }

    int sum = 0;

    for(int i = 0; i < size; i++){
        if(array[i] % 2 == 0){
            sum += array[i];
        }    
    }

    return sum;
}


int sumOfOdd(int array[], int size){
    if(size <= 1){
        return array[0];
    }

    int sum = 0;

    for(int i =0; i < size; i++){
        if(array[i] % 2 == 1){
            sum += array[i];
        }
    }

    return sum;
}