package goorm2;

import java.io.*;
import java.util.*;
import java.time.*;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int t = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		List<Long> times = new ArrayList<>();
		for (int i = 0; i < n; i++) times.add(Long.parseLong(br.readLine()));
		
		LocalDate ld = LocalDate.now();
		LocalTime lt = LocalTime.of(t, m);
		
		LocalDateTime ldtStart = LocalDateTime.of(ld, lt);
		
		for (long time : times) ldtStart = ldtStart.plusMinutes(time);
		
		System.out.println(ldtStart.getHour() + " " + ldtStart.getMinute());
		
	}

}
