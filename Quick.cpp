#include<bits/stdc++.h>
using namespace std;

int parti(int A[],int s,int e){
    swap(A[rand() %(e - s + 1) + s],A[e]);
    int pivot=A[e];
    int pindx=s;
    for(int i=s;i<=e;i++){
        if(A[i]<=pivot)
            swap(A[i],A[pindx++]);
    }
    return --pindx;
}

void QuickSort(int *A,int s,int e){
    if(s>=e)
        return;
    int pindx=parti(A,s,e);
    QuickSort(A,s,pindx-1);
    QuickSort(A,pindx+1,e);
}

//WOST: n*n AVG: nlogn BEST nlogn
//logn approx 1 aka Inplace
//Unstable
//Most prebuilt sorting algos uses this

int main(){
    int arr[]={3,2,1,8};
    int n=sizeof(arr)/sizeof(arr[2]);
    QuickSort(arr,n);

    for(int &n:arr) cout<<n<<" ";
}