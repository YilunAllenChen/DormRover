#include <iostream>

using namespace std;

int add(int i, int j) {
    return i + j;
}


extern "C" {
    int add_extern(int i, int j){
        return i + j;
    }

    int print_content(char * str){
        cout << str << endl;
        return 0;
    }
}