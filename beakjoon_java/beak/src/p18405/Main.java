package p18405;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static int K;
	public static int S;
	public static int x;
	public static int y;
	public static List<List<Integer>> plask = new ArrayList<>();

	public static void main(String[] args) throws Exception{
		input();
		while (S > 0) {
			
		}
	}
	
	public static void input() throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());


        StringTokenizer st1 = new StringTokenizer(br.readLine());
		S = Integer.parseInt(st1.nextToken());
		x = Integer.parseInt(st1.nextToken());
		y = Integer.parseInt(st1.nextToken());
	}

}
