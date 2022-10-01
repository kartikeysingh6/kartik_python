#include<bits/stdc++.h>
using namespace std;

template <class X> class ArrayList{
private:
	struct Block{
		int size;
		X* arr_ptr;
	};
	Block* s;
public:
	ArrayList(int capacity=0){
		s=new Block;
		s->size=capacity;
		s->arr_ptr=new X[s->size];
	}

	void push(int indx,X value){
		if(indx>=0 && indx<s->size)
			s->arr_ptr[indx]=value;
		else
			cout<<"Invalid Index\n";
	}

	void show(int indx,X &data){
		if(indx>=0 && indx<s->size)
			data=s->arr_ptr[indx];
		else
			cout<<"Invalid Index\n";
	}
	void viewAll(){
		for(int i=0;i<s->size;i++)
			cout<<s->arr_ptr[i]<<", ";
	}
};

main(){
	int data;
	ArrayList <double> list1(4);
	list1.push(0,9.4);
	list1.push(1,5.9);
	list1.push(2,15.13);
	list1.push(3,5.6);
	//list1.show(3,data);
	list1.viewAll();
	//cout<<data;
}