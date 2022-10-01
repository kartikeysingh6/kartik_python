#include<bits/stdc++.h>
using namespace std;

void InsSort(int arr[],int n){
    for(int i=1;i<n;i++){
        int value=arr[i];
        int hole=i;
        while(hole>0 && arr[hole-1]>value){
            arr[hole]=arr[hole-1];
            hole--;
        }
        arr[hole]=value;
    }
}

//WOST: n*n AVG n*n BEST n(adaptive)
//InPlace 
//Stable
//Best so far it has very less shifts and comparisions hence used often in LL

int main(){
    int arr[]={3,2,1,8};
    int n=sizeof(arr)/sizeof(arr[2]);
    InsSort(arr,n);

    for(int &n:arr) cout<<n<<" ";
}