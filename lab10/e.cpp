#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;

    vector<vector<int>> compat(n, vector<int>(n));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> compat[i][j];
        }
    }

    while (q--) {
        vector<int> arr;
        int x;

        string line;
         getline(cin, line);
        if (line.size() == 0) getline(cin, line);

        stringstream ss(line);
        while (ss >> x) arr.push_back(x - 1); 
        bool ok = true;

        // проверяем каждую пару
        for (int i = 0; i < arr.size(); i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (compat[arr[i]][arr[j]] == 0) {
                    ok = false;
                    break;
                }
            }
            if (!ok) break;
        }

        cout << (ok ? "YES\n" : "NO\n");
    }

    return 0;
}
