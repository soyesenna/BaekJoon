package p1052;

import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		if (n <= k) {
			System.out.println(0);
			System.exit(0);
		}
		
		//key : 물 용량, value : 병 개
		Map<Integer, Integer> bottles = new HashMap<>();
		
		bottles.put(1, n);
		
		int newBottle = 0;
		
		while (bottles.values().stream().reduce(0, (a, b) -> a + b) > k) {
			for (int i = bottles.get(1); i < 2; i++) {
				bottles.replace(1, bottles.get(1) + 1);
				newBottle++;
			}
			List<Integer> keys = new ArrayList<>(bottles.keySet());
			keys.sort(Comparator.naturalOrder());
			//Map<Integer, Integer> tmp = new HashMap<>();
			for (int key : keys) {
				if (bottles.get(key) >= 2) {
					int nextKey = key * 2;
					int nextValue = (int) bottles.get(key) / 2;
					bottles.replace(key, bottles.get(key) % 2);
					
					if (bottles.containsKey(nextKey)) bottles.replace(nextKey, bottles.get(nextKey) + nextValue);
					else bottles.put(nextKey, nextValue);
				}

			}
		}
		System.out.println(newBottle);
	}

}
