#include<bits/stdc++.h>
using namespace std;

void swapXOR(int *a, int *b)
{
	*a=(*a)^(*b);
	*b=(*a)^(*b);
	*a=(*a)^(*b);
}

int setIthBit(int n,int i)
{
	return n|(1<<i);
}

int main()
{
	int N;
	cin>>N;
	cout<<N<<endl;
	cout<<setIthBit(N,2);


	//if(N%4==1)
	//	cout<<1;
	//else if(N%4==2)
	//	cout<<N+1;
	//else if(N%4==3)
	//	cout<<0;
	//else
	//	cout<<N;

	return 0;
}