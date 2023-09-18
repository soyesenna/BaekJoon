
import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
	
	public static List<List<Character>> puyo = new ArrayList<>();
	public static List<List<Integer>> direction = List.of(
			List.of(-1, 0),
			List.of(0, 1),
			List.of(1, 0),
			List.of(0, -1)
			);

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int i = 0; i < 12; i++) {
			char[] tmp = br.readLine().toCharArray();
			List<Character> tmpList = new ArrayList<>();
			IntStream.range(0, tmp.length)
					.forEach((j) -> tmpList.add(tmp[j]));
			puyo.add(tmpList);
		}
		
		int result = 0;
		while (bfs()) {
			result++;
			setGravity();
			//System.out.println(puyo);
		}
		System.out.println(result);
	}
	
	public static void setGravity() {
		for (int i = 10; i >= 0; i--) {
			for (int j = 0; j < 6; j++) {
				if (puyo.get(i).get(j) != '.') {
					int now = i;
					char nowColor = puyo.get(i).get(j);
					while (now < 11 && puyo.get(now + 1).get(j) == '.') {
						puyo.get(now).set(j, '.');
						puyo.get(now + 1).set(j, nowColor);
						now++;
					}
				}
			}
		}
	}
	
	public static boolean bfs() {
		boolean flag = false;
		Deque<List<Integer>> queue = new ArrayDeque<>();
		for (int i = 0; i < 12; i++) {
			for (int j = 0; j < 6; j++) {
				if (puyo.get(i).get(j) != '.') {
					Set<List<Integer>> visit = new HashSet<>();
					char nowColor = puyo.get(i).get(j);
					queue.add(List.of(i, j));
					visit.add(List.of(i, j));
					while (!queue.isEmpty()) {
						List<Integer> now = queue.pollFirst();
						for (List<Integer> dir : direction) {
							int nowR = now.get(0) + dir.get(0);
							int nowC = now.get(1) + dir.get(1);
							if (inRange(nowR, nowC) && !visit.contains(List.of(nowR, nowC)) && puyo.get(nowR).get(nowC) == nowColor) {
								queue.add(List.of(nowR, nowC));
								visit.add(List.of(nowR, nowC));
							}
						}
					}
					if (visit.size() >= 4) {
						boom(visit);
						flag = true;
					}
				}
			}
		}
		return flag;
	}
	
	public static void boom(Set<List<Integer>> visit) {
		visit.stream()
			.forEach((li) -> {
				puyo.get(li.get(0)).set(li.get(1), '.');
			});
	}
	
	public static boolean inRange(int r, int c) {
		return r >= 0 && r < 12 && c >= 0 && c < 6;
	}

}
