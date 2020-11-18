#include<iostream>
#include<stack>
using namespace std;

int main() {
    int N;
    cin>> ws >>N;
    while(N--) {
        string x;
        stack<char> s;
        int diamante=0;
        cin>> ws >>x;
        for(auto c : x){
            if(c=='<') {
                s.push(c);
            } else
            if(s.size()>0 && c=='>') {
                s.pop();
                diamante++;
            }
        }
        cout << diamante << endl;
    }
    return 0;
}