#include <iostream>
using namespace std;

int main() {
int secs{};
cout << "Enter seconds: "<< endl;
cin >> secs;

if (secs <0) {
    cout << "time can't be smaller than 0 seconds";
    return 1;
}

int hours = (secs/3600);
int minutes = ((secs%3600)/60);
int seconds = secs%60;

cout << secs << " seconds is " << hours << " hours, " << minutes << " minutes, and " << seconds << " seconds." << endl;

    return 0;
}