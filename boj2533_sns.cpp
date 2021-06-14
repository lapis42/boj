#include <iostream>
#include <vector>
using namespace std;

const int max_n = 1000001;
int n, dp[max_n][2];
bool visited[max_n];
vector<int> graph[max_n];

void dfs(int i) {
    visited[i] = true;
    dp[i][0] = 0;
    dp[i][1] = 1;

    for (int j : graph[i]) {
        if (!visited[j]) {
            dfs(j);
            dp[i][0] += dp[j][1];
            dp[i][1] += min(dp[j][0], dp[j][1]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 1; i < n; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    dfs(1);
    cout << min(dp[1][0], dp[1][1]) << endl;

    return 0;
}
