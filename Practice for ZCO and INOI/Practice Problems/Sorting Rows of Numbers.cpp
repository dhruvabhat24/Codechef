#include <bits/stdc++.h>
using namespace std;

int main() {
    // your code goes here
    int n;
    cin>>n;
    vector<vector<int>>v1;
    for(int i=0;i<n;i++){
    	vector<int>v2;
    	int num;
    	while(cin>>num){
        	if(num==-1){
            	v1.push_back(v2);
            	break;
        	}
        	v2.push_back(num);
    	}
    }
    sort(v1.begin(),v1.end());
    for(auto e:v1){
    	for(auto f:e){
        	cout<<f<<" ";
    	}
    	cout<<"\n";
    }

}
