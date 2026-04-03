#include <iostream>
#include <cmath>
using namespace std;
int a = 12345;


int calc_sum(int r, int n) {
    if (n==0) {return 1;}
    a = pow(r,n);
    int curr = a;
    return curr+ calc_sum(r, n-1);
}

int main() {
    int n = 0;
    cout << "Enter number of terms: ";
    cin >> n;
    cout << "Result: " << calc_sum(5, n) << endl;
}