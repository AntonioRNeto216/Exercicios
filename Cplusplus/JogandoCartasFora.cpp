#include<iostream>
#include<queue>
using namespace std;

int main() {
    int n, i;
    do {
        queue<int> dc, pc;
        cin>>ws>>n;
        if(n>=2 and n<=50) {
            for(i=1;i<=n;i++) {
                pc.push(i);
            }
            while(pc.size()!=1) {
                dc.push(pc.front());
                pc.pop();
                pc.push(pc.front());
                pc.pop();
            }
            cout << "Discarded cards:";
            for(i=0;i<(n-1);i++) {
                cout << " " << dc.front();
                if(i!=(n-2)) {
                    cout << ",";
                }
                dc.pop();
            }
                cout << endl;
                cout << "Remaining card:" << " " << pc.front();
                cout << endl;
        }
    }while(n);
    return 0;
}