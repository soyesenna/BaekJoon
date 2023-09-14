package codetree_2_9_1;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		Map<Integer, Integer> birds = new HashMap<>();
		
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			String[] tmp = br.readLine().split(" ");
			int bird = Integer.parseInt(tmp[0]);
			int line = Integer.parseInt(tmp[1]);
			
			if (birds.containsKey(bird)){
				if (birds.get(bird) != line) {
					cnt++;
					birds.replace(bird, line);
				}
			}else birds.put(bird, line);
			
		}
		
		System.out.println(cnt);
	
	}

}
