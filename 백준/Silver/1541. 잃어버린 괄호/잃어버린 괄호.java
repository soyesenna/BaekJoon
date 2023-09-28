
import java.io.*;
import java.util.*;

public class Main {

    public static List<Integer> result = new ArrayList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String order = br.readLine();
        StringTokenizer nums = new StringTokenizer(order, "+-");
        StringTokenizer ops = new StringTokenizer(order, "0123456789");

        while (nums.hasMoreTokens()) {
            int num = Integer.parseInt(nums.nextToken());
            if (result.isEmpty()){
                result.add(num);
                continue;
            }
            if (ops.hasMoreTokens()) {
                String op = ops.nextToken();
                if (op.contentEquals("+")) {
                    result.set(result.size() - 1, result.get(result.size() - 1) + num);
                }else{
                    result.add(num);
                }
            }

        }


        Optional<Integer> re = result.stream().reduce((a, b) -> a - b);
        System.out.println(re.get());
    }
}
