// Scanner를 사용하기 위해서는 import를 통해 호출한다.
// java.util 패키지에 포함되어 있다.
import java.util.Scanner; 

public class BOJ_10430 {
	public static void main(String args[]) {
		// sc라는 객체를 생성하여 System.in으로 입력한 값을 바이트 단위로 읽는 것을 의미
		Scanner in = new Scanner(System.in); 
		int A = in.nextInt(); // 정수 A 입력 받기
		int B = in.nextInt(); // 정수 B 입력 받기
		int C = in.nextInt(); // 정수 C 입력 받기
		System.out.println((A+B)%C); 
		System.out.println(((A%C) + (B%C))%C);
		System.out.println((A*B)%C);
		System.out.println(((A%C) * (B%C))%C);
	}
}
	