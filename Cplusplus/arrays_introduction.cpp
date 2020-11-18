#include<iostream>
using namespace std;

int main() {
    int N, num, *vetor;
    cin >> N;
    vetor = new int[N];
    for(int i=0; i<N; i++) {
        cin >> num;
        vetor[N-1-i] = num;
    }
    for(int i=0; i<N; i++) {
        cout << vetor[i] << " ";
    }
    
    delete[] vetor;

    return 0;
}