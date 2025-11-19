#include <bits/stdc++.h>
using namespace std;

int min_repetition(const string& A, const string& B) {
    string repeated = A;
    int count = 1;
    while (repeated.size() < B.size()) {
        repeated += A;
        count++;
    }
    if (repeated.find(B) != string::npos) {
        return count;
    }
    repeated += A;
    if (repeated.find(B) != string::npos) {
        return count + 1;
    }

    return -1;
}

int main() {
    string s, sub;
    cin >> s >> sub;

    cout << min_repetition(s, sub);
    return 0; 

    cout << 
}
