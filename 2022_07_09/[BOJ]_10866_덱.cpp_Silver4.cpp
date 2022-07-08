#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int deque[10001];
int k; // ���� ũ��

int main() {
	int cmd = 0; // ����� ��
	cin >> cmd;
	string str; // ��ɾ�

	for (int i = 0; i < cmd; i++) {
		cin >> str;

		if (str == "push_front") {
			int n;
			cin >> n;

			if (k != 0) { // �̹� ���� ���� ������ ���
				for (int i = k - 1; i >= 0; i--) {
					deque[i + 1] = deque[i]; // ������ �ִ� ������ ��ĭ�� �̵���Ų��
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

			if (k == 0) { // ���� ����ִ� ������ ���� ���
				cout << "-1" << endl;
			}
			else {
				cout << deque[0] << endl;
				for (int i = 1; i < k; i++) {
					deque[i - 1] = deque[i]; // ������ �ִ� ������ ��ĭ�� �մ���.					
				}
				k--;
			}
		}

		else if (str == "pop_back") {

			if (k == 0) { // ���� ����ִ� ������ ���� ���
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
			if (k == 0) { // ���� ����ִ� ������ ���� ���
				cout << "-1" << endl;
			}
			else
				cout << deque[0] << endl;
		}

		else if (str == "back") {
			if (k == 0) { // ���� ����ִ� ������ ���� ���
				cout << "-1" << endl;
			}
			else {
				cout << deque[k-1] << endl;
			}
		}
	}
	return 0;
}