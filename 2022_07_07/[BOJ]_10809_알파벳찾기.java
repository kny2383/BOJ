import java.util.Scanner;

public class Main {
	public static void main(String[] args) { 
		
		Scanner sc = new Scanner(System.in);
		String str = sc.next(); // 문자열 입력 받기
		String[] strArr = str.split(""); // 입력받은 문자열 한글자씩 split
		char[] ch = str.toCharArray(); // String -> char 변환
		char[] alphabet = new char[26]; // 알파벳 배열
		int[] result = new int[26]; // 알파벳이 단어에 포함되어 있는지 유무
		
		for (int i = 0; i < 26; i++) {
			alphabet[i] = (char)(i+97); // 아스키코드를 이용해 알파벳 담기
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

// 숏코딩
//import java.util.*;

//public class Main {
//	public static void main(String[] args) {
//		String s=new Scanner(System.in).nextLine();
		
//		for(int i='a';i<='z';i++) System.out.print(s.indexOf(i)+" ");
//	}
//}