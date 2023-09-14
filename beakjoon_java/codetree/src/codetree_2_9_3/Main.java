package codetree_2_9_3;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int asciiA = (int)'A';
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
				
		List<Integer> talkName = new ArrayList<>();
		List<Integer> talkNum = new ArrayList<>();
		
		for (int i = 0; i < m; i++) {
			String[] s = br.readLine().split(" ");
			talkName.add((int)s[0].charAt(0));
			talkNum.add(Integer.parseInt(s[1]));
		}
		
		int targetName = talkName.get(p - 1);
		int targetNum = talkNum.get(p - 1);
		if (targetNum == 0) System.exit(0);
		
		Set<Character> result = new HashSet<>();
		
		for (int i = asciiA; i < asciiA + n; i++) {
			if (!(talkName.subList(p - 1, talkName.size()).contains(i))) result.add((char)i);
		}
		
		for (int i = p - 2; i >= 0; i--) {
			if (talkNum.get(i) == targetNum) result.remove((char)(int)talkName.get(i));
		}
		
		List<Character> sortResult = result.stream()
										.sorted(Comparator.naturalOrder())
										.collect(Collectors.toList());
		for (char c : sortResult) System.out.print(c + " ");
	}

}
