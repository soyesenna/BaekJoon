package p14500;

import java.io.*;
import java.util.*;

public class Main {

	public static int N;
	public static int M;
	public static List<List<Integer>> map = new ArrayList<>();
	public static int result = Integer.MIN_VALUE;
	public static List<List<Integer>> direction = List.of(
			List.of(0, -1),
			List.of(1, 0),
			List.of(-1, 0),
			List.of(0, 1)
			);
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		//p16236.Main.input(br, N, map);

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				List<List<Integer>> visit = new ArrayList<>();
				dfs(i, j, visit);
				bfs(i, j);
			}
		}
		System.out.println(result);
	}
	
	public static void bfs(int r, int c) {
		Deque<List<Integer>> queue = new ArrayDeque<>();
		Set<List<Integer>> visit = new HashSet<>();
		queue.add(List.of(r, c));
		visit.add(List.of(r, c));

		while (!queue.isEmpty()) {
			List<Integer> now = queue.pollFirst();
			visit.add(now);
			if (visit.size() >= 4) {
				List<List<Integer>> tmpVisit = new ArrayList<>(visit);
				int n = 0;
				for (int i = 0; i < visit.size(); i++) {
					n += map.get(tmpVisit.get(i).get(0)).get(tmpVisit.get(i).get(1));
				}
				if (result < n) result = n;
				visit.remove(now);
				continue;
			}
			for (List<Integer> dir : direction) {
				int nowR = now.get(0) + dir.get(0);
				int nowC = now.get(1) + dir.get(1);
				if (inRange(nowR, nowC) && !visit.contains(List.of(nowR, nowC))) {
					queue.add(List.of(nowR, nowC));
					//visit.add(List.of(nowR, nowC));
				}
			}
		}
	}
	
	public static void dfs(int r, int c, List<List<Integer>> visit) {
		if (visit.size() >= 4) {
			int n = 0;
			for (int i = 0; i < 4; i++) n += map.get(visit.get(i).get(0)).get(visit.get(i).get(1));
			if (n > result) result = n;
			return;
		}

		for (List<Integer> dir : direction) {
			int nowR = r + dir.get(0);
			int nowC = c + dir.get(1);
			if (inRange(nowR, nowC) && !visit.contains(List.of(nowR, nowC))) {
				visit.add(List.of(nowR, nowC));
				dfs(nowR, nowC, visit);
				visit.remove(List.of(nowR, nowC));
			}
		}

	}
	
	public static boolean inRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M;
	}

}
