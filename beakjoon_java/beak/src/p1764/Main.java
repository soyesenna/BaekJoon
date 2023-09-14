package p1764;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		
		List<String> inputNames = new ArrayList<>();
		List<String> result = new ArrayList<>();
		
		for (int i = 0; i < n + m; i++) {
			String now = br.readLine();
			if (inputNames.contains(now)) result.add(now);
			else inputNames.add(now);
		}
		
		
		result.sort((s1, s2) -> s1.charAt(0) - s2.charAt(0));
		
		System.out.println(result.size());
		for (String res : result) System.out.println(res);
		

	}

}
