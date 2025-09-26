#include <stdio.h>
#include <stdlib.h>

struct Calculator {
    int value1;
    int value2;
};

int add(struct Calculator *c);
int minus(struct Calculator *c);
double divide(struct Calculator *c);
int multiply(struct Calculator *c);

int main(){
    printf("..............Welcome to the basic calculator.........\n");
    struct Calculator c;
    c.value1 = 50;
    c.value2 = 20;

    int sum = add(&c);
    printf("The sum is %d\n", sum);

    int substraction = minus(&c);
    printf("The substraction is %d\n",substraction);

    double division = divide(&c);
    printf("The division is %.2f\n",division);

    int multiplication = multiply(&c);
    printf("The multiplication is: %d\n",multiplication);

    return EXIT_SUCCESS;
}

int add(struct Calculator *c){
    return c->value1 + c->value2;
}

int minus(struct Calculator *c){
    return c->value1 - c->value2;
}

double divide(struct Calculator *c){
    return (double)c->value1 / c->value2;
}

int multiply(struct Calculator *c){
    return c->value1 * c->value2;
}
