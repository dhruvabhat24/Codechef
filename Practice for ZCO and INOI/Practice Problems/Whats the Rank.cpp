#include <bits/stdc++.h>
using namespace std;

int main() {
    // your code goes here
    int n;
    cin>>n;
    vector<int>v1;
    for(int i=0;i<n;i++){
    	int n1;
    	cin>>n1;
    	int rank = 1;
    	for(auto e:v1){
        	if(e>n1)rank++;
    	}
    	cout<<rank<<"\n";
    	v1.push_back(n1);
    }

}
