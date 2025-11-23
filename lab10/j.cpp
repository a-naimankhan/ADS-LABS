#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> g(n+1);
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        g[x].push_back(y);
        g[y].push_back(x);
    }

    vector<bool> visited(n+1, false);
    int answer = 0;

    function<vector<int>(int)> get_component = [&](int start) {
        vector<int> comp;
        stack<int> st;
        st.push(start);
        visited[start] = true;

        while (!st.empty()) {
            int u = st.top(); st.pop();
            comp.push_back(u);
            for (int v : g[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    st.push(v);
                }
            }
        }
        return comp;
    };

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            vector<int> comp = get_component(i);

            int root = *min_element(comp.begin(), comp.end());

            // BFS to make the tree
            unordered_map<int,int> parent;
            unordered_map<int,int> children;
            for (int v : comp) children[v] = 0;

            queue<int> q;
            unordered_set<int> seen;
            q.push(root);
            seen.insert(root);
            parent[root] = -1;

            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : g[u]) {
                    if (!seen.count(v)) {
                        seen.insert(v);
                        parent[v] = u;
                        children[u]++;
                        q.push(v);
                    }
                }
            }

            // Count BigFam
            for (int v : comp) {
                if (v == root) answer++;
                else {
                    int p = parent[v];
                    if (children[v] > children[p])
                        answer++;
                }
            }
        }
    }

    cout << answer << "\n";
    return 0;
}
