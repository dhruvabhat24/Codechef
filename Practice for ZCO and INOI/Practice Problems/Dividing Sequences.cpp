#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin>>n;
	vector<int>v1(n);
	for(int i=0;i<n;i++){
    	cin>>v1[i];
	}
	int fans = 1;
	vector<int>dp(n+1,1);
	for(int i=n-1;i>=0;i--){
    	for(int j=i+1;j<n;j++){
        	if(v1[j]%v1[i]==0){
            	dp[i] = max(dp[i],dp[j]+1);
        	}
    	}
    	fans = max(fans,dp[i]);
	}
	cout<<fans<<"\n";
}
