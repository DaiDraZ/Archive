// #include <bits/stdc++.h>
// #include <string>
// #include <stdio.h>



#include <vector>
#include <math.h>
#include <iostream>
#include <map>
#define LL long long
#define LLI long long int
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))



//C:/MinGW/lib/gcc/mingw32/6.3.0/include

const LL oo=1e12;


long long a[1000000];

using namespace std;

bool prime(long long n) {
    if (n < 2) return false;
    if (n == 2 or n == 3) return true;
    if (n%2 == 0 or n%3 == 0) return false;
    int k = sqrt(n);
    for(int i = 5;i < k;i += 6){
        if (n%i == 0 or n%(i + 2) == 0) return false; 
    }
    return true;
}

void fastio() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);}

int main() {
	long long n;cin >> n;
    cout << prime(n) << endl;
    return 0;}
