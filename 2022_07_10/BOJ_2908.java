import java.util.Scanner;

public class BOJ_2908 {
	public static void main(String[] args) { 
		
		Scanner sc = new Scanner(System.in);
		int a;
		int b;
		a = sc.nextInt();
		b = sc.nextInt();
		a = flip(a);
		b = flip(b);
		System.out.print(find_max(a, b));
	}
	
	public static int flip(int num) {
		int result = 0;
		while(num != 0) {
			result = result * 10 + num % 10;
			num /= 10;
		}
		return result;
	}
	
	public static int find_max(int a, int b) {
		if (a > b) return a;
		else return b;
	}
}