#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double a, b;
    cin >> a >> b;
    cout << setprecision(10) << a / b;
    return 0;
}
