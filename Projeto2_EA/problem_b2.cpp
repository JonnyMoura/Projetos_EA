#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MOD = 1e9 + 7;

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


int count_schemes(vector<int>& prices, int k, int fee, long long int max_profit) {
    int n = prices.size();
    int max_buy = -prices[0] * k;
    int max_sell = 0;
    int count = 0;

    for (int i = 0; i < n; i++) {
        int buy_schemes = 0, sell_schemes = 0;
        if (prices[i] * k < max_sell) {
            continue;
        }
        for (int j = 0; j < n; j++) {
            if (prices[j] * k <= max_buy) {
                continue;
            }
            if (prices[i] * k - prices[j] * k > fee) {
                buy_schemes++;
                max_buy = max(max_buy, -prices[j] * k);
                max_sell = max(max_sell, prices[j] * k - fee * k); // atualiza max_sell após compra
            }
            else if (prices[j] * k - prices[i] * k > fee) {
                sell_schemes++;
                max_sell = max(max_sell, prices[j] * k - fee * k);
                max_buy = max(max_buy, -prices[i] * k); // atualiza max_buy após venda
            }
        }
        if (max_profit == (prices[i] * k + max_profit - max_sell)) {
            count = (count + buy_schemes + sell_schemes) % MOD;
        }
    }

    return count;
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
        if (task == 1 || task == 2) {
            max_profit(prices, K, R, task);
        }
        else if (task == 3) {
            long long int profit = max_profit(prices, K, R);
            int schemes = count_schemes(prices, K, R, profit);
            cout << profit << " " << schemes << endl;
        }


      }
    

    return 0;
}
