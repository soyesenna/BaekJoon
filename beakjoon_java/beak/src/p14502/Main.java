package p14502;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static int M;
	public static List<List<Integer>> lab = new ArrayList<>();
	public static List<List<Integer>> canWall = new ArrayList<>();
	public static List<List<Integer>> virus = new ArrayList<>();
	public static List<List<Integer>> direction = List.of(
			List.of(-1, 0),//up
			List.of(0, 1),//right
			List.of(1, 0),//down
			List.of(0, -1)//left
			);
	public static int result = 0;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) {
			String[] tmp = br.readLine().split(" ");
			List<Integer> liTmp = new ArrayList<>();
			for (int j = 0; j < M; j++) {
				int now = Integer.parseInt(tmp[j]);
				if (now == 0) canWall.add(List.of(i, j));
				else if (now == 2) virus.add(List.of(i, j));
				liTmp.add(now);
			}
			lab.add(liTmp);
		}
		
		//System.out.println(canWall);
		
		for (int i = 0; i < canWall.size() - 2; i++) {
			lab.get(canWall.get(i).get(0)).set(canWall.get(i).get(1), 1);
			for (int j = i + 1; j < canWall.size() - 1; j++) {
				lab.get(canWall.get(j).get(0)).set(canWall.get(j).get(1), 1);
				for (int k = j + 1; k < canWall.size(); k++) {
					//System.out.println(k);
					lab.get(canWall.get(k).get(0)).set(canWall.get(k).get(1), 1);
					bfs();
					lab.get(canWall.get(k).get(0)).set(canWall.get(k).get(1), 0);
				}
				lab.get(canWall.get(j).get(0)).set(canWall.get(j).get(1), 0);
			}
			lab.get(canWall.get(i).get(0)).set(canWall.get(i).get(1), 0);
		}
		
		System.out.println(result);
	}
	
	public static void bfs() {
		List<List<Integer>> copy = deepCopy();
		Deque<List<Integer>> queue = new ArrayDeque<>();
		
		for (int i = 0; i < virus.size(); i++) {
			List<Integer> nowVirus = virus.get(i);
			queue.add(nowVirus);
			while (queue.size() != 0) {
				List<Integer> now = queue.pollFirst();
				int nowR = now.get(0);
				int nowC = now.get(1);
				for (int j = 0; j < 4; j++) {
					int nextR = nowR + direction.get(j).get(0);
					int nextC = nowC + direction.get(j).get(1);
					if (inRange(nextR, nextC) && copy.get(nextR).get(nextC) == 0) {
						copy.get(nextR).set(nextC, 2);
						queue.add(List.of(nextR, nextC));
					}
				}
			}
		}
		//System.out.println(copy);
		checkVirus(copy);
	}
	
	public static void checkVirus(List<List<Integer>> copy) {
		int nowResult = 0;
		for (int i = 0; i < N; i++) nowResult += Collections.frequency(copy.get(i), 0);
		if (nowResult > result) result = nowResult;
	}
	
	public static boolean inRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M;
	}
	
	public static List<List<Integer>> deepCopy(){
		List<List<Integer>> copy = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			List<Integer> tmp = new ArrayList<>();
			for (int j = 0; j < M; j++) tmp.add(lab.get(i).get(j));
			copy.add(tmp);
		}
		
		return copy;
	}

}
