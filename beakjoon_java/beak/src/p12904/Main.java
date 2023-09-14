package p12904;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String origin = br.readLine();
		StringBuffer target = new StringBuffer(br.readLine());
		
		while (origin.length() < target.length()) {
			if (target.charAt(target.length() - 1) == 'A') target.deleteCharAt(target.length() - 1);
			else {
				target.deleteCharAt(target.length() - 1);
				target.reverse();
			}
		}
		
		if (origin.contentEquals(target)) System.out.println(1);
		else System.out.println(0);
		
	}

}
