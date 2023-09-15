package p3190;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static int K;
	public static int L;
	public static List<List<Integer>> apples = new ArrayList<>();
	public static Deque<List<Integer>> snake = new ArrayDeque<>();
	public static List<Integer> rotateTime = new ArrayList<>();
	public static List<String> rotateOrder = new ArrayList<>();
	public static List<List<Integer>> direction = List.of(
			List.of(-1, 0),//up
			List.of(0, 1),//right
			List.of(1, 0),//down
			List.of(0, -1)//left
			);
	
	public static int nowHead = 1;
	public static int nowR = 0;
	public static int nowC = 0;
	public static int nowTime = 0;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		K = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < K; i++) {
			String[] tmp = br.readLine().split(" ");
			apples.add(List.of(Integer.parseInt(tmp[0]), Integer.parseInt(tmp[1])));
		}
		
		L = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < L; i++) {
			String[] tmp = br.readLine().split(" ");
			rotateTime.add(Integer.parseInt(tmp[0]));
			rotateOrder.add(tmp[1]);
		}
		
		snake.add(List.of(0, 0));
		
		while (doGame());
		
		System.out.println(nowTime);
	}
	
	public static boolean doGame() {
		nowTime++;
		nowR += direction.get(nowHead).get(0);
		nowC += direction.get(nowHead).get(1);
		if (check()) {
			snake.add(List.of(nowR, nowC));
			if (!apples.contains(List.of(nowR, nowC))) {
				snake.pollFirst();
			}else apples.remove(List.of(nowR, nowC));
		}else return false;
		int ifRotate = rotateTime.indexOf(nowTime);
		if (ifRotate != -1) {
			if (rotateOrder.get(ifRotate).contentEquals("D")) nowHead++;
			else nowHead--;
			if (nowHead >= 4) nowHead -= 4;
			if (nowHead < 0) nowHead += 4;
		}
		return true;
	}
	
	public static boolean check() {
		if (nowR >= 0 && nowR < N && nowC >= 0 && nowC < N && !snake.contains(List.of(nowR, nowC))) return true;
		return false;
	}

}
