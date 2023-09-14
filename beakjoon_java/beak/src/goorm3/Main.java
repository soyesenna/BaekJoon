package goorm3;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		List<Integer> result = new ArrayList<>();

		for(int i = 0; i < t; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int first = Integer.parseInt(st.nextToken());
			String op = st.nextToken();
			int last = Integer.parseInt(st.nextToken());
			
			switch(op) {
			case "+":
				result.add(first + last);
				break;
			case "*":
				result.add(first * last);
				break;
			case "-":
				result.add(first - last);
				break;
			case "/":
				result.add((int) first / last);
				break;
			}
		}
		
		int sumResult = result.stream()
							.reduce(0, (a, b) -> a + b);
		System.out.println(sumResult);
		
	}

}
