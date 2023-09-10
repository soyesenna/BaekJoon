
import java.io.*;
import java.util.*;
import java.util.Map.Entry;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int k = Integer.parseInt(br.readLine());
		
		List<Integer> recommend = new ArrayList<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < k; i++) recommend.add(Integer.parseInt(st.nextToken()));
		
		List<Integer> pictures = new ArrayList<>();
		List<Integer> count = new ArrayList<>();
		//Map<Integer, Integer> picMap = new HashMap<>();
		for (int now : recommend) {
			int index = pictures.indexOf(now);
			if (index != -1) count.set(index, count.get(index) + 1); 
			else {
				if (pictures.size() < n) {
					pictures.add(now);
					count.add(1);
				}else {
					Optional<Integer> minVal = count.stream()
													.sorted(Comparator.naturalOrder())
													.findFirst();
					
					int minIndex = count.indexOf(minVal.get());
					pictures.remove(minIndex);
					count.remove(minIndex);
					
					pictures.add(now);
					count.add(1);
				}
			}
		}
		
		pictures.stream()
				.sorted(Comparator.naturalOrder())
				.forEach((Integer a) -> System.out.print(a + " "));
		
	}

}
