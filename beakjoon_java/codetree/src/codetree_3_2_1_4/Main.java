package codetree_3_2_1_4;

import java.io.*;
import java.util.*;

public class Main {
	
	public static List<Integer> result = new ArrayList<>();

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		
		for(int i = 0; i < n; i++) {
			String[] input = br.readLine().split(" ");
			if (input[0].equals("push_back")) pushBack(Integer.parseInt(input[1]));
			else if(input[0].equals("pop_back")) popBack();
			else if(input[0].equals("size")) System.out.println(result.size());
			else System.out.println(result.get(Integer.parseInt(input[1]) - 1));
		}
	}
	
	public static void pushBack(int num) {
		result.add(num);
	}
	
	public static void popBack() {
		result.remove(result.size() - 1);
	}

}
