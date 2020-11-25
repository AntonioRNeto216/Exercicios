#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {
    int l1 = s.at(0) - 48;
    int l2 = s.at(1) - 48;
    int begin = (l1) * 10 + l2;
    string temp;
    if(s.at(s.size()-2) == 'P') {
        if(begin < 12) 
            begin += 12;
    } else {
        if(begin >= 12)
            begin -= 12;
    }
    l2 = begin % 10;
    l1 = (begin - l2) / 10;
    temp.push_back(l1 + 48);
    temp.push_back(l2 + 48);
    s.replace(0, 2, temp);
    s.pop_back();
    s.pop_back();
    return s;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}