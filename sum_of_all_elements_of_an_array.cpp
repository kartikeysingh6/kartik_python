#include <iostream>
using namespace std;

int main()
{
    int A[] = { 3,4,6,3,7,1,8,7,3 };
    int sum = 0;

    for (auto x : A)
    {
        sum += x;
    }

    cout << sum;

    return 0;
}
