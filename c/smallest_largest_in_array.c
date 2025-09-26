#include <stdio.h>
#include <stdlib.h>

int smallest(int array[], int size);
int largest(int array[], int size);

int main(){
    int array[] = {1,2,3,4,5,6,7};
    int len = sizeof(array) / sizeof(array[0]);

    for (int i = 0; i <= len - 1 ; i++){
        printf("%i\n",array[i]);
    }

    int smallest_in_array = smallest(array, len);
    printf("The smallest number in the array is: %d\n",smallest_in_array);

    int largest_in_array = largest(array, len);
    printf("The largest number in the array is: %d\n",largest_in_array);

    return EXIT_SUCCESS;
}


int smallest(int array[], int size){
    int smallest = array[0];

    for (int i = 0; i < size; i++){
        if(array[i] < smallest){
            smallest = array[i];
        }
    }

    return smallest;
}


int largest(int arr[], int size){
    int largest = arr[0];

    for (int i = 0; i< size; i ++){
        if(arr[i] > largest){
            largest = arr[i];
        }
    }

    return largest;
}
