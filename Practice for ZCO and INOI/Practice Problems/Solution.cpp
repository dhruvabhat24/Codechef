#include <bits/stdc++.h>
using namespace std;

void nextPermutation(vector<int>& arr)
{
	int n = arr.size(), i, j;
 
	// Find for the pivot element.
	// A pivot is the first element from
	// end of sequenc ewhich doesn't follow
	// property of non-increasing suffix
	for (i = n - 2; i >= 0; i--) {
    	if (arr[i] < arr[i + 1]) {
        	break;
    	}
	}
 
	// Check if pivot is not found
	if (i < 0) {
    	reverse(arr.begin(), arr.end());
	}
 
	// if pivot is found
	else {
 
    	// Find for the successor of pivot in suffix
    	for (j = n - 1; j > i; j--) {
        	if (arr[j] > arr[i]) {
            	break;
        	}
    	}
 
    	// Swap the pivot and successor
    	swap(arr[i], arr[j]);
 
    	// Minimise the suffix part
    	reverse(arr.begin() + i + 1, arr.end());
	}
}
int main() {
	int n,m;
	cin>>n>>m;
	for(int i=0; i<m; i++){
    	vector<int>v1(n);
    	for(int j=0; j<n; j++){
        	cin>>v1[j];
    	}
    	nextPermutation(v1);
    	for(auto e:v1){
        	cout<<e<<" ";
    	}
    	cout<<"\n";
   	 
	}

}
