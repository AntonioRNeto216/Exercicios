#include<iostream>
using namespace std;

bool verificaImpar(int num) {
    if(num%2 == 0){
        return false;
    } else {
        return true;
    }
}

int main() {
    int a, b;
    string numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    string maior[2] = {"even", "odd"};
    cin >> a >> b;
    if(b >= a) {
        for(int i=a; i<=b; i++) {
            if(i >= 1 && i <= 9) {
                cout << numbers[i-1] << endl;
            } else if(verificaImpar(i)){
                cout << "odd" << endl;
            } else {
                cout << "even" << endl;
            }
        }
    }

    return 0;
}