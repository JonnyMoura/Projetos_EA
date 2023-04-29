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
    for (int i = 0; i < G[v].size(); i++) {
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
        t = 0, SCCcount = 0;
        memset(dfs, -1, sizeof dfs);
        memset(low, -1, sizeof low);
        memset(instack, false, sizeof instack);
        for (int i = 1; i <= N; i++) {
            G[i].clear();
            SCC[i].clear();
        }

        for (int i = 1; i <= N; i++) {
            int a;
            cin >> a;
            int b;
            while (cin >> b) {
                if (b == 0) break;
                G[a].push_back(b);
            }
        }

        for (int i = 1; i <= N; i++) {
            if (dfs[i] == -1) {
                Tarjan(i);
            }
        }

        if (SCCcount == 1) {
            cout << "No cluster\n";
            continue;
        }
        memset(indeg, 0, sizeof indeg);
        memset(outdeg, 0, sizeof outdeg);
        for (int i = 0; i < SCCcount; i++) {
            for (int j = 0; j < SCC[i].size(); j++) {
                int u = SCC[i][j];
                for (int k = 0; k < G[u].size(); k++) {
                    int v = G[u][k];
                    if (SCCid[u] != SCCid[v]) {
                        indeg[SCCid[v]]++;
                        outdeg[SCCid[u]]++;
                    }
                }
            }
        }

        int maxIndeg = 0, maxOutdeg = 0;
        for (int i = 0; i < SCCcount; i++) {
            if (indeg[i] == 0) maxIndeg++;
            if (outdeg[i] == 0) maxOutdeg++;
        }
        int result = max(maxIndeg, maxOutdeg);
        if (SCCcount == 2 && maxIndeg == 1 && maxOutdeg == 1) {
            // special case where there are only two SCCs and they are connected
            result = 0;
        }
        cout << result << endl;
    }
    return 0;
}
