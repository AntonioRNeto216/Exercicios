#include<iostream>
using namespace std;

int main() {
    int num;
    string numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin >> num;
    if(num >= 1 && num <= 9) {
        cout << numbers[num-1];
    } else if(num > 9) {
        cout << "Greater than 9";
    }

    return 0;
}