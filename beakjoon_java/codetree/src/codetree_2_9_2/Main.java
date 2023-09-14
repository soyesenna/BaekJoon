package codetree_2_9_2;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		List<List<Integer>> homes = new ArrayList<>();

		for (int i = 0; i < 2; i++) {
			List<String> tmp = List.of(br.readLine().split(" "));
			homes.add(tmp.stream()
						.map((s) -> Integer.parseInt(s))
						.collect(Collectors.toList()));
		}
		
		
	}

}
