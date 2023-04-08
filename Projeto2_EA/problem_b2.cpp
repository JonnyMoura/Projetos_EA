#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



long long int max_profit(vector<int>& prices, int k, int fee) {
    int n = prices.size();
    vector<vector<long long int>> dp(n, vector<long long int>(2, 0));

    dp[0][0] = -prices[0] * k;
    dp[0][1] = 0;

    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] * k);
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] * k - fee * k);
    }

    return dp[n - 1][1];
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
         if (task == 1) {
             long long int profit = max_profit(prices, K, R);
             cout << profit << endl;
         }
      }
    

    return 0;
}
