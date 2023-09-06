
import java.io.*;
import java.util.*;
import java.util.Map.Entry;


public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int k = Integer.parseInt(st.nextToken());
		int l = Integer.parseInt(st.nextToken());
		
		Map<String, Integer> map = new HashMap<>();
		
		for (int i = 0; i < l; i++) {
			String num = br.readLine();
			if (map.containsKey(num)) {
				map.replace(num, i);
			}else map.put(num, i);
		}

		List<Entry<String, Integer>> s = new ArrayList<>(map.entrySet());
		s.sort((Entry<String, Integer> a, Entry<String, Integer> b) -> a.getValue() - b.getValue());
		
		for (int i = 0; i < k; i++) {
			if (i >= map.size()) break;
			System.out.println(s.get(i).getKey());
		}
	}

}
