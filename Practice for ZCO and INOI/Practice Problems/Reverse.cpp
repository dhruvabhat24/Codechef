#include <bits/stdc++.h>
using namespace std;

int main() {

	int n;
	cin >> n;
	vector<string> v;
	string in;
	while(cin >> in){
    	v.push_back(in);
	}
	reverse(v.begin(), v.end());

	for(int i=0; i<v.size(); i++){

    	for(int j=0; j<v[i].size(); j++){

        	if (v[i][j] == '\'' || v[i][j] == '.' || v[i][j]==',' || v[i][j]==';' || v[i][j]==':'){
            	continue;
        	}
        	else {
            	cout << v[i][j];
        	}
    	}
    	cout << " ";
	}
    return 0;

}
