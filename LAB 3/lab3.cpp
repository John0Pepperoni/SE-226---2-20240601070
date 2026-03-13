#include <iostream>
using namespace std;


void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}


void printArray(int* arr, int size) {
    cout << "Array elements: " << endl;
    int *p = &arr[0];
    for (int i = 0; i < size; i++) {
        cout << *p << " ";
        p++;
    }
    cout << endl;
}


int findMax(int* arr, int size) {
    if (size <=0) {
        cout << "Invalid array size" << endl;
        return -1;
    }
    int max = arr[0];
    for (int i = 0; i < size; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }
    }
    return max;
}


void reverseArray(int* arr, int size) {
    if (size <=0) {
        cout << "Invalid array size" << endl;
        return;
    }
    int *p1 = &arr[0];
    int *p2 = &arr[size-1];
    while (p1 < p2) {
        swapValues(p1, p2);
        p1++;
        p2--;
    }
    cout << "Array after reverseArray:"<< endl;
    printArray(&arr[0], size);
}


int* createArray(int size) {
    if (size <=0) {
        cerr << "Invalid array size" << endl;
        return NULL;
    }
    int *p;
    p = new int[size];
    cout << "Enter values: " << endl;
    for (int i = 0; i < size; i++) {
        int val;
        cin >> val;
        p[i] = val;
    }
    return p;
}


void deleteArray(int* arr) {
    delete[] arr;
    cout << "Memory released successfully"<<endl;

}
int main() {
    cout << "Creating dynamic array..." << endl;
    cout << "Enter array size: ";
    int s;
    cin >> s;
    int* dynArray = createArray(s);

    printArray(dynArray, s);

    int dynArrMax = findMax(dynArray, s);
    cout << "Maximum element: " << dynArrMax << endl;

    cout << "------------" << endl;

    cout<< "Swapping two numbers" << endl;
    int a = 5;
    int b = 8;
    cout << "Before Swap \n" << "a = " <<  a << "\n "<< "b = " << b << endl;
    swapValues(&a, &b);
    cout << "After Swap \n" << "a = " <<  a << "\n "<< "b = " << b << endl;

    cout << "------------" << endl;

    cout << "Reversing array...";
    cout << endl;
    reverseArray(dynArray, s);

    cout << "------------" << endl;
    cout << "Deleting array..."<<endl;
    deleteArray(dynArray);

    return 0;
}
