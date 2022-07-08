import java.util.Scanner;

public class BOJ_2675{
	public static void main(String[] args) { 
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); // 테스트 케이스 개수
		int r = 0; // 반복 횟수 r
		String s; // 문자열 s 
		StringBuilder sb = new StringBuilder(20); // 변경 가능한 문자열을 만들어준다.
		
		for (int i = 0; i < T; i++) {
			r = sc.nextInt();
			s = sc.next();
			String str[] = s.split(""); // 문자열 쪼개기
			for (int j = 0; j < str.length; j++) {
				for (int k = 0; k < r; k++) {
					sb.append(str[j]); // 문자열 r만큼 반복
				}
			}
			System.out.println(sb);
			sb.setLength(0); // StringBuilder 객체 sb 초기화
		}
	}
}