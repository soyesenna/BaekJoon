package p1283;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		List<StringBuffer> strs = new ArrayList<>();
		for (int i = 0; i < n; i++) strs.add(new StringBuffer(br.readLine()));
		
		Set<Character> result = new HashSet<>();
		
		List<String> r = new ArrayList<>();
		
		for(StringBuffer str : strs) {
			boolean flag = false;
			String[] s = String.valueOf(str).split(" ");
			for(int i = 0; i < s.length; i++) {
				if (s[i].isEmpty()) continue;
				if (!result.contains(s[i].toLowerCase().charAt(0))) {
					result.add(s[i].toLowerCase().charAt(0));
					s[i] = new String("[" + s[i].charAt(0) + "]" + s[i].substring(1));
					
					flag = true;
					break;
				}
			}
			if (!flag) {
				flag = true;
			for (int i = 0; i < str.length(); i++) {
				char c = String.valueOf(str).toLowerCase().charAt(i);
				if (c == ' ') continue;
				if(!result.contains(c)) {
					result.add(c);
					str.insert(i + 1,"]");
					str.insert(i, "[");
					r.add(String.valueOf(str));
					flag = false;
					break;
				}
			}
			if (flag) {
				r.add(String.valueOf(str));
			}
		}else {
			r.add(String.join(" ", s));
		}
		}
		for (String res : r) {
			for (int i = 0; i < res.length(); i++) System.out.print(res.charAt(i));
			System.out.println();
		}
	}
				

}
