package p23970;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static List<Integer> origin = new ArrayList<>();
	public static List<Integer> target = new ArrayList<>();
	public static boolean result = false;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		String[] inputOrigin = br.readLine().split(" ");
		for (String s : inputOrigin) origin.add(Integer.parseInt(s));
		
		String[] inputTarget = br.readLine().split(" ");
		for (String s: inputTarget) target.add(Integer.parseInt(s));
		
		if (check()) {
			System.out.println(1);
			System.exit(0);
		}
		
		while(bubbleSort());
		
		if (result) System.out.println(1);
		else System.out.println(0);
	}
	
	public static boolean bubbleSort() {
		boolean flag = false;
		for (int last = N; last > 2; last--) {
			for (int i = 1; i < last - 1; i++) {
				if (origin.get(i) > origin.get(i + 1)) {
					int tmp = origin.get(i);
					origin.set(i, origin.get(i + 1));
					origin.set(i + 1, tmp);
					flag = true;
					if (check()) {
						result = true;
						return false;
					}
				}
			}
		}
		return flag;
	}
	
	public static boolean check() {
		for(int i = 0; i < N; i++) if (origin.get(i) != target.get(i)) return false;
		
		return true;
	}

}
