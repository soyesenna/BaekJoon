
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		
		for(int i = 0; i < n; i++) {
			
			Deque<Character> stack = new ArrayDeque<>();
			
			char[] cArray = br.readLine().toCharArray();
			for (char c : cArray) {
				stack.add(c);
				if (stack.size() >= 2) {
					Character last1 = stack.pollLast();
					Character last2 = stack.pollLast();
					if (!(last1 == ')' && last2 == '(')) {
						stack.add(last2);
						stack.add(last1);
					}
				}
				
			}
			if (stack.size() == 0) System.out.println("YES");
			else System.out.println("NO");
			
		}
		
	}


}
