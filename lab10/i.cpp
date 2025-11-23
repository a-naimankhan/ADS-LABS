#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> g(n+1);
    vector<int> indeg(n+1, 0);

    for (int k = 0; k < m; k++) {
        int i, j;
        cin >> i >> j;
        g[i].push_back(j);
        indeg[j]++;
    }

    queue<int> q;

    for (int i = 1; i <= n; i++) {
        if (indeg[i] == 0)
            q.push(i);
    }

    vector<int> order;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);

        for (int v : g[u]) {
            indeg[v]--;
            if (indeg[v] == 0)
                q.push(v);
        }
    }

    if ((int)order.size() == n) {
        cout << "Possible\n";
        for (int x : order)
            cout << x << " ";
        cout << "\n";
    } else {
        cout << "Impossible\n";
    }

    return 0;
}
