package goorm4;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		List<Integer> ham = new ArrayList<>();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) ham.add(Integer.parseInt(st.nextToken()));
		
		int max = Collections.max(ham);
		
		boolean flag = true;
		
		int result = 0;
		int before = 0;
		for (int now : ham) {
			if (flag) {
				if (now >= before) result += now;
				else {
					result = 0;
					break;
				}
			}else {
				if (now <= before) result += now;
				else {
					result = 0;
					break;
				}
			}
			before = now;
			if (before == max) flag = false;
		}
		System.out.println(result);
	}

}
