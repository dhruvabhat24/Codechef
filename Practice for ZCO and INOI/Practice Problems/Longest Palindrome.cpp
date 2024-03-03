#include <bits/stdc++.h>
using namespace std;
bool check(string &sub){
	int start = 0;
	int end = sub.length()-1;
	while(start<end){
    	if(sub[start]!=sub[end]){
        	return false;
    	}
    	start++;
    	end--;
	}
	return true;
}
int main() {
	int n;
	cin>>n;
	string s;
	cin>>s;
	int maxLength = 0;
	string subword = "";
	for(int i=0;i<n;i++){
   	 
    	for(int j=i;j<n;j++){
        	string sub = s.substr(i,j-i+1);
        	if(check(sub)){
            	int length = sub.length();
            	if(length>maxLength)
            	{
                	maxLength = length;
                	subword = sub;
            	}
        	}
    	}
	}
	cout<<maxLength<<"\n";
	cout<<subword<<"\n";

}
