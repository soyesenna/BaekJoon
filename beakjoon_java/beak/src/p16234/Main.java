package p16234;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static int L;
	public static int R;
	public static List<List<Integer>> map = new ArrayList<>();
	public static List<List<Integer>> direction = List.of(
			List.of(-1, 0),
			List.of(0, 1),
			List.of(1, 0),
			List.of(0, -1)
			);
	public static int result = 0;
	

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) {
			String[] tmp = br.readLine().split(" ");
			List<Integer> tmpList = new ArrayList<>();
			for (String s : tmp) tmpList.add(Integer.parseInt(s));
			map.add(tmpList);
		}
		
		List<List<List<Integer>>> union = bfs();
		while (!union.isEmpty()) {
			result++;
			move(union);
			union = bfs();
		}
		System.out.println(result);
	}
	
	public static void move(List<List<List<Integer>>> union) {
		for (List<List<Integer>> nowUnion : union) {
			int persons = 0;
			for (List<Integer> now : nowUnion) {
				persons += map.get(now.get(0)).get(now.get(1));
			}
			persons = (int) (persons / nowUnion.size());
			for (List<Integer> now : nowUnion) {
				map.get(now.get(0)).set(now.get(1), persons);
			}
		}
	}
	
	public static List<List<List<Integer>>> bfs(){
		List<List<List<Integer>>> union = new ArrayList<>();
	
		Set<List<Integer>> visit = new HashSet<>();
		Deque<List<Integer>> queue = new ArrayDeque<>();
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
					visit.add(List.of(i, j));
					queue.add(List.of(i, j));
					List<List<Integer>> nowUnion = new ArrayList<>();
					while (!queue.isEmpty()) {
						List<Integer> now = queue.pollFirst();
						//System.out.println(now);
						nowUnion.add(now);
						visit.add(now);
						for (List<Integer> dir : direction) {
							int nowR = now.get(0) + dir.get(0);
							int nowC = now.get(1) + dir.get(1);
							if (!visit.contains(List.of(nowR, nowC)) && inRange(nowR, nowC) && canUnion(now, List.of(nowR, nowC))) {
								//nowUnion.add(List.of(nowR, nowC));
								visit.add(List.of(nowR, nowC));
								queue.add(List.of(nowR, nowC));
							}
						}
					}
					if (nowUnion.size() > 1) union.add(nowUnion);
				
			}
		}
		
		return union;
	}
	
	public static boolean canUnion(List<Integer> now, List<Integer> check) {
		int c = Math.abs(map.get(now.get(0)).get(now.get(1)) - map.get(check.get(0)).get(check.get(1)));
		if (c >= L && c <= R) return true;
		return false;
	}
	
	public static boolean inRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}

}
