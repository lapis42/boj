#include <bits/stdc++.h>
using namespace std;

const int max_n = 500000;
int t, n, m, cnt, s, p;
int visited[max_n], cash[max_n], restaurant[max_n], r_scc[max_n], dp[max_n];
vector<int> st, sum_scc;
vector<vector<int>> g(max_n), gr(max_n);
vector<set<int>> g_scc(max_n);

void dfs(int i) {
    visited[i] = 1;
    for (int j : g[i])
        if (!visited[j]) dfs(j);
    st.push_back(i);
}

int dfs_rev(int i) {
    int ans = cash[i];
    visited[i] = cnt;
    for (int j : gr[i])
        if (!visited[j]) ans += dfs_rev(j);
    return ans;
}

int dfs_cash(int *dp, int i) {
    if (dp[i] == -1) {
        int temp = 0;
        for (int j : g_scc[i])
            temp = max(dfs_cash(dp, j), temp);
        if ((temp == 0) && (r_scc[i] == 0))
            dp[i] = 0;
        else {
            dp[i] = sum_scc[i] + temp;
        }
    }
    return dp[i];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // input
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g[a - 1].push_back(b - 1);
        gr[b - 1].push_back(a - 1);
    }

    for (int i = 0; i < n; i++) cin >> cash[i];
    cin >> s >> p;

    for (int i = 0; i < p; i++) {
        int c;
        cin >> c;
        restaurant[c - 1] = 1;
    }

    // Kosaraju's algorithm
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);
        }
    }

    memset(visited, 0, sizeof(visited));
    for (int i = n - 1; i > -1; i--) {
        if (!visited[st[i]]) {
            cnt++;
            sum_scc.push_back(dfs_rev(st[i]));
        }
    }

    // graph between scc
    for (int i = 0; i < n; i++) {
        for (int j : g[i])
            if (visited[i] != visited[j])
                g_scc[visited[i] - 1].insert(visited[j] - 1);
        if (restaurant[i]) r_scc[visited[i] - 1] = 1;
    }

    memset(dp, -1, sizeof(dp));
    cout << dfs_cash(dp, visited[s - 1] - 1) << endl;

    return 0;
}
