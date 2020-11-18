#include <iostream>
#include <stack>
using namespace std;

int main() {
    int N;
    do
    {
    escape:
        cin >> ws >> N;
        do {
            int tam = 1, ordem, i;
            stack<int> estacao;
            for (i = 0; i < N; i++) {
                cin >> ws >> ordem;
                if (ordem == 0) {
                    cout << endl;
                    goto escape;
                }
                while (i < N) {
                    if (estacao.size() > 0) {
                        if (estacao.top() == ordem) {
                            estacao.pop();
                            break;
                        }
                        else if (estacao.top() != ordem && tam >= N){
                            break;
                        }
                    }
                    if (ordem != tam && tam < N) {
                        estacao.push(tam);
                        tam++;
                    }
                    if (ordem == tam) {
                        tam++;
                        break;
                    }
                }
            }
            if (ordem != 0){
                if (estacao.size() == 0){
                    cout << "Yes" << endl;
                }
                else
                    cout << "No" << endl;
            }
        } while (N);
    } while (N);

    return 0;
}