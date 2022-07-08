#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int deque[10001];
int k; // 덱의 크기

int main() {
	int cmd = 0; // 명령의 수
	cin >> cmd;
	string str; // 명령어

	for (int i = 0; i < cmd; i++) {
		cin >> str;

		if (str == "push_front") {
			int n;
			cin >> n;

			if (k != 0) { // 이미 덱에 값이 존재할 경우
				for (int i = k - 1; i >= 0; i--) {
					deque[i + 1] = deque[i]; // 기존에 있던 값들을 한칸씩 이동시킨다
				}
			}
			deque[0] = n;
			k++;
		}

		else if (str == "push_back") {
			int n;
			cin >> n;
			deque[k] = n;
			k++;
		}

		else if (str == "pop_front") {

			if (k == 0) { // 덱에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << deque[0] << endl;
				for (int i = 1; i < k; i++) {
					deque[i - 1] = deque[i]; // 기존에 있던 값들을 한칸씩 앞당긴다.					
				}
				k--;
			}
		}

		else if (str == "pop_back") {

			if (k == 0) { // 덱에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << deque[k-1] << endl;
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

		else if (str == "front") {
			if (k == 0) { // 덱에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else
				cout << deque[0] << endl;
		}

		else if (str == "back") {
			if (k == 0) { // 덱에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << deque[k-1] << endl;
			}
		}
	}
	return 0;
}