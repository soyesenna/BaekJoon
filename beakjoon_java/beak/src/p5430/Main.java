package p5430;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		List<StringBuffer> result = new ArrayList<>();
		
		for (int i = 0; i < T; i++) {
			String p = br.readLine();
			int n = Integer.parseInt(br.readLine());
			
			//true : 정방향, false : 역방
			boolean flag = true;
			
			Deque<Integer> nowDeq = new ArrayDeque<>();
			
			String now = br.readLine();
			String[] numStr = now.substring(1, now.length() - 1).split(",");
			
			try {
				for (String s : numStr) nowDeq.add(Integer.parseInt(s));
			}catch(Exception e) {
				
			}
			
			
			if (n == 0) {
				if (p.contains("D")) result.add(new StringBuffer("error"));
				else result.add(new StringBuffer("[]"));
				continue;
			}
			
			boolean error = false;
			for (char order : p.toCharArray()) {
				if (order == 'R') {
					flag = !flag;
				}
				else {
					if (!delete(nowDeq, flag)) {
						result.add(new StringBuffer("error"));
						error = true;
						break;
					}
				}
			}
			if (!error)result.add(printDeq(nowDeq, flag));
		}
		
		for (StringBuffer s : result) System.out.println(s);
	}
	
	public static StringBuffer printDeq(Deque<Integer> deq, boolean flag) {
		StringBuffer result = new StringBuffer("[");
		if (deq.size() == 0) result.append("]");
		else {
			if (flag) while (deq.size() > 0) result.append(deq.pollFirst() + ",");
			else while (deq.size() > 0) result.append(deq.pollLast() + ",");
			
			result.deleteCharAt(result.length() - 1);
			result.append("]");
		}
		return result;
	}
	
	public static boolean delete(Deque<Integer> deq, boolean flag) {
		if (deq.size() == 0) return false;
		if (flag) deq.remove();
		else deq.removeLast();
		return true;
	}

}
