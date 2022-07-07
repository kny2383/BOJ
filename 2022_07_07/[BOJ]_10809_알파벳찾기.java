import java.util.Scanner;

public class Main {
	public static void main(String[] args) { 
		
		Scanner sc = new Scanner(System.in);
		String str = sc.next(); // ���ڿ� �Է� �ޱ�
		String[] strArr = str.split(""); // �Է¹��� ���ڿ� �ѱ��ھ� split
		char[] ch = str.toCharArray(); // String -> char ��ȯ
		char[] alphabet = new char[26]; // ���ĺ� �迭
		int[] result = new int[26]; // ���ĺ��� �ܾ ���ԵǾ� �ִ��� ����
		
		for (int i = 0; i < 26; i++) {
			alphabet[i] = (char)(i+97); // �ƽ�Ű�ڵ带 �̿��� ���ĺ� ���
		}
		
		for (int j = 0; j < 26; j++) {
			for (int k = 0; k < strArr.length; k++) {
				if (alphabet[j] == ch[k]) {
					result[j] = k;
					break;
				}
				else {
					result[j] = -1;
				}
			}
		}
		
		for (int k = 0; k < 26; k++) {
			System.out.print(result[k]+" ");
		}
	}
}

// ���ڵ�
//import java.util.*;

//public class Main {
//	public static void main(String[] args) {
//		String s=new Scanner(System.in).nextLine();
		
//		for(int i='a';i<='z';i++) System.out.print(s.indexOf(i)+" ");
//	}
//}