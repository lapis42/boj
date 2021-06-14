#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N, temp, count = 0;
    cin >> N;
    temp = N;

    do {
        temp = temp % 10 * 10 + (temp / 10 + temp % 10) % 10;
        count++;
    } while (temp != N);

    cout << count << endl;
    return 0;
}
