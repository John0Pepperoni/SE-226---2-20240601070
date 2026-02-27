#include <iostream>
#include <cmath>
using namespace std;
int main() {
int x1{};
int y1{};
int x2{};
int y2{};

cout << "Enter x coordinate for first point: "<< endl;
cin >> x1;
cout << "Enter y coordinate for first point: "<< endl;
cin >> y1;
cout << "Enter x coordinate for second point: "<< endl;
cin >> x2;
cout << "Enter y coordinate for second point: "<< endl;
cin >> y2;

double distance = pow((pow((x2-x1),2) + pow((y2-y1),2)),0.5);
cout << distance << endl;

return 0;
}