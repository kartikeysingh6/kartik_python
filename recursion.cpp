#include<bits/stdc++.h>
using namespace std;

//L5. Multiple Recursion Calls
//TC ~ O(2^n)
int fibonacci(int n)
{
	if(n==0 || n==1)
		return n;
	return fibonacci(n-1) + fibonacci(n-2);
}

//L6. Recursion on Subsequences
//TC ~ O(2^n)
void printSubsequences(int index,vector<int> &ds,vector<int> &array)
{
	if(index==array.size())
	{
		for(auto it:ds)
			cout<<it<<" ";
		cout<<endl;
		return;
	}
	ds.push_back(array[index]);
	printSubsequences(index+1,ds,array);

	ds.pop_back();
	printSubsequences(index+1,ds,array);
}

//L7. All Kind of Patterns in Recursion
//TC ~ O(2^n)
void sumEqualK(int index,vector<int> &ds,vector<int> &array,int sum,int k)
{
	if(index==array.size())
	{
		if(sum==k)
		{
			for(auto it:ds)
			cout<<it<<" ";
			cout<<endl;
		}
		return;
	}
	ds.push_back(array[index]);
	sum+=array[index];
	sumEqualK(index+1,ds,array,sum,k);

	sum-=array[index];
	ds.pop_back();
	sumEqualK(index+1,ds,array,sum,k);
}

bool sumEqualOnce(int index,vector<int> &ds,vector<int> &array,int sum,int k)
{
	if(index==array.size())
	{
		if(sum==k)
		{
			for(auto it:ds)
			cout<<it<<" ";
			cout<<endl;
			return true;
		}
		return false;
	}
	ds.push_back(array[index]);
	sum+=array[index];
	if(sumEqualOnce(index+1,ds,array,sum,k)==true)
		return true;

	sum-=array[index];
	ds.pop_back();
	if(sumEqualOnce(index+1,ds,array,sum,k)==true)
		return true;

	return false;
}

int countSumEqualK(int index,vector<int> &array,int sum,int k)
{
	if(index==array.size())
	{
		if(sum==k)
			return 1;
		return 0;
	}
	sum+=array[index];
	int l=countSumEqualK(index+1,array,sum,k);

	sum-=array[index];
	int r=countSumEqualK(index+1,array,sum,k);

	return l+r;
}

void withSpaces(string ip,string op,int n)
{
	if(n==0)
	{
		op.push_back(ip[0]);
		n++;
	}
	if(n==ip.size())
	{
		cout<<op<<endl;
		return;
	}

	string op1=op;
	string op2=op;
	op1.push_back(' ');
	op1.push_back(ip[n]);
	op2.push_back(ip[n]);
	n++;
	withSpaces(ip,op1,n);
	withSpaces(ip,op2,n);

}

void solve(string op,int one, int zero, int n)
{
	if(one+zero==n)
	{
		cout<<op<<endl;
		return;
	}
	string op1=op;
	op1.push_back('1');
	solve(op1,one+1,zero,n);

	if(one>zero)
	{
		string op2=op;
		op2.push_back('0');
		solve(op2,one,zero+1,n);
	}
}

int main()
{
	//cout<<fibonacci(6);
	//vector<int> test={3,1,2};
	//vector<int> ds;
	//printSubsequences(0,ds,test);
	//vector<int> test={1,1,1};
	//vector<int>ds;
	//sumEqualK(0,ds,test,0,3);
	//cout<<countSumEqualK(0,test,0,3);
	//string ip="ABCD";
	//string op="";
	//withSpaces(ip,op,0);

	string op="";
	solve(op,0,0,3);

	return 0;


}