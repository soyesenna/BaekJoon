
import java.io.*;
import java.util.*;
public class Main {

    public static int N;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        List<Integer> numsA = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            numsA.add(Integer.parseInt(st.nextToken()));
        }

        Collections.sort(numsA);

        Deque<Integer> nums = new ArrayDeque<>(numsA);

        int start = 0;
        while (!nums.isEmpty()) {
            int now = nums.pollFirst();
            if (start == 0 && now != 1) {
                System.out.println(1);
                System.exit(0);
            }
            int before = 0;
            if (now - start == 1) before = start + 1;
            else before = start;
            for (int i = 1; i < start + 1; i++) {
                int n = i + now;
                if (n - before > 1){
                    System.out.println(before + 1);
                    System.exit(0);
                }
                before = n;
            }
            start += now;
        }
        int result = 0;
        for (Integer num : numsA) {
            result += num;
        }
        System.out.println(result + 1);
    }
}
