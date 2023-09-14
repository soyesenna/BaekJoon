package p16496;

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		String[] inputStr = br.readLine().split(" ");
		
		List<String> li = new ArrayList<>(); 
		
		for (String s: inputStr) li.add(s);
		//BigInteger zero = BigInteger.ZERO; 
		Collections.sort(li, (String a, String b) -> {
			
			if (a.length() == b.length()) {
				BigInteger tmp = BigInteger.valueOf(Long.parseLong(b) - Long.parseLong(a));
				
				if (tmp.compareTo(BigInteger.ZERO) > 0) return 1;
				else if (tmp.compareTo(BigInteger.ZERO) == 0) return 0;
				else return -1;
			}
			else {
				BigInteger val1 = new BigInteger(b.concat(a));
				BigInteger val2 = new BigInteger(a.concat(b));
				BigInteger tmp = (val1.subtract(val2));
				if (tmp.compareTo(BigInteger.ZERO) > 0) return 1;
				else if (tmp.compareTo(BigInteger.ZERO) == 0) return 0;
				else return -1;
			}
		});
		
		//System.out.println(li);
		
		StringBuffer result = new StringBuffer();
		for (String s : li) result.append(s);
		BigInteger intResult = new BigInteger(result.toString());
		if (intResult.compareTo(BigInteger.ZERO) == 0) System.out.println(0);
		else System.out.println(result);
	}

}
