#include <bits/stdc++.h>
using namespace std;

static const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, q;
    cin >> n >> m >> q;

    vector<vector<int>> g(n+1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    vector<long long> dist(n+1, INF);
    deque<int> dq;

    auto bfs_update = [&]() {
        while (!dq.empty()) {
            int u = dq.front();
            dq.pop_front();

            for (int w : g[u]) {
                if (dist[w] > dist[u] + 1) {
                    dist[w] = dist[u] + 1;
                    dq.push_back(w);
                }
            }
        }
    };

    while (q--) {
        int t, v;
        cin >> t >> v;

        if (t == 1) {
            if (dist[v] > 0) {     
                dist[v] = 0;
                dq.push_back(v);
                bfs_update();
            }
        } else {
            if (dist[v] == INF) cout << -1 << "\n";
            else cout << dist[v] << "\n";
        }
    }

    return 0;
}
