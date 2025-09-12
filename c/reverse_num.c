#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int reverse(int n);

int main() {
    int number = 234;
    int reversed_num = reverse(number);

    printf("The reversed number is: %d\n", reversed_num);

    return EXIT_SUCCESS;
}

int reverse(int n) {
    char str_num[256];
    sprintf(str_num, "%d", n);  // convert int to string

    int size = strlen(str_num);  // correct length of the number string
    char temp;

    // reverse the string
    for (int i = 0; i < size / 2; i++) {
        temp = str_num[i];
        str_num[i] = str_num[size - 1 - i];
        str_num[size - 1 - i] = temp;
    }

    return atoi(str_num);  // convert back to int
}
