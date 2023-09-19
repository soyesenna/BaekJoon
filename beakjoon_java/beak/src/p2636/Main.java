package p2636;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int R;
	public static int C;
	public static List<List<Integer>> cheese = new ArrayList<>();
	public static List<List<Integer>> air = new ArrayList<>();
	public static List<List<Integer>> direction = List.of(
			List.of(-1, 0),
			List.of(0, 1),
			List.of(1, 0),
			List.of(0, -1)
			);
	public static int time = 0;
	public static int beforeCheese = 0;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < R; i++) {
			String[] tmp = br.readLine().split(" ");
			List<Integer> tmpList = new ArrayList<>();
			for (String s : tmp) tmpList.add(Integer.parseInt(s));
			cheese.add(tmpList);
		}
		
		findAir();
		while (meltCheese()) {
			time++;
			findAir();
		}
		System.out.println(time);
		System.out.println(beforeCheese);
		
	}
	
	public static int numCheese() {
		int num = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (cheese.get(i).get(j) == 1) num++;
			}
		}
			
		return num;
				
	}
	
	
	public static boolean meltCheese() {
		int nowNumCheese = numCheese();
		if (nowNumCheese == 0) {
			return false;
		}else beforeCheese = nowNumCheese;
		
		List<List<Integer>> tmp = new ArrayList<>();
		for (int i = 0; i < R; i++) {
			List<Integer> tmpList = new ArrayList<>();
			for (int j = 0; j < C; j++) {
				boolean flag = false;
				if (cheese.get(i).get(j) == 1) {
					for (List<Integer> dir : direction) {
						int nowR = i + dir.get(0);
						int nowC = j + dir.get(1);
						if (inRange(nowR, nowC) && air.contains(List.of(nowR, nowC))) {
							tmpList.add(0);
							flag = true;
							break;
						}
					}
					if (!flag) tmpList.add(1);
				}else tmpList.add(0);
			}
			tmp.add(tmpList);
		}
		cheese = tmp;
		return true;
	}
	
	public static void findAir() {
		Deque<List<Integer>> queue = new ArrayDeque<>();
		Set<List<Integer>> visit = new HashSet<>();
		List<List<Integer>> tmpAir = new ArrayList<>();
		visit.add(List.of(0, 0));
		queue.add(List.of(0, 0));
		
		while (!queue.isEmpty()) {
			//System.out.println("air");
			List<Integer> now = queue.pollFirst();
			visit.add(now);
			tmpAir.add(now);
			for (List<Integer> dir : direction) {
				int nowR = now.get(0) + dir.get(0);
				int nowC = now.get(1) + dir.get(1);
				if (inRange(nowR, nowC) && !visit.contains(List.of(nowR, nowC)) && cheese.get(nowR).get(nowC) == 0) {
					queue.add(List.of(nowR, nowC));
					visit.add(List.of(nowR, nowC));
				}
			}
		}
		air = tmpAir;
	}
	
	public static boolean inRange(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}

}
