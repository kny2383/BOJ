import java.util.Scanner;

public class Main {
	public static void main(String[] args) { 
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 숫자의 개수
		String a = sc.next(); // 더할 숫자
		sc.close();
		int sum = 0; // 합
		
		for(int i = 0; i < n; i++) {
			sum += a.charAt(i)-'0'; 
			// charAt()은 해당 문자의 아스키코드 값을 반환해서 반드시 -48 또는 -'0'을 해줘야 입력받은 숫자 값을 그대로 사용할 수 있다.
		}
		System.out.println(sum);
	}
}
