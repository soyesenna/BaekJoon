package p1380;


import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int idx = 1;
		while(true) {
			int n = Integer.parseInt(br.readLine());
			if (n == 0) break;
			List<String> names = new ArrayList<>();
			boolean[] c = new boolean[n];
			for(int i = 0; i < n; i++) {
				names.add(br.readLine());
				c[i] = true;
			}
			for (int i = 0; i < 2 * n - 1; i++) {
				String[] line = br.readLine().split(" ");
				int k = Integer.parseInt(line[0]) - 1;
				c[k] = !c[k];
			}
			int k = IntStream.range(0, n).filter(i -> !c[i]).findFirst().orElse(-1);
			System.out.println(idx++ + " " + names.get(k));
		}
	}
}
