import java.util.Scanner;

public class BOJ_2675{
	public static void main(String[] args) { 
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); // �׽�Ʈ ���̽� ����
		int r = 0; // �ݺ� Ƚ�� r
		String s; // ���ڿ� s 
		StringBuilder sb = new StringBuilder(20); // ���� ������ ���ڿ��� ������ش�.
		
		for (int i = 0; i < T; i++) {
			r = sc.nextInt();
			s = sc.next();
			String str[] = s.split(""); // ���ڿ� �ɰ���
			for (int j = 0; j < str.length; j++) {
				for (int k = 0; k < r; k++) {
					sb.append(str[j]); // ���ڿ� r��ŭ �ݺ�
				}
			}
			System.out.println(sb);
			sb.setLength(0); // StringBuilder ��ü sb �ʱ�ȭ
		}
	}
}