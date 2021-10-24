#include <bits/stdc++.h>
using namespace std;
//This is exact problem of Target Sum
//There it is said that assign sign to elements +/- such that
//we achieve the given target sum
int static t[101][1001];

int countSubSum(int* arr,int n,int sum){
	for(int i=0;i<=n;i++){
		for(int j=0;j<=sum;j++){
			if(i==0)
				t[i][j]=0;
			if(j==0)
				t[i][j]=1;
		}
	}

	for(int i=1;i<=n;i++){
		for(int j=1;j<=sum;j++){

			if(t[i][j]!=-1)
				return t[i][j];

			if(arr[i-1]>j)
				t[i][j]=t[i-1][j];
			else
				t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j];

		}
	}

	return t[n][sum];

}

//s1-s2=diff
//s1+s2=sigma
//s1 = (sigma+diff)/2 and s2 = sigma-diff//2
//i.e find count of subset sum that can get sigma+diff//2
//NOTE: if sigma+diff is odd this means subsetsum will be in decimal which is impossilbe
// for set of integers to generate, so return 0
int countSubSumDiff(int* arr,int n,int diff){
	int sigma=0;
	for(int i=0;i<n;i++) sigma+=arr[i];

	if((sigma+diff)%2!=0)
		return 0;

	return countSubSum(arr,n,(sigma+diff)/2);
}

int main(){
	memset(t,-1,sizeof(t));
	int arr[]={1,1,2,3};
	int n=sizeof(arr)/sizeof(arr[0]);
	int diff=1;

	cout<<countSubSumDiff(arr,n,diff);
}