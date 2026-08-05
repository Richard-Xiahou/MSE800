#include <iostream>
#include <iomanip>

int main() {
    double weight, height, bmi;

    // 1. 输入体重和身高
    std::cout << "Please input your weight (kg): ";
    std::cin >> weight;
    std::cout << "Please input your height (m): ";
    std::cin >> height;

    // 2. 计算 BMI
    bmi = weight / (height * height);

    // 3. 输出结果，保留两位小数
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Your BMI is: " << bmi << std::endl;

    return 0;
}