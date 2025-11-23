#include <bits/stdc++.h>
using namespace std;

const int WHITE = 0, GRAY = 1, BLACK = 2;

int n, m;
vector<vector<int>> g;
vector<int> color, parent;
vector<pair<int,int>> cycle_edges;

bool dfs(int u) {
    color[u] = GRAY;
    for (int v : g[u]) {
        if (color[v] == WHITE) {
            parent[v] = u;
            if (dfs(v)) return true;
        } else if (color[v] == GRAY) {
            cycle_edges.clear();
            int x = u;
            cycle_edges.push_back({u, v});
            while (x != v) {
                int px = parent[x];
                cycle_edges.push_back({px, x});
                x = px;
            }
            return true;
        }
    }
    color[u] = BLACK;
    return false;
}

bool has_cycle_skip(int su, int sv) {
    vector<int> col(n+1, WHITE);

    function<bool(int)> dfs2 = [&](int u) {
        col[u] = GRAY;
        for (int v : g[u]) {
            if (u == su && v == sv) continue;
            if (col[v] == WHITE) {
                if (dfs2(v)) return true;
            } else if (col[v] == GRAY) {
                return true;
            }
        }
        col[u] = BLACK;
        return false;
    };

    for (int i = 1; i <= n; i++) {
        if (col[i] == WHITE) {
            if (dfs2(i)) return true;
        }
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    g.assign(n+1, {});
    color.assign(n+1, WHITE);
    parent.assign(n+1, -1);

    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back(v);
    }

    bool found = false;
    for (int i = 1; i <= n; i++) {
        if (color[i] == WHITE && dfs(i)) {
            found = true;
            break;
        }
    }

    if (!found) {
        cout << "YES\n";
        return 0;
    }

    // Try removing each edge of the cycle
    for (auto &p : cycle_edges) {
        if (!has_cycle_skip(p.first, p.second)) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
}
