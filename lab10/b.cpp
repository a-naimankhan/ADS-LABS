#include <bits/stdc++.h>
using namespace std;

int find_shortest_path(const vector<vector<int>>& matrix, int s, int e) {
    int start = s - 1;
    int end = e - 1;
    int n = matrix.size();

    vector<bool> visited(n, false);
    vector<int> dist(n, -1);

    queue<int> q;
    q.push(start);
    visited[start] = true;
    dist[start] = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (u == end) {
            return dist[u];
        }

        for (int v = 0; v < n; v++) {
            if (matrix[u][v] == 1 && !visited[v]) {
                visited[v] = true;
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    return -1; 
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    int start, end;
    cin >> start >> end;

    cout << find_shortest_path(grid, start, end) << "\n";
    return 0;
}
