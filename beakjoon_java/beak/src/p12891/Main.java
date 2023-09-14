package p12891;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		
		String str = br.readLine();
		
		Map<Character, Integer> order = new HashMap<>();
		List<Character> keys = List.of('A', 'C', 'G', 'T');
		
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			order.put(keys.get(i), Integer.parseInt(st1.nextToken()));
		}
		
		int result = 0;
		
		for (int i = 0; i <= s - p; i++) {
			char[] sub = str.substring(i, i + p).toCharArray();
			
			List<Character> subList = new ArrayList<>();
			for (int k = 0; k < sub.length; k++) subList.add(sub[k]);
			
			boolean flag = true;
			for (int j = 0; j < 4; j++) {
				if (order.get(keys.get(j)) > Collections.frequency(subList, keys.get(j))) {
					flag = false;
					break;
				}
			}
			if (flag) result++;
		}
		System.out.println(result);
	}

}
