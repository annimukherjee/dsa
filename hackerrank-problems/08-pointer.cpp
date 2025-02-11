#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function    
    int a_original = *a;
    int b_original = *b;
    
    *a = a_original + b_original;
    *b = a_original - b_original;
    if (*b < 0)
    {
        *b *= -1;
    }
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
