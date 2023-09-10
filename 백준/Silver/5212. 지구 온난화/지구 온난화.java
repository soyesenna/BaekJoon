
import java.util.*;
import java.io.*;

public class Main {
	
	public static List<List<Integer>> direction = 
			List.of(List.of(-1, 0), List.of(0, 1), List.of(1, 0), List.of(0, -1));
	
	public static List<String> oldMap = new ArrayList<>();
	
	public static List<StringBuffer> newMap = new ArrayList<>();
	
	public static int R;
	public static int C;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		
		for (int i = 0; i < R; i++) oldMap.add(br.readLine());
		
		
		for (int i = 0; i < R; i++) {
			StringBuffer tmp = new StringBuffer();
			for (int j = 0; j < C; j++) {
				if (oldMap.get(i).charAt(j) == '.') tmp.append('.');
				else tmp.append(checkIsland(i, j));
			}
			newMap.add(tmp);
		}
		
		for (int i = minRowIndex(); i <= maxRowIndex(); i++) {
			for (int j = minColIndex(); j <= maxColIndex(); j++) {
				System.out.print(newMap.get(i).charAt(j));
			}
			System.out.println();
		}
	}
	
	public static char checkIsland(int r, int c) {
		int count = 0;
		for (List<Integer> dir : direction) {
			if ((r + dir.get(0) >= 0 && r + dir.get(0) < R && c + dir.get(1) >= 0 && c + dir.get(1) < C) ) {
				if (oldMap.get(r + dir.get(0)).charAt(c + dir.get(1)) == '.') count++;
			}else count++;
		}
		
		if (count >= 3) return '.';
		else return 'X';
	}
	
	public static int minRowIndex(){
		for (int i = 0; i < R; i++) {
			int index = newMap.get(i).indexOf("X");
			if (index != -1) return i;
		}
		return -1;
	}
	
	public static int maxRowIndex() {
		for(int i = R - 1; i >= 0; i--) {
			int index = newMap.get(i).indexOf("X");
			if (index != -1) return i;
		}
		return -1;
	}
	
	public static int minColIndex() {
		for(int i = 0; i < C; i++) {
			for (int j = 0; j < R; j++) {
				if (newMap.get(j).charAt(i) == 'X') return i;
			}
		}
		return -1;
	}
	
	public static int maxColIndex() {
		for(int i = C - 1; i >= 0; i--) {
			for (int j = 0; j < R; j++) {
				if (newMap.get(j).charAt(i) == 'X') return i;
			}
		}
		return -1;
	}

}
