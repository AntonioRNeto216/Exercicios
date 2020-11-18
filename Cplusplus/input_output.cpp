#include<iostream>
using namespace std;

int main() {
    int a, b, c;
    do {
        cin >> a >> b >> c;
    } while((a < 1 || a > 1000) && (b < 1 || b > 1000) && (c < 1 || c > 1000));
    cout << a+b+c << endl;

    return 0;
}