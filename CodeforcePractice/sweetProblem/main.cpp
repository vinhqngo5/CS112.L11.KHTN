#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t-->0){
        int A[3];
        cin>>A[0]>>A[1]>>A[2];
        sort(A,A+3);
        if (A[2]>=A[1]+A[0]) cout<<A[1]+A[0]<<endl;
        else cout<<((A[1]+A[0])-(A[2]-(A[1]-A[0]))-(A[1]-A[0]))/2+A[2]<<endl;
    }
}
