#include <iostream>
using namespace std;

int queue[10001];
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
			queue[k] = n;
			k++;
		}

		else if (str == "pop") {

			if (k == 0) { // 스택에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << queue[0] << endl;
				for (int i = 1; i < k; i++) {
					queue[i - 1] = queue[i]; // 기존에 있던 값들을 한칸씩 앞당긴다.					
				}
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
			if (k == 0) { // 스택에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << queue[0] << endl;
			}
		}

		else if (str == "back") {
			if (k == 0) { // 스택에 들어있는 정수가 없는 경우
				cout << "-1" << endl;
			}
			else {
				cout << queue[k - 1] << endl;
			}
		}
	}
	return 0;
}