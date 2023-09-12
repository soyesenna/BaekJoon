
import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static int M;
	public static int d;
	public static int r;
	public static int c;
	public static Map<Integer, List<Integer>> direction = new HashMap<>();
	public static List<List<Integer>> room = new ArrayList<>();
	public static int cleanCnt = 0;

	public static void main(String[] args) throws Exception{
		getInput();
		
		boolean lastFlag = true;
		while (lastFlag) {
			clean();
			if (checkNext()) while (turnAndGo());
			else {
				if (!back()) lastFlag = false;
			}
		}
		
		System.out.println(cleanCnt);
	}
	
	public static boolean back() {
		int tmpD = d - 2;
		if (tmpD < 0) tmpD += 4;
		if (room.get(r + direction.get(tmpD).get(0)).get(c + direction.get(tmpD).get(1)) != 1) {
			r += direction.get(tmpD).get(0);
			c += direction.get(tmpD).get(1);
			return true;
		}
		return false;
	}
	
	public static boolean turnAndGo() {
		d--;
		if (d < 0) d += 4;
		if (room.get(r + direction.get(d).get(0)).get(c + direction.get(d).get(1)) == 0) {
			r += direction.get(d).get(0);
			c += direction.get(d).get(1);
			return false;
		}
		return true;
	}
	
	public static boolean checkNext() {
		for (int i = 0; i < 4; i++) {
			if (room.get(r + direction.get(i).get(0)).get(c + direction.get(i).get(1)) == 0){
				return true;
			}
		}
		return false;
	}
	
	public static void clean() {
		if (room.get(r).get(c) == 0) {
			room.get(r).set(c, 2);
			cleanCnt++;
		}
	}
	
	public static void getInput() throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		direction.put(0, List.of(-1, 0));
		direction.put(1, List.of(0, 1));
		direction.put(2, List.of(1, 0));
		direction.put(3, List.of(0, -1));
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st1.nextToken());
		c = Integer.parseInt(st1.nextToken());
		
		//0 : up, 1 : right, 2 : down, 3 : left 
		d = Integer.parseInt(st1.nextToken());
		
		for (int i = 0; i < N; i++) {
			String[] tmp = br.readLine().split(" ");
			List<Integer> tmpList = new ArrayList<>();
			for (String s: tmp) tmpList.add(Integer.parseInt(s));
			room.add(tmpList);
		}
		
		
	}

}
