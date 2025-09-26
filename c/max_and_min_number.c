#include <stdio.h>
#include <stdlib.h>


int max_num(int arr[], int size);
int min_num(int arr[], int size);

int main(){
    int array[] = {1,2,3,4,5};
    int size = sizeof(array) / sizeof(array[0]);

    int big_num = max_num(array, size);
    int small_num = min_num(array, size);

    printf("The big number is: %d\n",big_num);
    printf("The small number is: %d\n",small_num);

    return EXIT_SUCCESS;
}

int max_num(int arr[], int size){
    int max_num = arr[0];
    for(int i = 1; i < size; i++){
        if(arr[i] > max_num){
            max_num = arr[i];
        }
    }

    return max_num;
}

int min_num(int arr[], int size){
    int min_num = arr[0];
    for(int i = 1; i < size; i++){
        if(arr[i] < min_num){
            min_num = arr[i];
        }
    }

    return min_num;
}
