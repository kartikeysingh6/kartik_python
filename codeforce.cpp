#include<bits/stdc++.h>
using namespace std;

int fact(int n)
{
	if(n==0 || n==1)
		return 1;
	return n*fact(n-1);
}

void insert_element(stack<int>& st,int temp)
{
	if(st.size()==0 || st.top()<=temp)
	{
		st.push(temp);
		return;
	}
	int val=st.top();
	st.pop();
	insert_element(st,temp);
	st.push(val);
}

void sort_stack(stack<int>& st)
{
	if(st.size()==1)
		return;
	int temp=st.top();
	st.pop();
	sort_stack(st);
	insert_element(st,temp);
}

void delete_middle(stack<int>& st,int k)
{
	if(k==1)
	{
		st.pop();
		return;
	}
	int temp=st.top();
	st.pop();
	delete_middle(st,k-1);
	st.push(temp);
}



int main()
{
	stack<int> s;
	s.push(1);
	s.push(2);
	s.push(3);
	s.push(4);
	s.push(5);
	s.push(6);
}