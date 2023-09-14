package codetree_3_3_2_3;

import java.io.*;
import java.util.*;

public class Main {
	
	public static int N;
	public static int[] list;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		list = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) list[i] = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) selectSort(i);
		
		for (int n : list) System.out.print(n + " ");

	}
	
	public static void selectSort(int start) {
		int min = start;
		for (int i = start; i < N; i++) {
			if (list[i] < list[min]) {
				min = i;
			}
		}
			int tmp = list[start];
			list[start] = list[min];
			list[min] = tmp;

	}

}
