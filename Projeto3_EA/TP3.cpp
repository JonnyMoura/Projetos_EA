#include <iostream>
#include <vector>
#include <stack>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 5005;
int N, t = 0, SCCcount = 0;
vector<int> G[MAXN];
vector<int> SCC[MAXN];
stack<int> S;
int dfs[MAXN], low[MAXN], SCCid[MAXN], indeg[MAXN], outdeg[MAXN];
bool instack[MAXN];

void Tarjan(int v) {
    low[v] = dfs[v] = t;
    t = t + 1;
    S.push(v);
    instack[v] = true;
    for (int i = 1; i < G[v].size(); i += 2) {
        int w = G[v][i];
        if (dfs[w] == -1) {
            Tarjan(w);
            low[v] = min(low[v], low[w]);
        }
        else if (instack[w]) {
            low[v] = min(low[v], dfs[w]);
        }
    }
    if (low[v] == dfs[v]) {
        int w;
        do {
            w = S.top();
            S.pop();
            instack[w] = false;
            SCCid[w] = SCCcount;
            SCC[SCCcount].push_back(w);
        } while (w != v);
        SCCcount++;
    }
}

int main() {
    while (cin >> N) {
        if (N == 0) break;
        vector<vector<int>> debt(N, vector<int>(N));
        t = 0, SCCcount = 0;
        memset(dfs, -1, sizeof dfs);
        memset(low, -1, sizeof low);
        memset(instack, false, sizeof instack);
        for (int i = 0; i <= N; i++) {
            if (i >= 1) {
                G[i].clear();
            }
            SCC[i].clear();
        }
        for_each(debt.begin(), debt.end(), [&](auto& row) { row.assign(N, 0); });
        for (int i = 1; i <= N; i++) {
            int a;
            cin >> a;
            int b;
            int count = 0;
            while (cin >> b) {
                if (b == 0) break;
                G[a].push_back(b);
                if (count % 2 != 0) {
                    debt[a - 1][b - 1] = G[a][count - 1];
                }
                count++;
            }
        }


        for (int i = 1; i <= N; i++) {
            if (dfs[i] == -1) {
                Tarjan(i);
            }
        }
        if (SCCcount == N) {
            cout << "No cluster\n";
        }
        else {
            size_t maior_cluster = 0;
            int id = -1;
            for (int i = 0; i < SCCcount; i++) {
                if (SCC[i].size() >= maior_cluster) {
                    maior_cluster = SCC[i].size();
                    id = i;
                }
            }
            int sum = 0;
            for (int j = 0; j < SCC[id].size(); j++) {

                int u = SCC[id][j];

                for (int k = 0; k < N; k++) {
                    sum += debt[k][u - 1] - debt[u - 1][k];
                }

            }
            cout << sum << endl;
        }


    }
    return 0;
}