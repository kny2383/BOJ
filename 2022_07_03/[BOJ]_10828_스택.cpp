#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int arr[10001];
int k; // ������ ũ��

int main() {
	int n = 0; // ����� ��
	cin >> n;
	string str; // ��ɾ�
	
	for (int i = 0; i < n; i++) {
		cin >> str;

		if (str == "push") {
			int n;
			cin >> n;
			arr[k] = n;
			k++;
		}

		else if (str == "pop") {

			if (k == 0) { // ���ÿ� ����ִ� ������ ���� ���
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
			if (k == 0) { // ���ÿ� ����ִ� ������ ���� ���
				cout << "-1" << endl;
			}
			else {
				cout << arr[k - 1] << endl;
			}
		}
	}
	return 0;
}