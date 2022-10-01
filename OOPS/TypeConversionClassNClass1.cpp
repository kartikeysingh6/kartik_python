#include<bits/stdc++.h>
using namespace std;

class Imaginary{
	int b;
public:
	Imaginary(int x=0){b=x;}
	void show(){cout<<b;}
};	//so that compiler understands Imaginary meaning in Complex class

class Complex{
	int a,b;
public:
	Complex(int x=0,int y=0){a=x;b=y;}	//default,parameterized and c=4 all will be handeled by this
	void show(){cout<<a<<"+i"<<b;}
	operator Imaginary(){
		Imaginary i(b);
		return i;
	}
};


main(){
	Complex c1(9,12);
	Imaginary i1;
	i1=c1;	//c1 should return Imaginary type value such that i1 can handle it
	i1.show();

}