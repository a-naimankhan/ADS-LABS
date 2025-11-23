#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int v : g[u]) {
        if (!visited[v]) dfs(v);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    g.assign(n+1, {});
    visited.assign(n+1, false);

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        g[x].push_back(y);
        g[y].push_back(x);
    }

    int s, f;
    cin >> s >> f;

    dfs(s);

    cout << (visited[f] ? "YES" : "NO") << "\n";
}
