// Problem : https://codeforces.com/problemset/problem/977/A

#include<iostream>
int main(void){
    int n, k;
    std::cin >> n >> k;
    for(int i=0; i<k; i++){
        if(n%10 == 0){
            n = n/10;
        }
        else {
            n--;
        }
    }
    std::cout << n;
    return 0;
}