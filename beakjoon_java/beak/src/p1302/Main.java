package p1302;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		List<String> books = new ArrayList<>();
		
		for (int i = 0; i < n; i++) books.add(br.readLine());
		
		int max = 0;
		
		List<String> result = new ArrayList<>();
		
		for (String book : books) {
			int nowBookNum = Collections.frequency(books, book);
			if (nowBookNum >= max) max = nowBookNum;
		}
		
		for (String book : books) {
			
		}
		
		Collections.sort(result);
		System.out.println(result.get(0));
	}

}
