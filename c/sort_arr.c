#include <stdio.h>
#include <stdlib.h>

int main(){
    printf("Welcome to array sorter");

    int arr[] = {4,3,5,2,7,4,6,9,8,4,5,3};
    int size = sizeof(arr) / sizeof(arr[1]);

    for(int i = 0; i < size; i++){
        for(int j =0; j < size - i; j++){
            if(arr[j] > arr[j +1]){
                int temp = arr[j+1];
                arr[j + 1] = arr[j];
                arr[j] = temp;

            }
        }
    }

    for (int i = 0; i < size; i++){
        printf("%d\n",arr[i]);
    }

    return EXIT_SUCCESS;
}
