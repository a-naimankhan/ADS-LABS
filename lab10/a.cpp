#include <bits/stdc++.h>
using namespace std;

int kill_mushrooms(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();

    queue<pair<int,int>> q;
    int mushrooms = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 2) {
                q.push({i, j});
            } else if (grid[i][j] == 1) {
                mushrooms++;
            }
        }
    }

    if (mushrooms == 0)
        return 0;

    vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};
    int minutes = -1;

    while (!q.empty()) {
        int size = q.size();
        minutes++;

        for (int s = 0; s < size; s++) {
            auto [x, y] = q.front();
            q.pop();

            for (auto& d : dirs) {
                int nx = x + d.first;
                int ny = y + d.second;

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        mushrooms--;
                        q.push({nx, ny});
                    }
                }
            }
        }
    }

    if (mushrooms != 0)
        return -1;

    return minutes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    cout << kill_mushrooms(grid) << "\n";

    return 0;
}
