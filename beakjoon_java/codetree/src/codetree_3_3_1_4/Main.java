package codetree_3_3_1_4;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int[] list;
	public static int N;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		list = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) list[i] = Integer.parseInt(st.nextToken());
		
		while (bubbleSort());
		
		for (int n : list) {
			System.out.print(n + " ");
		}
	}
	
	public static boolean bubbleSort() {
		boolean result = false;
		for (int i = 0; i < N - 1; i++) {
			if (list[i] > list[i + 1]){
				int tmp = list[i];
				list[i] = list[i + 1];
				list[i + 1] = tmp;
				result = true;
			}
		}
		return result;
	}

}
