#include<iostream>
using namespace std;

void update(int *a,int *b) {
    int valor_a, valor_b;
    valor_a = *a+*b;
    if(*a-*b < 0) {
        valor_b = (*a-*b)*-1;
    } else {
        valor_b = *a-*b;
    }
    *a = valor_a;
    *b = valor_b;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    cin >> a >> b;
    update(pa,pb);
    cout << a << "\n" << b;

    return 0;
}