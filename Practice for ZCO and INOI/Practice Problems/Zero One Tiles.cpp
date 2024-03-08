#include <iostream>
using namespace std;

int main() {
    // your code goes here
    int n;
    cin>>n;
    int dp[n+1];
    dp[0] = 1;
    dp[1] = 1;
    for(int i=2;i<=n;i++)
    {
    	dp[i] = (dp[i-1] + dp[i-2]) % 15746;
    }
    cout<<dp[n]%15746<<endl;
    return 0;
}
