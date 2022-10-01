#include<bits/stdc++.h>
using namespace std;

class A{
	int a;
public:
	void f1(){cout<<"Af1\n";}
	virtual void f2(){cout<<"Af2\n";}
	virtual void f3(){cout<<"Af3\n";}
};

class B:public A{
	int b;
public:
	void f1(){cout<<"Bf1\n";}
	void f2(){cout<<"Bf2"<<endl;}
	void f3(int x=0){cout<<"Bf3 "<<x<<"\n";}			//vTable | f2,points to B | f3(NOT f3(int)),point to A |
};

main(){
	A *p,obj1;
	B obj2;
	p=&obj2;
	p->f1();
	p->f2();
	p->f3();
}
