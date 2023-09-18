
import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static int M;
	public static List<List<Integer>> map = new ArrayList<>();
	public static List<List<Integer>> direction = List.of(
			List.of(-1, 0),
			List.of(0, 1),
			List.of(1, 0),
			List.of(0, -1)
			);
	public static int year = 0;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) {
			String[] tmp = br.readLine().split(" ");
			List<Integer> tmpList = new ArrayList<>();
			for (String s : tmp) tmpList.add(Integer.parseInt(s));
			map.add(tmpList);
		}
		
		int ice = iceCnt();
		
		while (ice < 2) {
			year++;
			melting();
			ice = iceCnt();
			if (ice <= 0) {
				System.out.println(0);
				System.exit(0);
			}
		}
		System.out.println(year);
	}
	
	public static int iceCnt() {
		int result = 0;
		
		Deque<List<Integer>> stack = new ArrayDeque<>();
		Set<List<Integer>> visit = new HashSet<>();
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map.get(i).get(j) != 0 && !visit.contains(List.of(i ,j))) {
					result++;
					stack.add(List.of(i, j));
					visit.add(List.of(i, j));
					while(!stack.isEmpty()) {
						List<Integer> now = stack.pollLast();
						for (List<Integer> dir : direction) {
							int nowR = now.get(0) + dir.get(0);
							int nowC = now.get(1) + dir.get(1);
							if (inRange(nowR, nowC) && map.get(nowR).get(nowC) != 0 && !visit.contains(List.of(nowR, nowC))) {
								stack.add(List.of(nowR, nowC));
								visit.add(List.of(nowR, nowC));
							}
						}
					}
				}
			}
		}
		return result;
	}
	
	public static void melting() {
		boolean flag = false;
		List<List<Integer>> tmp = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			List<Integer> tmpList = new ArrayList<>();
			for (int j = 0; j < M; j++) {
				if (map.get(i).get(j) == 0) tmpList.add(0);
				else {
					flag = true;
					int meltCnt = 0;
					for (List<Integer> dir : direction) {
						int nowR = i + dir.get(0);
						int nowC = j + dir.get(1);
						if (inRange(nowR, nowC) && map.get(nowR).get(nowC) == 0) meltCnt++;	
					}
					tmpList.add(reLu(map.get(i).get(j) - meltCnt));
				}
			}
			tmp.add(tmpList);
		}
		map = tmp;
		//return flag;
	}
	
	public static int reLu(int n) {
		if (n < 0) return 0;
		return n;
	}
	
	public static boolean inRange(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < M;
	}

}
