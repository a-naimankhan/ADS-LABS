#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int start, target;
    cin >> start >> target;

    const int MAXN = 100000;

    vector<int> dist(MAXN+1, -1);
    vector<int> parent(MAXN+1, -1);

    queue<int> q;
    q.push(start);
    dist[start] = 0;
    parent[start] = -1;

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        if (x == target) break;

        if (x * 2 <= MAXN && dist[x*2] == -1) {
            dist[x*2] = dist[x] + 1;
            parent[x*2] = x;
            q.push(x*2);
        }

        if (x - 1 >= 1 && dist[x-1] == -1) {
            dist[x-1] = dist[x] + 1;
            parent[x-1] = x;
            q.push(x-1);
        }
    }

    vector<int> path;
    int cur = target;
    while (cur != -1) {
        path.push_back(cur);
        cur = parent[cur];
    }
    reverse(path.begin(), path.end());

    cout << dist[target] << "\n" 
}