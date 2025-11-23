#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];

    vector<vector<bool>> vis(n, vector<bool>(m, false));

    vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};

    auto bfs = [&](int sx, int sy) {
        queue<pair<int,int>> q;
        q.push({sx, sy});
        vis[sx][sy] = true;

        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();

            for (auto &d : dirs) {
                int nx = x + d.first;
                int ny = y + d.second;
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (!vis[nx][ny] && grid[nx][ny] == '1') {
                        vis[nx][ny] = true;
                        q.push({nx, ny});
                    }
                }
            }
        }
    };

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '1' && !vis[i][j]) {
                bfs(i, j);
                cnt++;
            }
        }
    }

    cout << cnt << "\n";
    return 0;
}
