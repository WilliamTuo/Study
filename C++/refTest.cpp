#include <iostream>

struct Test {
    int t_;

    Test (int t): t_(t) {}
};

Test& TestFunc(Test& t) {
    return t;
}

int main() {
    Test t(10);
    Test t1 = TestFunc(t);

    return 0;
}