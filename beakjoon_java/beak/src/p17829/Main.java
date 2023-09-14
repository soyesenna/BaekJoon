package p17829;

import java.io.*;
import java.util.*;

public class Main {
	
	public static List<List<Integer>> map = new ArrayList<>();

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			List<Integer> tmp = new ArrayList<>();
			for (int j = 0; j < n; j++) tmp.add(Integer.parseInt(st.nextToken()));
			
			map.add(tmp);
		}
		
		while(map.size() > 1) doPooling(map.size());
		
		System.out.println(map.get(0).get(0));
		
	}
	
	public static void doPooling(int n) {
		List<List<Integer>> newMap = new ArrayList<>();
		for (int i = 0; i < n; i += 2){
			List<Integer> toNewMap = new ArrayList<>();
			for (int j = 0; j < n; j += 2) {
				List<Integer> tmp = new ArrayList<>();
				tmp.add(map.get(i).get(j));
				tmp.add(map.get(i).get(j + 1));
				tmp.add(map.get(i + 1).get(j));
				tmp.add(map.get(i + 1).get(j + 1));
				tmp.sort(Comparator.naturalOrder());
				toNewMap.add(tmp.get(2));
			}
			newMap.add(toNewMap);
		}
		map = newMap;
	}

}
