// Created by Daifunny
#include <bits/stdc++.h>


using namespace std;
using ll = long long;

void fastio() {
	ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    }
int main(){
	fastio() ;
    #ifdef ONLINEJUDGE
        clock_t tStart = clock();
        freopen("TASK.inp","r",stdin); //can need to change file . this one for taking input
        freopen("TASK.out","w",stdout); // this one for output
    #endif
    
    // code here
    int n;
    cin >> n;
    for(int i=0; i<n; i++) {
    	cout << n << " ";
    }



  	#ifdef ONLINEJUDGE
    	fprintf(stderr, "\n>> Runtime: %.10fs\n", (double) (clock() - tStart) / CLOCKS_PER_SEC); // this line gives your code runtime
  	#endif
   	return 0;
}