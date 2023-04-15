#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long int max_profit(vector<int>& prices, int k, int fee, int task) {
    int n = prices.size();
    vector<vector<long long int>> dp(n, vector<long long int>(2, 0));
    vector<int> path(n);
    dp[0][0] = -prices[0] * k;
    dp[0][1] = 0;

    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] * k);
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] * k - fee * k);
    }
    if (task == 2 || task ==1) {
        cout << dp[n - 1][1] << endl;
    }
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
    return dp[n-1][1];
}


void count_schemes(vector<int> & prices, long long int k, long long int fee) {
    size_t n = prices.size();
    std::vector<std::vector<long long int>> dp(n, std::vector<long long int>(k + 1, 0));
    vector<vector<long long int>> count(n, vector<long long int>(k + 1, 0));
    const int MOD = 1000000007;


    for (int j = 0; j <= k; j++) {
        dp[0][j] = -prices[0] * j - fee * j;
        count[0][j] = 1;
    }

    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= k; j++) {

            // Compra ações
            long long int py2 = dp[i - 1][j];
            long long int count2 = count[i - 1][j];
            for (int m = 1; m <= j; m++) {
                long long int new_profit = dp[i - 1][j - m] - prices[i] * m - fee * m;
                if (new_profit > py2) {
                    py2 = new_profit;
                    count2 = count[i - 1][j - m];
                }
                else if (new_profit == py2) {
                    count2 = (count2 + count[i - 1][j - m]);
                }
            }

            // Vende ações
            long long int py3 = dp[i - 1][j];
            long long int count3 = count[i - 1][j];

            for (int m = 1; m <= k - j; m++) {
                long long int new_profit = dp[i - 1][j + m] + prices[i] * m;
                if (new_profit > py3) {
                    py3 = new_profit;
                    count3 = count[i - 1][j + m];
                }
                else if (new_profit == py3) {
                    count3 = (count3 + count[i - 1][j + m]);
                }
            }

            dp[i][j] = max( py2, py3);
            if( dp[i][j] == py2 && dp[i][j] == py3){
                count[i][j] = max(count2,count3);
            }else if(dp[i][j] == py2 ){
                count[i][j] = count2;
            }else{
                count[i][j] = count3;
            }

        }
    }
    long long int best_profit = dp[n - 1][0];
    long long int num_schemes = count[n - 1][0] % MOD;

    cout << best_profit << " " << num_schemes << endl;

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
        } else if (task == 3) {
            count_schemes(prices, K, R);
        }
    }

    return 0;
}
