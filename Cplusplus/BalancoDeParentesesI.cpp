#include<iostream>
#include<stack>
using namespace std;

int main() {
    string entrada;
    while(cin>>ws>>entrada) {
        stack<char> eq;
        for(auto c:entrada) {
            if(c=='(' or c==')') {
                if(eq.size()==0 and c==')') {
                    eq.push(c);
                    break;
                } else if(eq.size()==0 and c=='(') {
                    eq.push(c);
                } else if(eq.size()>0) {
                    if(c!=eq.top()) {
                        eq.pop();
                    } else
                        eq.push(c);
                }
            }
        }
        if(eq.size()>0) {
            cout << "incorrect" << endl;
        } else
            cout << "correct" << endl;
    }
    return 0;
}