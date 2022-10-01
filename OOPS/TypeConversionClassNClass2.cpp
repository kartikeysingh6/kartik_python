#include<bits/stdc++.h>
using namespace std;

class Imaginary;

class Complex{
	int a,b;
public:
	Complex(int x=0,int y=0){a=x;b=y;}	//default,parameterized and c=4 all will be handeled by this
	void show(){cout<<a<<"+i"<<b;}
	friend class Imaginary;
};

class Imaginary{
	int b;
public:
	Imaginary(int x=0){b=x;}
	Imaginary(Complex cn){b=cn.b;}	//cn.b won't be accessible like this so we have 3 options
	void show(){cout<<b;}			//1.Make b public 2.Make Imaginary a friend class in Complex 3. Create getB() in Complex
};

main(){
	Complex c1(9,12);
	Imaginary i1;
	i1=c1;	//i1 should be able to handle c1 type
	i1.show();

}