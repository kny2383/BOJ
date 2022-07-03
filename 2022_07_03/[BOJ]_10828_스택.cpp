#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int arr[10001];
int k; // 스택의 크기

int main() {
	int n = 0; // 명령의 수
	cin >> n;
	string str; // 명령어
	
	for (int i = 0; i < n; i++) {
		cin >> str;

		if (str == "push") {
			int n;
			cin >> n;
			arr[k] = n;
			k++;
		}

		else if (str == "pop") {

			if (k == 0) { // 스택에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << arr[k - 1] << endl;
				k--;
			}
		}

		else if (str == "size") {
			cout << k << endl;
		}

		else if (str == "empty") {
			if (k == 0) {
				cout << "1" << endl;
			}
			else
				cout << "0" << endl;
		}

		else if (str == "top") {
			if (k == 0) { // 스택에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << arr[k - 1] << endl;
			}
		}
	}
	return 0;
}