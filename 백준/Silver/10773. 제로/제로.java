
import java.io.*;
import java.util.*;
public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < K; i++) {
            int now = Integer.parseInt(br.readLine());
            if (now == 0) stack.pollLast();
            else stack.addLast(now);
        }

        System.out.println(stack.stream().reduce(0, (a, b) -> a + b));

        
    }
}
