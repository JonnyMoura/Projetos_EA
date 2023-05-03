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
int dfs[MAXN], low[MAXN];
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
            //SCCid[w] = SCCcount;
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
        for (int i = 0; i < N; i++) {
            SCC[i].clear();
        }
        for (int i = 1; i <= N; i++) {
            G[i].clear();
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
                    //cout << count << "--ct"<<endl;
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
            cout << "No cluster" << endl;
        }
        else {
            int ans = 0;
            for (int i = 0; i < SCCcount; i++) {
                int sum = 0;
                if (SCC[i].size() > 1) {
                    for (int u : SCC[i]) {
                        //cout << u << "-";
                        for (int k = 0; k < N; k++) {
                            sum += debt[k][u - 1] - debt[u - 1][k];
                        }

                    }
                    //cout << sum << endl;
                    int sum_pos = max(abs(sum), abs(ans));
                    if (abs(sum) == abs(ans)) {
                        ans = abs(sum);
                    } else if (sum_pos == abs(sum)) {
                        ans = sum;
                    } else if (sum_pos == abs(ans)) {
                        ans = ans;
                    }
                }
                //cout << sum << endl;
            }
            /*
            int sum = 0;
            for (int u : SCC[id]) {

                for (int k = 0; k < N; k++) {
                    sum += debt[k][u - 1] - debt[u - 1][k];
                }

            }
             */
            cout << ans << endl;
        }


    }
    return 0;
}