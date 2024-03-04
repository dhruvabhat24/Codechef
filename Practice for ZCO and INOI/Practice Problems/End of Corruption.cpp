#include <bits/stdc++.h>
using namespace std;

int main() {
	int n,m;
	cin>>n>>m;
	priority_queue<int>q1;
	for(int i = 0; i < n+m; i++){
    	int n1;
    	cin>>n1;
    	if(n1 == -1){
        	cout<<q1.top()<<"\n";
        	q1.pop();
    	}
    	else{
        	q1.push(n1);
    	}
	}

}
