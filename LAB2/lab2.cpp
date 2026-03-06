#include <iostream>
using namespace std;
int main() {
    int num{};
    int sum{0};
    int temp{};
    std::cout << "Please enter a positive integer greater than 9: ";
    std::cin >> num;
    while (num <= 9) {
        std::cout << "Invalid input. Please enter a positive integer greater than 9: ";
        std:: cin >> num;
    }
    temp = num;
    std::cout << temp;

    while (temp > 9) {
        int sum = 0;
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        temp = sum;
        std::cout << " -> " << sum;
    }
    std::cout << std::endl;




    // Task 2
    int val{};
    int count{1};
    std::cout << "Please enter a positive integer between 1 and 100: ";
    std::cin >> val;
    while (val < 10 || val > 100) {
        std::cout << "Invalid input. Please enter a positive integer between 1 and 100: ";
        std::cin >> val;
    }
    int fizzSteps{0};
    int buzzSteps{0};
    int fizzBuzzSteps{0};

    while (count <= val) {
        if (count % 7 == 0) {
            std::cout << "(" << count << " is skipped)" << std::endl;
            count++;
            continue;
        }
        if (count % 3 == 0) {
            if (count % 5 == 0) {
                std::cout << "FizzBuzz" << std::endl;
                fizzBuzzSteps++;
            } else {
                std::cout << "Fizz" << std::endl;
                fizzSteps++;
            }
        } else if (count % 5 == 0) {
            std::cout << "Buzz" << std::endl;
            buzzSteps++;
        } else {
            std::cout << count << std::endl;
        }
        count++;

    }
    std::cout << "----- Summary -----"<< std::endl;
    std::cout << "Fizz count: " << fizzSteps << std::endl;
    std::cout << "Buzz count: " << buzzSteps << std::endl;
    std::cout << "FizzBuzz count: " << fizzBuzzSteps << std::endl;




    // Task 3
    int pat{0};
    std::cout << "Please enter a number between 3 and 9:";
    std::cin >> pat;
    while (pat < 3 || pat > 9) {
        std::cout << "Invalid input. Please enter a number between 3 and 9:";
    }
    int i{1};
    while (i <= 2*pat-1) {
        int k = pat - abs(pat -i);
        for (int j = 1; j <= k; j++) {
            std::cout << j;
        }
        std::cout << std::endl;
        i++;
        if (i <1) {
            break;
        }
    }

    return 0;
}