#include<bits/stdc++.h>
using namespace std;

class Complex{
	int a,b;
public:
	Complex(int x=0,int y=0){a=x;b=y;}	//default,parameterized and c=4 all will be handeled by this
	void show(){cout<<a<<"+i"<<b;}
	operator int(){
		return sqrt(a*a +b*b);
	}
};


main(){
	Complex c1(9,12);
	Complex c2;
	int x,y=12;
	x=c1;
	c2=y;

	cout<<x<<endl;
	c2.show();

}