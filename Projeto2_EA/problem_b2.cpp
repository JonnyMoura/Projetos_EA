#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



void max_profit(vector<int>& prices, int k, int fee, int task) {
    int n = prices.size();
    vector<vector<long long int>> dp(n, vector<long long int>(2, 0));
    vector<int> path(n);
    dp[0][0] = -prices[0] * k;
    dp[0][1] = 0;

    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] * k);
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] * k - fee * k);
    }
    cout << dp[n-1][1] << endl;
    if (task == 2) {
        bool sell = false;
        for (int day = n - 1; day > 0; day--) {
            if (!sell && dp[day][1] > dp[day - 1][1]) {
                path[day] = -k;
                sell = true;
                continue;
            }
            if (sell && dp[day][0] > dp[day - 1][0]) {
                path[day] = k;
                sell = false;
            }
        }
        if (sell) {
            path[0] = k;
        }

        for (int d = 0; d < n; d++) {
            cout << path[d] << " ";
        }
        cout << endl;
    }
}

int main() {
    int task;
    cin >> task;


    int N, D, K, R;
    cin >> N >> D >> K >> R;

    for (int j = 0; j < N; j++) {
         vector<int> prices(D);
         for (int k = 0; k < D; k++) {
                cin >> prices[k];
          }
         max_profit(prices, K, R,task);


      }
    

    return 0;
}
