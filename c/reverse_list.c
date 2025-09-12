#include <stdio.h>
#include <stdlib.h>

void reverse(int* arr, int size);

int main() {
    int arr[] = {1,2,4};
    int size = sizeof(arr) / sizeof(arr[0]);

    reverse(arr, size);

    for(int i = 0; i < size; i++) {
        printf("%i ", arr[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}

void reverse(int* arr, int size) {

    if(size <= 1){
        return;
    }

    printf("passsing\n");
    int temp;
    for(int i = 0; i < size / 2; i++) {
        // swap arr[i] with arr[size - 1 - i]
        temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }
}
