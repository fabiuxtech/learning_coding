#include <stdio.h>
int main() {
    char author = 'Fabio Carrassi';
    short a;
    long b;
    long long c;
    long double d;
    printf("size of short = %d bytes\n", sizeof(a));
    printf("size of long = %d bytes\n", sizeof(b));
    printf("size of long long = %d bytes\n", sizeof(c));
    printf("size of long double = %d bytes\n", sizeof(d));
    printf("The Authos is = %c");
    return 0;
}